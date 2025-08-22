<div align="center">

# 🎯 Celeste Reranking

### One Interface, All Reranking Providers - Unified API for Text Reranking

[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Providers](https://img.shields.io/badge/Providers-1_Implemented-orange?style=for-the-badge&logo=cohere&logoColor=white)](#-supported-providers)
[![Models](https://img.shields.io/badge/Rerank_Models-4+-purple?style=for-the-badge&logo=tensorflow&logoColor=white)](#-supported-models)

[![Documentation](https://img.shields.io/badge/📚_Docs-Coming_Soon-blue?style=for-the-badge)](#)

</div>

---

## 🎯 Why Celeste Reranking?

<div align="center">
  <table>
    <tr>
      <td align="center">🔀<br><b>Smart Reranking</b><br>Reorder texts by relevance to query</td>
      <td align="center">🔌<br><b>Unified API</b><br>One interface for all reranking providers</td>
      <td align="center">⚡<br><b>Async First</b><br>Built for performance</td>
      <td align="center">📊<br><b>Score Output</b><br>Relevance scores in metadata</td>
    </tr>
  </table>
</div>

## 🚀 Quick Start

```python
# Install (part of Celeste ecosystem)
from celeste_reranking import create_reranker

# Create a reranker
reranker = create_reranker("cohere", model="rerank-multilingual-v3.0")

# Rerank texts by relevance to query
query = "What are the benefits of exercise?"
texts = [
    "Exercise improves cardiovascular health and reduces disease risk.",
    "The weather is nice today with sunny skies.",
    "Regular physical activity boosts mental health and mood.",
    "Cooking pasta requires boiling water and adding salt."
]

# Get reranked results
response = await reranker.rerank(query, texts, top_k=2)

# Access reranked texts (most relevant first)
reranked_texts = response.content
# ['Exercise improves cardiovascular health...', 'Regular physical activity boosts...']

# Access relevance scores
scores = response.metadata["scores"]  # [0.92, 0.84]
```

## 📦 Installation

<details open>
<summary><b>Part of Celeste Ecosystem</b></summary>

```bash
# Install as part of Celeste development environment
cd celeste
make dev-sync  # Installs all Celeste domains including reranking
```
</details>

## 🔧 Configuration

### Add your API keys to `.env`

<details>
<summary><b>🔑 Required API Keys</b></summary>

| Provider | Environment Variable | Get API Key |
|----------|---------------------|-------------|
| 🎯 **Cohere** | `COHERE_API_KEY` | [Cohere Dashboard](https://dashboard.cohere.ai/api-keys) |

</details>

## 🎨 Supported Providers

<div align="center">

| Provider | Status | Models | Multilingual | Free Tier |
|----------|--------|--------|-------------|------------|
| 🎯 **Cohere** | ✅ Implemented | 4 | ✅ | ✅ (Trial) |
| 🤗 **Local Models** | 🛠️ Planned | - | ✅ | ✅ |

</div>

## 📊 Supported Reranking Models

<details>
<summary><b>View All Models</b></summary>

### 🎯 Cohere (Implemented)
- `rerank-multilingual-v3.0` - Latest multilingual model (100+ languages)
- `rerank-english-v3.0` - Latest English-only model
- `rerank-multilingual-v2.0` - Legacy multilingual model
- `rerank-english-v2.0` - Legacy English-only model

### 🤗 Local Models (Planned)
- `BAAI/bge-reranker-base` - Base BGE reranker
- `BAAI/bge-reranker-large` - Large BGE reranker
- `BAAI/bge-reranker-v2-m3` - Multilingual BGE v2
- `cross-encoder/ms-marco-MiniLM-L-6-v2` - MS MARCO MiniLM
- `cross-encoder/ms-marco-electra-base` - MS MARCO Electra

</details>

## 🎮 Use Cases

- **🔍 Search Enhancement** - Improve search result relevance
- **📄 RAG Systems** - Rerank retrieved documents for better context
- **💡 Content Recommendation** - Order content by user query relevance  
- **📊 A/B Testing** - Compare different ranking approaches
- **🎯 Semantic Matching** - Find most relevant content for queries

## 🗺️ Roadmap

### Celeste-Reranking Next Steps
- [x] 📝 **Core Types** - Clean AIResponse pattern with metadata scores
- [x] 🎯 **Cohere Provider** - Complete implementation with 4 models
- [ ] 🤗 **Local Models** - CrossEncoder support for offline reranking
- [ ] 🧪 **Unit Tests** - Comprehensive test coverage
- [ ] 📚 **Documentation** - API documentation with examples
- [ ] 🎨 **UI Integration** - React components for reranking demos

### Celeste Ecosystem

| Package | Description | Status |
|---------|-------------|--------|
| 🎯 **celeste-reranking** | Text reranking across providers | 🔄 This Package |
| 💬 **celeste-client** | Text generation and chat | ✅ Available |
| 🌟 **celeste-embeddings** | Text embeddings across providers | ✅ Available |
| 🎨 **celeste-image-generation** | Image generation across providers | ✅ Available |
| 🖼️ **celeste-image-edit** | Image editing and manipulation | ✅ Available |
| 🎵 **celeste-audio-intelligence** | Audio processing and analysis | ✅ Available |
| 📄 **celeste-document-intelligence** | Document processing and analysis | ✅ Available |
| 🎥 **celeste-video-generation** | Video generation across providers | ✅ Available |
| 🚀 **And more...** | Expanding ecosystem of AI tools | 🔮 Future |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by the Celeste Team
  
  <a href="#-celeste-reranking">⬆ Back to Top</a>
</div>