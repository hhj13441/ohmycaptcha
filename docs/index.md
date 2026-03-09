# OhMyCaptcha

<div class="hero hero--light" markdown>

<div class="hero__copy" markdown>

## ⚡ Self-hostable captcha solving with a clean YesCaptcha-style API

OhMyCaptcha combines **FastAPI**, **Playwright**, and **OpenAI-compatible multimodal models** into a focused service for **flow2api** and similar integrations.

<div class="hero__actions" markdown>

[Get started](getting-started.md){ .md-button .md-button--primary }
[API reference](api-reference.md){ .md-button }
[GitHub](https://github.com/shenhao-stu/ohmycaptcha){ .md-button }

</div>

</div>

<div class="hero__visual">
  <img src="assets/ohmycaptcha-diagram.png" alt="OhMyCaptcha architecture diagram">
</div>

</div>

## ✨ Highlights

<div class="grid cards feature-cards" markdown>

-   :material-api: **YesCaptcha-style API**

    ---

    Familiar async `createTask` / `getTaskResult` semantics for the task types implemented in this repository.

-   :material-google-chrome: **Browser-based reCAPTCHA v3**

    ---

    Playwright + Chromium power the token-generation path for supported targets.

-   :material-image-search: **Multimodal image recognition**

    ---

    Route image captcha analysis through hosted or self-hosted OpenAI-compatible providers.

-   :material-cloud-outline: **Self-hosted deployment**

    ---

    Run locally or follow the included Render and Hugging Face Spaces deployment guides.

</div>

## 🧠 Supported task types

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`
- `ImageToTextTask`

## 🚀 Quick paths

<div class="grid cards feature-cards" markdown>

-   :material-rocket-launch-outline: **Quick start**

    ---

    Install dependencies, configure environment variables, and launch the service locally.

    [Open quick start](getting-started.md)

-   :material-file-document-outline: **API reference**

    ---

    Review supported endpoints, request formats, and compatibility notes.

    [Open API reference](api-reference.md)

-   :material-play-box-outline: **Acceptance**

    ---

    Validate detector-target behavior and confirm token generation flow.

    [Open acceptance guide](acceptance.md)

-   :material-server-outline: **Deployment**

    ---

    Follow the Render or Hugging Face Spaces guides for a production-facing instance.

    [Open deployment guide](deployment/render.md)

</div>

## 📌 Scope note

OhMyCaptcha implements a **YesCaptcha-style API surface for the task types available in this repository**. It does **not** claim full feature parity with commercial captcha-solving vendors, and it does **not** guarantee score targeting for `minScore`.
