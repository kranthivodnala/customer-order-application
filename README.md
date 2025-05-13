# Simple Customer Order Application

Frontend hosted on S3, backend using Lambda, API Gateway, SQS, and SNS.

## How it works

- User selects an item and submits the form.
- Request is sent to API Gateway.
- Lambda adds the order to SQS and sends an SNS email.

## Tech Stack

- HTML/CSS (Frontend)
- Lambda (Backend)
- SQS (Queue)
- SNS (Notifications)
- S3 (Frontend Hosting)
- API Gateway (API endpoint)

## Deploy in 15 Minutes

1. Deploy HTML to S3.
2. Create SQS queue and SNS topic.
3. Deploy Lambda with env vars.
4. Create and link API Gateway to Lambda.
5. Done ✅
