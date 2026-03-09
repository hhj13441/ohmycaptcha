"""Tests for the YesCaptcha-compatible captcha solver API."""

from __future__ import annotations

import asyncio
import importlib
import os
import sys
from pathlib import Path
from types import ModuleType
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    _ = sys.path.insert(0, str(PROJECT_ROOT))

from fastapi.testclient import TestClient


def _load_app(*, client_key: str | None = None) -> TestClient:
    """Reload modules with fresh env vars and return a test client."""
    os.environ.pop("CLIENT_KEY", None)
    os.environ.setdefault("CAPTCHA_BASE_URL", "https://example.com/v1")
    os.environ.setdefault("CAPTCHA_API_KEY", "test-key")
    os.environ.setdefault("CAPTCHA_MODEL", "gpt-5.4")
    os.environ.setdefault("CAPTCHA_MULTIMODAL_MODEL", "qwen3.5-2b")
    os.environ.setdefault("BROWSER_HEADLESS", "true")
    if client_key is not None:
        os.environ["CLIENT_KEY"] = client_key

    config_mod = importlib.import_module("src.core.config")
    routes_mod = importlib.import_module("src.api.routes")
    task_mgr_mod = importlib.import_module("src.services.task_manager")
    main_mod = importlib.import_module("src.main")

    _ = importlib.reload(config_mod)
    _ = importlib.reload(task_mgr_mod)
    _ = importlib.reload(routes_mod)
    main_mod = importlib.reload(main_mod)

    return TestClient(getattr(main_mod, "app"))


def test_health_endpoint() -> None:
    client = _load_app()
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "captcha_model" in body
    assert "captcha_multimodal_model" in body


def test_root_endpoint() -> None:
    client = _load_app()
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "captcha-solver"
    assert "createTask" in body["endpoints"]
    assert isinstance(body["supported_task_types"], list)


def test_root_endpoint_reports_supported_types_when_registered() -> None:
    client = _load_app()
    task_mgr_mod = importlib.import_module("src.services.task_manager")
    mgr = getattr(task_mgr_mod, "task_manager")
    for task_type in [
        "RecaptchaV3TaskProxyless",
        "RecaptchaV3TaskProxylessM1",
        "RecaptchaV3TaskProxylessM1S7",
        "RecaptchaV3TaskProxylessM1S9",
        "ImageToTextTask",
    ]:
        mgr.register_solver(task_type, AsyncMock())
    response = client.get("/")
    body = response.json()
    assert set(body["supported_task_types"]) == {
        "RecaptchaV3TaskProxyless",
        "RecaptchaV3TaskProxylessM1",
        "RecaptchaV3TaskProxylessM1S7",
        "RecaptchaV3TaskProxylessM1S9",
        "ImageToTextTask",
    }


def test_get_balance() -> None:
    client = _load_app()
    response = client.post("/getBalance", json={"clientKey": "any"})
    assert response.status_code == 200
    body = response.json()
    assert body["errorId"] == 0
    assert body["balance"] > 0


def test_get_balance_requires_client_key() -> None:
    client = _load_app(client_key="secret")
    bad = client.post("/getBalance", json={"clientKey": "wrong"})
    good = client.post("/getBalance", json={"clientKey": "secret"})
    assert bad.json()["errorId"] == 1
    assert good.json()["errorId"] == 0


def test_create_task_unsupported_type() -> None:
    client = _load_app()
    response = client.post(
        "/createTask",
        json={
            "clientKey": "any",
            "task": {"type": "UnsupportedType", "websiteURL": "https://example.com"},
        },
    )
    body = response.json()
    assert body["errorId"] == 1
    assert body["errorCode"] == "ERROR_TASK_NOT_SUPPORTED"


def test_create_task_missing_fields() -> None:
    client = _load_app()
    # Without lifespan, no solvers are registered, so first register a mock solver
    task_mgr_mod = importlib.import_module("src.services.task_manager")
    mgr = getattr(task_mgr_mod, "task_manager")
    mgr.register_solver("RecaptchaV3TaskProxyless", AsyncMock())
    try:
        response = client.post(
            "/createTask",
            json={
                "clientKey": "any",
                "task": {"type": "RecaptchaV3TaskProxyless"},
            },
        )
        body = response.json()
        assert body["errorId"] == 1
        assert body["errorCode"] == "ERROR_TASK_PROPERTY_EMPTY"
    finally:
        mgr._solvers.pop("RecaptchaV3TaskProxyless", None)


def test_create_task_invalid_client_key() -> None:
    client = _load_app(client_key="correct-key")
    response = client.post(
        "/createTask",
        json={
            "clientKey": "wrong-key",
            "task": {
                "type": "RecaptchaV3TaskProxyless",
                "websiteURL": "https://example.com",
                "websiteKey": "key123",
            },
        },
    )
    body = response.json()
    assert body["errorId"] == 1
    assert body["errorCode"] == "ERROR_KEY_DOES_NOT_EXIST"


def test_get_task_result_not_found() -> None:
    client = _load_app()
    response = client.post(
        "/getTaskResult",
        json={"clientKey": "any", "taskId": "nonexistent-id"},
    )
    body = response.json()
    assert body["errorId"] == 1
    assert body["errorCode"] == "ERROR_NO_SUCH_CAPCHA_ID"
