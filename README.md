<p align="center">
  <img src="https://img.shields.io/badge/OhMyCaptcha-YesCaptcha--style%20API-2F6BFF?style=for-the-badge" alt="OhMyCaptcha">
  <br/>
  <img src="https://img.shields.io/badge/version-public%20repo-22C55E?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-2563EB?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/task%20types-5-F59E0B?style=flat-square" alt="Task Types">
  <img src="https://img.shields.io/badge/runtime-FastAPI%20%7C%20Playwright%20%7C%20OpenAI--compatible-7C3AED?style=flat-square" alt="Runtime">
  <img src="https://img.shields.io/badge/deploy-Render%20%7C%20Hugging%20Face%20Spaces-0F172A?style=flat-square" alt="Deploy">
  <img src="https://img.shields.io/badge/docs-bilingual-2563EB?style=flat-square" alt="Docs">
</p>

<h1 align="center">🧩 OhMyCaptcha</h1>

<p align="center">
  <strong>Self-hostable YesCaptcha-style captcha solver for <a href="https://github.com/OpenClaw/openclaw">flow2api</a> and similar integrations</strong>
  <br/>
  <em>Ship a browser-based reCAPTCHA v3 and multimodal image captcha service with a familiar async task API.</em>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-task-types">Task Types</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-skills">Skills</a> •
  <a href="#-development">Development</a>
</p>

<p align="center">
  <a href="README.zh-CN.md">中文说明</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/">Documentation</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/deployment/render/">Render Guide</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/deployment/huggingface/">Hugging Face Guide</a> •
  <a href="skills/README.md">Skills</a>
</p>

![OhMyCaptcha hero](docs/assets/ohmycaptcha-hero.png)

---

## ✨ What Is This?

**OhMyCaptcha** is a ready-to-deploy self-hosted captcha-solving service that exposes a **YesCaptcha-style async API** for the task types implemented in this repository. It is designed for **flow2api**, internal routing layers, and other systems that expect `createTask` / `getTaskResult` semantics.

### What You Get

- ⚡ **YesCaptcha-style async API** with `createTask`, `getTaskResult`, `getBalance`, and health endpoints
- 🌐 **Browser-based reCAPTCHA v3 solving** through Playwright + Chromium
- 🧠 **OpenAI-compatible multimodal reasoning** for image captcha analysis
- 🏠 **Self-hostable deployment paths** for local use, Render, and Hugging Face Spaces
- 📚 **Bilingual documentation** published through GitHub Pages
- 🧩 **Reusable local skills** for Claude Code, OpenCode, and similar agent workflows
- 🛡️ **Clear capability boundaries** without overstating vendor parity or score guarantees

> OhMyCaptcha is best described as a **self-hostable YesCaptcha-compatible service for the task types implemented here**. It does **not** claim full feature parity with every commercial captcha-solving platform.

---

## 📦 Quick Start

### For Humans

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps chromium

export CLIENT_KEY="your-client-key"
export CAPTCHA_BASE_URL="https://your-openai-compatible-endpoint/v1"
export CAPTCHA_API_KEY="your-api-key"
export CAPTCHA_MODEL="gpt-5.4"
export CAPTCHA_MULTIMODAL_MODEL="qwen3.5-2b"
export BROWSER_HEADLESS="true"
export BROWSER_TIMEOUT="30"

python main.py
```

### Verify Health

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/v1/health
```

### For LLM Agents

Paste this into your agent environment:

```text
Install and validate OhMyCaptcha from this repository. Follow the local setup, configure placeholder environment variables, start the service, verify the health endpoints, and show me how to create a reCAPTCHA v3 task and an ImageToTextTask.
```

---

## 🏗 Architecture

<p align="center">
  <img src="docs/assets/ohmycaptcha-diagram.png" alt="OhMyCaptcha architecture diagram" width="100%">
</p>

### Core Building Blocks

- **FastAPI** powers the HTTP API
- **Playwright + Chromium** generate reCAPTCHA v3 tokens
- **OpenAI-compatible multimodal APIs** analyze image captchas
- **An in-memory async task manager** handles background execution

---

## 🧠 Task Types

