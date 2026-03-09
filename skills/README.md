# OhMyCaptcha Skills

This repository includes a reusable skill for agent-driven environments such as Claude Code and similar tool-using assistants.

## Included skill

- `skills/ohmycaptcha/` — operational guidance for deploying, configuring, validating, and integrating OhMyCaptcha

## Installation idea

For human users or agent-driven setup flows, point the assistant at this repository and ask it to install or copy the skill from:

- `skills/ohmycaptcha/`

Example prompt for an LLM agent:

```text
Install the OhMyCaptcha skill from this repository and make it available in my local skills directory. Then show me how to use it for deploying or integrating the service.
```

## Notes

- The skill is documentation-backed and uses only placeholder credentials.
- It is intended to make OhMyCaptcha easier to operate from agent environments.
