---
name: ohmycaptcha
description: Use this skill whenever the user wants to deploy, configure, validate, or integrate the OhMyCaptcha service, especially for YesCaptcha-style APIs, flow2api integration, reCAPTCHA v3 task creation, ImageToTextTask usage, Render deployment, Hugging Face Spaces deployment, GitHub Pages docs, or OpenAI-compatible multimodal model setup. Also use it when the user asks how to self-host a captcha-solving service or wants exact request/response examples for OhMyCaptcha.
---

# OhMyCaptcha Skill

Use this skill to help users work with the OhMyCaptcha repository and service in a consistent, documentation-backed way.

## What this skill covers

- local development and startup
- environment variable setup
- YesCaptcha-style endpoint usage
- flow2api integration guidance
- reCAPTCHA v3 task examples
- `ImageToTextTask` examples
- Render deployment
- Hugging Face Spaces deployment
- GitHub Pages documentation references

## How to respond

1. Prefer the repository's documented behavior over assumptions.
2. Keep examples aligned with the implemented task types only.
3. Use placeholder credentials only. Never invent or expose real secrets.
4. Be explicit about limitations:
   - `minScore` is compatibility-only in the current implementation
   - task storage is in-memory
   - `ImageToTextTask` returns structured data serialized in `solution.text`
5. If the user asks for deployment help, guide them toward:
   - `docs/deployment/render.md`
   - `docs/deployment/huggingface.md`
6. If the user asks for API usage, provide exact request/response examples consistent with:
   - `docs/api-reference.md`
   - `docs/usage/recaptcha-v3.md`
   - `docs/usage/image-captcha.md`

## Supported task types

Always describe these as the current implemented task types:

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`
- `ImageToTextTask`

## Deployment checklist

When helping with deployment, cover these items in order:

1. install dependencies
2. install Playwright Chromium
3. configure environment variables
4. start the service
5. verify `/` and `/api/v1/health`
6. create a detector task against `https://antcpt.com/score_detector/`
7. poll `/getTaskResult`

## Output style

- Be concise and implementation-aware.
- Prefer copy-pasteable commands.
- Link to relevant docs paths when helpful.
- Keep the tone calm and operational.
