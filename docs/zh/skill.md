# Agent Skill

OhMyCaptcha 在 `skills/ohmycaptcha/` 下附带了一个可复用的 skill。

## 用途

该 skill 用来帮助 agent 环境更一致地回答 OhMyCaptcha 相关问题，包括：

- 部署
- 环境配置
- YesCaptcha 风格 API 使用
- flow2api 集成
- Render 部署
- Hugging Face Spaces 部署

## Skill 位置

```text
skills/ohmycaptcha/SKILL.md
```

## 安装提示词示例

你可以让 LLM agent 帮你安装或复制该 skill。

```text
Install the OhMyCaptcha skill from this repository and make it available in my local skills directory. Then show me how to use it for deploying or integrating the service.
```

## 设计原则

- 只使用占位符密钥
- 与仓库当前已实现任务类型保持一致
- 明确说明限制
- 在需要时把用户引导回仓库文档
