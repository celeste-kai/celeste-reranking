from typing import Any, List, Union

import cohere
import httpx
from celeste_core import AIResponse, Provider
from celeste_core.base.reranker import BaseReranker
from celeste_core.config.settings import settings


class CohereReranker(BaseReranker):
    """Reranker using Cohere's API."""

    def __init__(self, model: str = "rerank-v3.5", **kwargs: Any) -> None:
        """
        Initialize Cohere reranker.

        Args:
            model: Cohere rerank model to use
            **kwargs: Additional arguments passed to Cohere client
        """
        # Create httpx client with proper SSL verification
        httpx_client = httpx.Client()

        self.client = cohere.ClientV2(
            api_key=settings.cohere.api_key, httpx_client=httpx_client, **kwargs
        )
        self.model = model

    async def rerank(
        self, query: str, texts: Union[str, List[str]], top_k: int = 5, **kwargs: Any
    ) -> AIResponse[List[str]]:
        """
        Rerank texts using Cohere API.

        Args:
            query: Search query
            texts: Text(s) to rerank
            top_k: Maximum number of results to return
            **kwargs: Additional arguments passed to Cohere rerank API

        Returns:
            AIResponse with reranked texts as content and scores in metadata
        """
        if not texts:
            return AIResponse(
                content=[],
                provider=Provider.COHERE,
                metadata={"model": self.model, "scores": [], "original_indices": []},
            )

        # Ensure texts is a list
        if isinstance(texts, str):
            texts = [texts]

        # Cohere uses 'top_n' instead of 'top_k'
        top_n = min(top_k, len(texts))

        # Call Cohere rerank API
        cohere_response = self.client.rerank(
            model=self.model,
            query=query,
            documents=texts,
            top_n=top_n,
            **kwargs,
        )

        # Extract results
        reranked_texts = []
        scores = []
        original_indices = []

        for result in cohere_response.results:
            reranked_texts.append(texts[result.index])
            scores.append(result.relevance_score)
            original_indices.append(result.index)

        return AIResponse(
            content=reranked_texts,
            provider=Provider.COHERE,
            metadata={
                "model": self.model,
                "scores": scores,
                "original_indices": original_indices,
            },
        )
