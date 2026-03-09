"""FastAPI application with Playwright lifecycle management."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from .api.routes import router
from .core.config import config
from .services.recognition import CaptchaRecognizer
from .services.recaptcha_v3 import RecaptchaV3Solver
from .services.task_manager import task_manager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

# All RecaptchaV3 task type variants (YesCaptcha compatible)
_RECAPTCHA_V3_TYPES = [
    "RecaptchaV3TaskProxyless",
    "RecaptchaV3TaskProxylessM1",
    "RecaptchaV3TaskProxylessM1S7",
    "RecaptchaV3TaskProxylessM1S9",
]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # ── startup ──
    solver = RecaptchaV3Solver(config)
    await solver.start()
    for task_type in _RECAPTCHA_V3_TYPES:
        task_manager.register_solver(task_type, solver)
    log.info("Registered reCAPTCHA v3 solver for types: %s", _RECAPTCHA_V3_TYPES)

    recognizer = CaptchaRecognizer(config)
    task_manager.register_solver("ImageToTextTask", recognizer)
    log.info("Registered image captcha recognizer: ImageToTextTask")

    yield
    # ── shutdown ──
    await solver.stop()


app = FastAPI(
    title="Captcha Solver Service",
    version="2.0.0",
    description="YesCaptcha-compatible captcha solving service for flow2api.",
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/")
async def root() -> dict[str, object]:
    return {
        "service": "captcha-solver",
        "version": "2.0.0",
        "endpoints": {
            "createTask": "/createTask",
            "getTaskResult": "/getTaskResult",
            "getBalance": "/getBalance",
            "health": "/api/v1/health",
        },
        "supported_task_types": task_manager.supported_types(),
    }