### reCAPTCHA v3

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`

All four task types currently use the same browser-based solving path in this codebase.

### Image captcha recognition

- `ImageToTextTask`

`ImageToTextTask` uses an Argus-inspired multimodal recognition prompt, normalizes images into a 1440×900 coordinate space, and returns structured recognition output serialized into `solution.text`.

---

## 🔌 API Surface

| Endpoint | Purpose |
|----------|---------|
| `POST /createTask` | Create an async captcha task |
| `POST /getTaskResult` | Poll task execution result |
| `POST /getBalance` | Return compatibility balance payload |
| `GET /api/v1/health` | Health and service status |

### Create a reCAPTCHA v3 task

```bash
curl -X POST http://localhost:8000/createTask \
  -H "Content-Type: application/json" \
  -d '{
    "clientKey": "your-client-key",
    "task": {
      "type": "RecaptchaV3TaskProxyless",
      "websiteURL": "https://antcpt.com/score_detector/",
      "websiteKey": "6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf",
      "pageAction": "homepage"
    }
  }'
```

### Poll task result

```bash
curl -X POST http://localhost:8000/getTaskResult \
  -H "Content-Type: application/json" \
  -d '{
    "clientKey": "your-client-key",
    "taskId": "uuid-from-createTask"
  }'
```

### Create an image task

```bash
curl -X POST http://localhost:8000/createTask \
  -H "Content-Type: application/json" \
  -d '{
    "clientKey": "your-client-key",
    "task": {
      "type": "ImageToTextTask",
      "body": "<base64-encoded-image>"
    }
  }'
```

---

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `CLIENT_KEY` | Client authentication key used as `clientKey` | unset |
| `CAPTCHA_BASE_URL` | OpenAI-compatible API base URL | `https://your-openai-compatible-endpoint/v1` |
| `CAPTCHA_API_KEY` | API key for the configured model backend | unset |
| `CAPTCHA_MODEL` | Strong text model name | `gpt-5.4` |
| `CAPTCHA_MULTIMODAL_MODEL` | Multimodal model name | `qwen3.5-2b` |
| `CAPTCHA_RETRIES` | Retry count for model or browser operations | `3` |
| `CAPTCHA_TIMEOUT` | Model request timeout in seconds | `30` |
| `BROWSER_HEADLESS` | Whether Chromium runs headless | `true` |
| `BROWSER_TIMEOUT` | Page load timeout in seconds | `30` |
| `SERVER_HOST` | Bind host | `0.0.0.0` |
| `SERVER_PORT` | Bind port | `8000` |

---

## 🚀 Deployment

- [Render deployment](https://shenhao-stu.github.io/ohmycaptcha/deployment/render/)
- [Hugging Face Spaces deployment](https://shenhao-stu.github.io/ohmycaptcha/deployment/huggingface/)
- [Full documentation](https://shenhao-stu.github.io/ohmycaptcha/)

---

## 🧩 Skills

This repository includes reusable local skills under `skills/`:

- `skills/ohmycaptcha/` — operate, deploy, validate, and integrate OhMyCaptcha
- `skills/ohmycaptcha-image/` — generate public-safe README and docs visuals

They are designed for Claude Code, OpenCode, OpenClaw-style workflows, and similar agent environments.

---

## ✅ Acceptance Status

This repository has been validated locally against the public reCAPTCHA v3 detector target at:

- `https://antcpt.com/score_detector/`
- site key: `6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf`

The verified result for this codebase is that the service can successfully:

- start the API service
- create a detector task
- poll until `ready`
- return a non-empty `solution.gRecaptchaResponse`

The implementation does **not** claim guaranteed score targeting or full compatibility with all commercial captcha service features.

---

## ⚠️ Limitations

- Tasks are stored **in memory** and expire after the configured TTL
- `minScore` exists in the schema for compatibility, but the current solver does **not** enforce score targeting
- `ImageToTextTask` currently returns structured output serialized into `solution.text`
- Reliability depends on browser environment, target-site behavior, IP reputation, and model or provider quality

---

## 🔧 Development

```bash
pytest tests/
npx pyright
python -m mkdocs build --strict
```

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=shenhao-stu/ohmycaptcha&type=Date)](https://www.star-history.com/#shenhao-stu/ohmycaptcha&Date)

---

## 📄 License

[MIT](LICENSE) — use freely, modify openly, deploy carefully.
