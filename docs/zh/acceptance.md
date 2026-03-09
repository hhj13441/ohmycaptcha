# 验收

## 最终业务验收目标

当前主要验收目标为：

- URL：`https://antcpt.com/score_detector/`
- site key：`6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf`

## 验收清单

1. 安装依赖与 Playwright Chromium。
2. 本地启动服务。
3. 确认：
   - `GET /`
   - `GET /api/v1/health`
4. 创建一个 `RecaptchaV3TaskProxyless` 任务。
5. 轮询 `POST /getTaskResult` 直到 `status=ready`。
6. 确认返回非空 `solution.gRecaptchaResponse`。

## 当前仓库的已验证结果

一次本地验收已经成功观察到以下行为：

- 服务启动成功
- 健康检查返回了预期任务类型
- detector 任务创建成功
- 轮询到 `ready`
- 返回了非空 token

## 这份验收的意义

它说明当前仓库实现的路径可以：

- 启动服务
- 跑通异步 API 流程
- 针对 detector 目标生成 token

但它**不代表**：

- 可以保证目标 score
- 与商业打码平台完全等价
- 在所有环境和 IP 下表现一致
