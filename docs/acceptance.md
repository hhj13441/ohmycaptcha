# Acceptance

## Final business acceptance target

The primary target used for validation is:

- URL: `https://antcpt.com/score_detector/`
- site key: `6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf`

## Acceptance checklist

1. Install dependencies and Playwright Chromium.
2. Start the service locally.
3. Confirm:
   - `GET /`
   - `GET /api/v1/health`
4. Create a `RecaptchaV3TaskProxyless` task against the detector target.
5. Poll `POST /getTaskResult` until `status=ready`.
6. Confirm a non-empty `solution.gRecaptchaResponse` is returned.

## Verified outcome for this repository

A local acceptance run completed successfully with the following observed behavior:

- service startup succeeded
- health endpoint reported all expected task types
- detector task creation succeeded
- polling reached `ready`
- a non-empty token was returned

## What this acceptance means

It means the repository's implemented path can:

- start the service
- execute the asynchronous API flow
- generate a token for the detector target

It does **not** mean:

- guaranteed target score control
- complete parity with commercial captcha-solving platforms
- identical behavior across all environments or IPs
