# OhMyCaptcha

<div class="hero hero--light" markdown>

<div class="hero__copy" markdown>

## ⚡ 面向自托管场景的简洁 YesCaptcha 风格验证码服务

OhMyCaptcha 将 **FastAPI**、**Playwright** 与 **OpenAI-compatible 多模态模型** 组合为一个聚焦、清晰的服务，适用于 **flow2api** 与类似集成场景。

<div class="hero__actions" markdown>

[快速开始](getting-started.md){ .md-button .md-button--primary }
[API 参考](api-reference.md){ .md-button }
[GitHub](https://github.com/shenhao-stu/ohmycaptcha){ .md-button }

</div>

</div>

<div class="hero__visual">
  <img src="assets/ohmycaptcha-diagram.png" alt="OhMyCaptcha 架构图">
</div>

</div>

## ✨ 项目亮点

<div class="grid cards feature-cards" markdown>

-   :material-api: **YesCaptcha 风格 API**

    ---

    为当前仓库已实现的任务类型提供熟悉的异步 `createTask` / `getTaskResult` 语义。

-   :material-google-chrome: **基于浏览器的 reCAPTCHA v3**

    ---

    使用 Playwright + Chromium 为支持的目标生成 token。

-   :material-image-search: **多模态图片识别**

    ---

    将图片验证码分析路由到托管或自托管的 OpenAI-compatible 提供方。

-   :material-cloud-outline: **适合自托管的部署路径**

    ---

    既可本地运行，也可配合 Render 与 Hugging Face Spaces 文档完成部署。

</div>

## 🧠 支持的任务类型

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`
- `ImageToTextTask`

## 🚀 快速入口

<div class="grid cards feature-cards" markdown>

-   :material-rocket-launch-outline: **快速开始**

    ---

    安装依赖、配置环境变量，并在本地启动服务。

    [打开快速开始](getting-started.md)

-   :material-file-document-outline: **API 参考**

    ---

    查看支持的接口、请求格式与兼容性说明。

    [打开 API 参考](api-reference.md)

-   :material-play-box-outline: **验收说明**

    ---

    验证 detector 目标流程，并确认 token 返回行为。

    [打开验收指南](acceptance.md)

-   :material-server-outline: **部署指南**

    ---

    按 Render 或 Hugging Face Spaces 路径部署你的服务实例。

    [打开部署指南](deployment/render.md)

</div>

## 📌 范围说明

OhMyCaptcha 提供的是**针对本仓库已实现任务类型的 YesCaptcha 风格 API**。它**不宣称**与商业打码平台具备完全等价的全部功能，也**不保证**基于 `minScore` 的分数控制能力。
