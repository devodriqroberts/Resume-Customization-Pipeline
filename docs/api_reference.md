# API Reference

This document provides an overview of how the Automated Resume Tailoring Tool interacts with the OpenAI API, including endpoint usage, request/response structure, and rate limits.

## Overview

The tool uses the OpenAI API to tailor LaTeX resumes based on job descriptions. It sends a prompt containing the base LaTeX resume and the job description to the API and receives a response containing tailored resume content.

## API Endpoint

- **Endpoint**: `https://api.openai.com/v1/chat/completions`
- **Method**: `POST`
- **Headers**:
  - `Authorization`: Bearer token using your OpenAI API key.
  - `Content-Type`: `application/json`.

## Authentication

All requests to the OpenAI API require an API key. Make sure to set the `OPENAI_API_KEY` in your `.env` file:

```

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

This key is passed in the `Authorization` header for every API request.

Example of `Authorization` header:

```

Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

## Request Structure

Here is the general structure of the API request used to tailor the resume:

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "<SYSTEM_ROLE>"
    },
    {
      "role": "user",
      "content": "<PROMPT>"
    }
  ]
}
```

### Parameters

- **`model`**: The model used to generate the response. In this case, `gpt-4o-mini` is specified for optimal performance.
- **`messages`**: A list of messages forming the context for the API to generate a response.
  - **`role`**: The role for the message. Can be `"system"`, `"user"`, or `"assistant"`.
    - `"system"`: Sets the context or persona of the assistant.
    - `"user"`: Contains the prompt provided by the user (i.e., base resume and job description).
  - **`content`**: The content of the message.
    - **`<SYSTEM_ROLE>`**: The role or context for the assistant, provided by the `SYSTEM_ROLE` variable in `.env`.
    - **`<PROMPT>`**: The actual prompt to tailor the resume, consisting of the base LaTeX resume and job description text.

### Example Request Body

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Assistant for resume tailoring"
    },
    {
      "role": "user",
      "content": "Resume (LaTeX):\n<Resume Content Here>\n\nJob Description(s):\n<Job Description Content Here>\n\n"
    }
  ]
}
```

## Response Structure

The response from the API contains the tailored content for the resume. Here's a basic structure of the response:

```json
{
  "id": "<response_id>",
  "object": "chat.completion",
  "created": 1234567890,
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "<Tailored Resume LaTeX Content>"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 256,
    "completion_tokens": 128,
    "total_tokens": 384
  }
}
```

### Parameters

- **`choices[0].message.content`**: The tailored resume LaTeX content provided by the API.
- **`usage`**: Information about token usage for the request, which may be important for monitoring API costs and limits.

### Example Response Content

```latex
\documentclass{article}
\begin{document}
% Tailored resume content based on job description
\end{document}
```

## Rate Limits & Usage Monitoring

Your OpenAI account may have rate limits on the number of API requests you can make within a specific time period. These limits depend on your account type and subscription plan.

To monitor your usage and rate limits:

1. Log into the [OpenAI Dashboard](https://platform.openai.com/account/usage).
2. Check the "API Usage" section to see the number of tokens used and remaining limits.

## Error Handling

If an error occurs during the API request, the tool will raise an exception or print an error message. Common issues include:

- **Invalid API Key**: Ensure the `OPENAI_API_KEY` is correctly set in your `.env` file.
- **Rate Limit Exceeded**: You may need to wait before making additional requests or upgrade your account for higher limits.
- **Malformed Request**: Double-check that all required parameters are correctly formatted and included in the request body.

## Best Practices for API Usage

- **Optimize Prompt Length**: Keep the LaTeX resume and job description content concise to avoid exceeding token limits.
- **Monitor Usage**: Regularly check your token usage to stay within your rate limits.
- **Cache Results**: If you expect to use the same tailored content multiple times, store the output locally to avoid repeated API calls.
