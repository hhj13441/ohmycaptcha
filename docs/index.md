<div class="hero" markdown>

# OhMyCaptcha

Self-hostable captcha solving service with a YesCaptcha-style API, built with **FastAPI**, **Playwright**, and **OpenAI-compatible multimodal models**.

[Get started](getting-started.md){ .md-button .md-button--primary }
[View GitHub](https://github.com/shenhao-stu/ohmycaptcha){ .md-button }

</div>

<div class="grid cards" markdown>

-   **YesCaptcha-style API**

    ---

    Async `createTask` / `getTaskResult` semantics for the task types implemented in this repository.

-   **Browser-based reCAPTCHA v3**

    ---

    Uses Playwright + Chromium to generate reCAPTCHA v3 tokens against supported targets.

-   **Multimodal image reasoning**

    ---

    Uses OpenAI-compatible multimodal APIs for Argus-inspired image captcha analysis.

-   **Self-hostable deployment**

    ---

    Works locally and includes deployment paths for Render and Hugging Face Spaces.

</div>

## Supported task types

### reCAPTCHA v3

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`

### Multimodal image task

- `ImageToTextTask`

## Intended use

OhMyCaptcha is designed for users who want:

- a self-hosted alternative for selected YesCaptcha-style workflows
- control over browser automation and model backends
- support for hosted or self-hosted OpenAI-compatible multimodal providers
- integration with systems such as flow2api

## Scope note

This project implements a YesCaptcha-style API surface for the task types available in this repository. It does **not** claim full commercial-vendor feature parity.
