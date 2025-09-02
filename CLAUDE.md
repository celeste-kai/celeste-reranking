# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This is the **celeste-reranking** package, part of the larger Celeste multi-modal AI framework. It provides unified reranking capabilities across multiple providers, currently supporting Cohere with plans for local models.

## Architecture

### Package Structure
```
celeste-reranking/
├── src/celeste_reranking/
│   ├── __init__.py              # Main factory function create_reranker()
│   ├── mapping.py               # Provider-to-implementation mapping
│   ├── core/                    # Domain-specific types and enums (empty currently)
│   └── providers/
│       ├── __init__.py
│       └── cohere.py           # CohereReranker implementation
├── example.py                   # Streamlit demo application
├── pyproject.toml              # Package configuration with celeste-core dependency
└── README.md                   # Package documentation
```

### Core Concepts
- **BaseReranker**: Abstract base class from `celeste_core.base.reranker`
- **AIResponse**: Standard response format with content and metadata
- **Provider Mapping**: Links providers to implementation classes via `PROVIDER_MAPPING` dict
- **Factory Pattern**: `create_reranker()` function instantiates appropriate provider class

### Dependencies
- `celeste-core`: Foundation package providing base classes, enums, and validation
- `cohere>=5.10.0`: Cohere API client for reranking functionality
- `httpx>=0.27.0`: HTTP client for API communication

## Development Commands

### Setup
Run from the parent Celeste directory:
```bash
make dev-sync          # Install all packages in editable mode including celeste-reranking
```

### Testing and Quality
```bash
make lint              # Run Ruff linting
make format            # Apply Ruff formatting  
make typecheck         # Run mypy type checking
make test              # Run pytest (currently no tests in this package)
```

### Running the Demo
```bash
uv run python example.py    # Start Streamlit demo application
```

## Implementation Patterns

### Provider Implementation
1. Inherit from `BaseReranker` in `celeste_core.base.reranker`
2. Implement async `rerank()` method returning `AIResponse[List[str]]`
3. Handle provider authentication via `celeste_core.config.settings`
4. Include scores and original indices in response metadata

### Adding New Providers
1. Create provider class in `providers/` directory
2. Add entry to `PROVIDER_MAPPING` in `mapping.py`
3. Ensure corresponding models exist in `celeste-core` model catalog

### Response Format
- `content`: List of reranked texts (most relevant first)
- `metadata`: Dict containing `scores`, `original_indices`, and `model` info
- `provider`: Provider enum indicating which service was used

## API Configuration

### Environment Variables
- `COHERE_API_KEY`: Required for Cohere reranking functionality

### Models Supported
- `rerank-multilingual-v3.0`: Latest multilingual model (default recommended)
- `rerank-english-v3.0`: Latest English-only model  
- `rerank-multilingual-v2.0`: Legacy multilingual model
- `rerank-english-v2.0`: Legacy English-only model

## Key Files

- `src/celeste_reranking/__init__.py:17`: Main `create_reranker()` factory function
- `src/celeste_reranking/providers/cohere.py:29`: Core `rerank()` implementation
- `mapping.py:6`: Provider-to-class mapping configuration
- `example.py`: Full Streamlit application demonstrating usage