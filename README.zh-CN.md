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
  <strong>面向 <a href="https://github.com/OpenClaw/openclaw">flow2api</a> 与类似集成场景的可自托管 YesCaptcha 风格验证码服务</strong>
  <br/>
  <em>通过熟悉的异步任务 API，快速交付基于浏览器的 reCAPTCHA v3 与多模态图片验证码服务。</em>
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> •
  <a href="#-架构">架构</a> •
  <a href="#-任务类型">任务类型</a> •
  <a href="#-部署">部署</a> •
  <a href="#-skills">Skills</a> •
  <a href="#-开发">开发</a>
</p>

<p align="center">
  <a href="README.md">English README</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/">在线文档</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/zh/deployment/render/">Render 部署指南</a> •
  <a href="https://shenhao-stu.github.io/ohmycaptcha/zh/deployment/huggingface/">Hugging Face Spaces 指南</a> •
  <a href="skills/README.md">Skills</a>
</p>

![OhMyCaptcha Hero](docs/assets/ohmycaptcha-hero.png)

---

## ✨ 这是什么？

**OhMyCaptcha** 是一个可直接部署的自托管验证码解决服务，为本仓库已实现的任务类型提供 **YesCaptcha 风格异步 API**。它面向 **flow2api**、内部路由层，以及其他依赖 `createTask` / `getTaskResult` 语义的系统。

### 你能获得什么

- ⚡ **YesCaptcha 风格异步 API**，包含 `createTask`、`getTaskResult`、`getBalance` 与健康检查接口
- 🌐 **基于浏览器的 reCAPTCHA v3 求解**，底层使用 Playwright + Chromium
- 🧠 **OpenAI-compatible 多模态推理**，用于图片验证码分析
- 🏠 **适合自托管的部署路径**，支持本地、Render 与 Hugging Face Spaces
- 📚 **双语文档站**，通过 GitHub Pages 发布
- 🧩 **可复用的本地 skills**，适用于 Claude Code、OpenCode 与类似 agent 工作流
- 🛡️ **明确的能力边界**，不夸大 vendor parity 或 score 保证

> 更准确地说，OhMyCaptcha 是一个**针对本仓库已实现任务类型的、自托管 YesCaptcha-compatible 服务**，而不是对所有商业打码平台能力的完整对标。

---

## 📦 快速开始

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

### 健康检查

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/v1/health
```

### For LLM Agents

把下面这段话贴给你的 agent 环境：

```text
Install and validate OhMyCaptcha from this repository. Follow the local setup, configure placeholder environment variables, start the service, verify the health endpoints, and show me how to create a reCAPTCHA v3 task and an ImageToTextTask.
```

---

## 🏗 架构

<p align="center">
  <img src="docs/assets/ohmycaptcha-diagram.png" alt="OhMyCaptcha architecture diagram" width="100%">
</p>

### 核心构成

- **FastAPI** 提供 HTTP API
- **Playwright + Chromium** 生成 reCAPTCHA v3 token
- **OpenAI-compatible 多模态接口** 分析图片验证码
- **内存型异步任务管理器** 负责后台执行

---

## 🧠 任务类型

### reCAPTCHA v3

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`

当前这四种任务类型在本仓库中共用同一套浏览器求解路径。

### 图片验证码识别

- `ImageToTextTask`

`ImageToTextTask` 采用受 Argus 启发的多模态识别提示词设计，会先将图片归一化到 1440×900 坐标空间，再把结构化识别结果序列化到 `solution.text` 中返回。

---

## 🔌 API 接口

| 接口 | 作用 |
|------|------|
| `POST /createTask` | 创建异步验证码任务 |
| `POST /getTaskResult` | 轮询任务执行结果 |
| `POST /getBalance` | 返回兼容性的余额响应 |
| `GET /api/v1/health` | 健康状态检查 |

### 创建 reCAPTCHA v3 任务

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

### 轮询任务结果

```bash
curl -X POST http://localhost:8000/getTaskResult \
  -H "Content-Type: application/json" \
  -d '{
    "clientKey": "your-client-key",
    "taskId": "uuid-from-createTask"
  }'
```

### 创建图片验证码任务

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

## ⚙️ 配置项

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `CLIENT_KEY` | 客户端认证密钥，对应 `clientKey` | 未设置 |
| `CAPTCHA_BASE_URL` | OpenAI-compatible API 基地址 | `https://your-openai-compatible-endpoint/v1` |
| `CAPTCHA_API_KEY` | 模型接口密钥 | 未设置 |
| `CAPTCHA_MODEL` | 强文本模型名称 | `gpt-5.4` |
| `CAPTCHA_MULTIMODAL_MODEL` | 多模态模型名称 | `qwen3.5-2b` |
| `CAPTCHA_RETRIES` | 模型或浏览器失败重试次数 | `3` |
| `CAPTCHA_TIMEOUT` | 模型请求超时（秒） | `30` |
| `BROWSER_HEADLESS` | Chromium 是否无头运行 | `true` |
| `BROWSER_TIMEOUT` | 页面加载超时（秒） | `30` |
| `SERVER_HOST` | 监听地址 | `0.0.0.0` |
| `SERVER_PORT` | 监听端口 | `8000` |

---

## 🚀 部署

- [Render 部署](https://shenhao-stu.github.io/ohmycaptcha/zh/deployment/render/)
- [Hugging Face Spaces 部署](https://shenhao-stu.github.io/ohmycaptcha/zh/deployment/huggingface/)
- [完整文档](https://shenhao-stu.github.io/ohmycaptcha/)

---

## 🧩 Skills

本仓库在 `skills/` 目录下附带可复用的本地 skills：

- `skills/ohmycaptcha/` — 用于部署、验证、集成和运维 OhMyCaptcha
- `skills/ohmycaptcha-image/` — 用于生成 README 与文档所需的公开安全图片

适用于 Claude Code、OpenCode、OpenClaw 风格工作流，以及类似的 agent 环境。

---

## ✅ 验收状态

本仓库已经在本地环境下，针对以下公开 reCAPTCHA v3 检测目标完成了验收：

- `https://antcpt.com/score_detector/`
- site key：`6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf`

当前已验证的结果是：

- 服务可以正常启动
- 可以成功创建 detector 任务
- 可以轮询到 `ready`
- 可以返回非空的 `solution.gRecaptchaResponse`

本实现**不宣称**可以保证特定 score，也**不宣称**与商业打码平台所有功能完全一致。

---

## ⚠️ 限制说明

- 任务状态保存在**内存中**，并会在 TTL 到期后清理
- `minScore` 为兼容性字段，当前 solver **不会**依据它做分数控制
- `ImageToTextTask` 当前把结构化结果序列化后放在 `solution.text` 中返回
- 实际稳定性取决于浏览器环境、目标站行为、IP 信誉以及模型或供应商质量

---

## 🔧 开发

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

[MIT](LICENSE) —— 自由使用，开放修改，谨慎部署。
