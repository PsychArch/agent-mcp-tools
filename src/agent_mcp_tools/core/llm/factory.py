"""Factory for creating LLM clients.

This module provides a factory for creating LLM clients based on configuration.
"""

import os

from .base import LLMClient, LLMProviderError
from .openrouter import OpenAICompatibleClient


class LLMClientFactory:
    """Factory for creating LLM clients based on configuration or environment."""

    @staticmethod
    def create_openai_client(
        api_key: str | None = None, 
        base_url: str | None = None
    ) -> LLMClient:
        """Create an OpenAI-compatible client.

        Args:
            api_key: API key. If not provided, will try to get from OPENAI_API_KEY environment variable.
            base_url: Base URL for the API. If not provided, will try to get from OPENAI_BASE_URL environment variable.

        Returns:
            OpenAI-compatible LLM client

        Raises:
            LLMProviderError: If API key is not provided or found in environment
        """
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")

        if base_url is None:
            base_url = os.environ.get("OPENAI_BASE_URL")

        if not api_key:
            raise LLMProviderError("API key not provided and OPENAI_API_KEY environment variable not set")

        return OpenAICompatibleClient(api_key, base_url)

    @staticmethod
    def create_default_client(api_key: str | None = None) -> LLMClient:
        """Create the default LLM client (currently OpenAI-compatible).

        Args:
            api_key: API key for the provider

        Returns:
            Default LLM client
        """
        return LLMClientFactory.create_openai_client(api_key)
