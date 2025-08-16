"""OpenAI-compatible LLM provider implementation.

This module provides an OpenAI-compatible implementation of the LLM client
that can work with OpenAI API or any compatible service.
"""

import logging
import os
from typing import Any

import httpx

from .base import LLMClient, LLMProviderError

logger = logging.getLogger(__name__)

# Constants
API_REQUEST_TIMEOUT = 120.0
DEFAULT_BASE_URL = "https://api.openai.com/v1"


class OpenAICompatibleClient(LLMClient):
    """Handles communication with OpenAI-compatible APIs."""

    def __init__(self, api_key: str, base_url: str | None = None):
        self.api_key = api_key
        self.base_url = base_url or DEFAULT_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    async def chat_completion(
        self,
        messages: list[dict[str, Any]],
        model: str,
        max_tokens: int,
        temperature: float,
        tools: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """Send a chat completion request to OpenAI-compatible API."""
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        if tools:
            payload["tools"] = tools

        endpoint_url = f"{self.base_url.rstrip('/')}/chat/completions"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint_url,
                headers=self.headers,
                json=payload,
                timeout=API_REQUEST_TIMEOUT,
            )

            if response.status_code != 200:
                error_msg = f"API error: {response.status_code} - {response.text}"
                logger.error(f"❌ {error_msg}")
                raise LLMProviderError(error_msg)

            response_data = response.json()
            return response_data
