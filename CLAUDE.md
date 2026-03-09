# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

YesCaptcha/AntiCaptcha-compatible captcha solving service built with FastAPI + Playwright. Designed as a third-party captcha solver for flow2api. Solves reCAPTCHA v3 by automating Chromium to generate valid tokens, and supports image captcha recognition via OpenAI-compatible vision models.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt
playwright install --with-deps chromium

# Run the server
python main.py

# Run all tests
pytest tests/

# Run a single test
pytest tests/test_api.py::test_health_endpoint -v

# Type checking
pyright
```

## Architecture

**Entrypoint**: `main.py` → imports `src.main:app` and runs uvicorn.

**`src/` layout** (layered: routes → services → models):
- `core/config.py` — Frozen `Config` dataclass from env vars. Singleton `config`.
- `models/task.py` — YesCaptcha API models: `CreateTaskRequest/Response`, `GetTaskResultRequest/Response`, `GetBalanceRequest/Response`.
- `api/routes.py` — Root-level endpoints matching YesCaptcha format: `/createTask`, `/getTaskResult`, `/getBalance`, plus `/api/v1/health`.
- `services/task_manager.py` — In-memory async task queue. `TaskManager` singleton dispatches tasks to registered `Solver` instances via `asyncio.create_task`. Auto-cleans expired tasks (10min TTL).
- `services/recaptcha_v3.py` — `RecaptchaV3Solver` uses Playwright Chromium to visit target pages, execute `grecaptcha.execute()`, and return tokens. Includes anti-detection scripts and retry logic.
- `services/recognition.py` — `CaptchaRecognizer` sends captcha images to an OpenAI-compatible vision model for analysis (Argus-inspired).

**Key patterns**:
- Playwright browser lifecycle managed via FastAPI `lifespan` context manager in `src/main.py`.
- Solvers are registered with `task_manager.register_solver(type, solver)` at startup.
- Tasks are processed asynchronously — `createTask` returns immediately with `taskId`, client polls `getTaskResult`.
- Auth uses YesCaptcha's `clientKey` field (validated against `CLIENT_KEY` env var).

## Environment Variables

- `CLIENT_KEY` — API key for client auth (YesCaptcha clientKey)
- `CAPTCHA_BASE_URL` — OpenAI-compatible API base URL (default: `https://your-openai-compatible-endpoint/v1`)
- `CAPTCHA_API_KEY` — API key for the model endpoint
- `CAPTCHA_MODEL` — Strong model name (default: `gpt-5.4`)
- `CAPTCHA_MULTIMODAL_MODEL` — Vision model name (default: `qwen3.5-2b`)
- `BROWSER_HEADLESS` — Run Chromium headless (default: `true`)
- `BROWSER_TIMEOUT` — Page load timeout in seconds (default: `30`)

## Deployment

Targets Render via `Dockerfile.render` + `render.yaml`. Python 3.11-slim + Playwright Chromium. Port 8000.

## Test Target

reCAPTCHA v3 score detector: `https://antcpt.com/score_detector/`
Site key: `6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf`
