"""Environment-driven application configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    server_host: str
    server_port: int

    # Auth: YesCaptcha clientKey
    client_key: str | None

    # OpenAI-compatible model API
    captcha_base_url: str
    captcha_api_key: str
    captcha_model: str  # strong model (e.g. gpt-5.4)
    captcha_multimodal_model: str  # vision model (e.g. qwen3.5-2b)
    captcha_retries: int
    captcha_timeout: int

    # Playwright browser
    browser_headless: bool
    browser_timeout: int  # seconds


def load_config() -> Config:
    return Config(
        server_host=os.environ.get("SERVER_HOST", "0.0.0.0"),
        server_port=int(os.environ.get("SERVER_PORT", "8000")),
        client_key=os.environ.get("CLIENT_KEY", "").strip() or None,
        captcha_base_url=os.environ.get(
            "CAPTCHA_BASE_URL", "https://your-openai-compatible-endpoint/v1"
        ),
        captcha_api_key=os.environ.get("CAPTCHA_API_KEY", ""),
        captcha_model=os.environ.get("CAPTCHA_MODEL", "gpt-5.4"),
        captcha_multimodal_model=os.environ.get(
            "CAPTCHA_MULTIMODAL_MODEL", "qwen3.5-2b"
        ),
        captcha_retries=int(os.environ.get("CAPTCHA_RETRIES", "3")),
        captcha_timeout=int(os.environ.get("CAPTCHA_TIMEOUT", "30")),
        browser_headless=os.environ.get("BROWSER_HEADLESS", "true").strip().lower()
        in {"1", "true", "yes"},
        browser_timeout=int(os.environ.get("BROWSER_TIMEOUT", "30")),
    )


config = load_config()
