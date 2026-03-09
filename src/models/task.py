"""YesCaptcha / AntiCaptcha compatible API models."""

from __future__ import annotations

from pydantic import BaseModel, Field


# ── createTask ──────────────────────────────────────────────

class TaskObject(BaseModel):
    type: str
    websiteURL: str | None = None
    websiteKey: str | None = None
    pageAction: str | None = None
    minScore: float | None = None
    # image captcha fields
    body: str | None = None  # base64 image


class CreateTaskRequest(BaseModel):
    clientKey: str
    task: TaskObject


class CreateTaskResponse(BaseModel):
    errorId: int = 0
    taskId: str | None = None
    errorCode: str | None = None
    errorDescription: str | None = None


# ── getTaskResult ───────────────────────────────────────────

class GetTaskResultRequest(BaseModel):
    clientKey: str
    taskId: str


class SolutionObject(BaseModel):
    gRecaptchaResponse: str | None = None
    text: str | None = None


class GetTaskResultResponse(BaseModel):
    errorId: int = 0
    status: str | None = None  # "processing" | "ready"
    solution: SolutionObject | None = None
    errorCode: str | None = None
    errorDescription: str | None = None


# ── getBalance ──────────────────────────────────────────────

class GetBalanceRequest(BaseModel):
    clientKey: str


class GetBalanceResponse(BaseModel):
    errorId: int = 0
    balance: float = 99999.0
