# Agent Skill

OhMyCaptcha ships with a reusable skill under `skills/ohmycaptcha/`.

## Purpose

The skill helps agent environments answer OhMyCaptcha-specific questions consistently, including:

- deployment
- environment setup
- YesCaptcha-style API usage
- flow2api integration
- Render deployment
- Hugging Face Spaces deployment

## Skill location

```text
skills/ohmycaptcha/SKILL.md
```

## Example install prompt

You can ask an LLM agent to install or copy the skill for you.

```text
Install the OhMyCaptcha skill from this repository and make it available in my local skills directory. Then show me how to use it for deploying or integrating the service.
```

## Design principles

- uses placeholder credentials only
- stays aligned with the actual implemented task types
- keeps limitations explicit
- points users back to repository docs when needed
