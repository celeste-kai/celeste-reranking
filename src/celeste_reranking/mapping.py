from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider

CAPABILITY: Capability = Capability.RERANKING

PROVIDER_MAPPING: dict[Provider, tuple[str, str]] = {
    Provider.COHERE: (".providers.cohere", "CohereReranker"),
}

__all__ = ["CAPABILITY", "PROVIDER_MAPPING"]
