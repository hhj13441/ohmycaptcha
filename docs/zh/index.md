<div class="hero" markdown>

# OhMyCaptcha

一个可自托管的验证码解决服务，提供 YesCaptcha 风格 API，底层基于 **FastAPI**、**Playwright** 和 **OpenAI-compatible 多模态模型**。

[快速开始](getting-started.md){ .md-button .md-button--primary }
[查看 GitHub](https://github.com/shenhao-stu/ohmycaptcha){ .md-button }

</div>

<div class="grid cards" markdown>

-   **YesCaptcha 风格 API**

    ---

    为本仓库已实现任务类型提供异步 `createTask` / `getTaskResult` 语义。

-   **基于浏览器的 reCAPTCHA v3**

    ---

    使用 Playwright + Chromium 为支持的目标生成 reCAPTCHA v3 token。

-   **多模态图片推理**

    ---

    使用 OpenAI-compatible 多模态接口进行受 Argus 启发的图片验证码分析。

-   **可自托管部署**

    ---

    支持本地运行，并提供 Render 与 Hugging Face Spaces 部署路径。

</div>

## 支持的任务类型

### reCAPTCHA v3

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`

### 多模态图片任务

- `ImageToTextTask`

## 适用场景

OhMyCaptcha 适合以下需求：

- 自托管 YesCaptcha 风格工作流
- 可控地管理浏览器自动化与模型后端
- 接入托管或自托管 OpenAI-compatible 多模态提供方
- 与 flow2api 等系统集成

## 范围说明

本项目为当前仓库已实现的任务类型提供 YesCaptcha 风格 API，但**不宣称**与商业平台全量功能等价。
