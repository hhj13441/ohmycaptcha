# API Reference

## Endpoints

- `POST /createTask`
- `POST /getTaskResult`
- `POST /getBalance`
- `GET /api/v1/health`
- `GET /`

All task endpoints are JSON-based and follow a YesCaptcha-style async task pattern.

## `POST /createTask`

### Request shape

```json
{
  "clientKey": "your-client-key",
  "task": {
    "type": "RecaptchaV3TaskProxyless",
    "websiteURL": "https://antcpt.com/score_detector/",
    "websiteKey": "6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf",
    "pageAction": "homepage"
  }
}
```

### Supported task types

#### reCAPTCHA v3

- `RecaptchaV3TaskProxyless`
- `RecaptchaV3TaskProxylessM1`
- `RecaptchaV3TaskProxylessM1S7`
- `RecaptchaV3TaskProxylessM1S9`

Required fields:

- `websiteURL`
- `websiteKey`
- `pageAction` is recommended and passed through to `grecaptcha.execute()`

#### Image recognition

- `ImageToTextTask`

Required fields:

- `body` — base64-encoded image payload

### Compatibility note on `minScore`

The request model accepts `minScore` for compatibility. The current solver implementation does **not** enforce score targeting based on this field.

### Success response

```json
{
  "errorId": 0,
  "taskId": "uuid-string"
}
```

### Common error responses

```json
{
  "errorId": 1,
  "errorCode": "ERROR_TASK_NOT_SUPPORTED",
  "errorDescription": "Task type 'X' is not supported."
}
```

```json
{
  "errorId": 1,
  "errorCode": "ERROR_TASK_PROPERTY_EMPTY",
  "errorDescription": "websiteURL and websiteKey are required"
}
```

## `POST /getTaskResult`

### Request

```json
{
  "clientKey": "your-client-key",
  "taskId": "uuid-from-createTask"
}
```

### Processing response

```json
{
  "errorId": 0,
  "status": "processing"
}
```

### Ready response for reCAPTCHA v3

```json
{
  "errorId": 0,
  "status": "ready",
  "solution": {
    "gRecaptchaResponse": "token..."
  }
}
```

### Ready response for `ImageToTextTask`

```json
{
  "errorId": 0,
  "status": "ready",
  "solution": {
    "text": "{\"captcha_type\":\"click\", ...}"
  }
}
```

### Not found response

```json
{
  "errorId": 1,
  "errorCode": "ERROR_NO_SUCH_CAPCHA_ID",
  "errorDescription": "Task not found"
}
```

## `POST /getBalance`

### Request

```json
{
  "clientKey": "your-client-key"
}
```

### Response

```json
{
  "errorId": 0,
  "balance": 99999.0
}
```

This balance is currently a static compatibility response.

## `GET /api/v1/health`

Example response:

```json
{
  "status": "ok",
  "supported_task_types": [
    "RecaptchaV3TaskProxyless",
    "RecaptchaV3TaskProxylessM1",
    "RecaptchaV3TaskProxylessM1S7",
    "RecaptchaV3TaskProxylessM1S9",
    "ImageToTextTask"
  ],
  "browser_headless": true,
  "captcha_model": "gpt-5.4",
  "captcha_multimodal_model": "qwen3.5-2b"
}
```

## `GET /`

The root endpoint returns a compact service description and the registered task types at runtime.
