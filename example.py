import asyncio

import streamlit as st
from celeste_core import Provider, list_models
from celeste_core.enums.capability import Capability
from celeste_reranking import create_reranker


async def main() -> None:
    st.set_page_config(page_title="Celeste Reranking", page_icon="🎯", layout="wide")
    st.title("🎯 Celeste Reranking")

    # Get providers that support reranking
    providers = sorted(
        {m.provider for m in list_models(capability=Capability.RERANKING)},
        key=lambda p: p.value,
    )

    with st.sidebar:
        st.header("⚙️ Configuration")
        provider = st.selectbox(
            "Provider:", [p.value for p in providers], format_func=str.title
        )
        models = list_models(
            provider=Provider(provider), capability=Capability.RERANKING
        )
        model_names = [m.display_name or m.id for m in models]
        selected_idx = st.selectbox(
            "Model:", range(len(models)), format_func=lambda i: model_names[i]
        )
        model = models[selected_idx].id

        st.subheader("Options")
        top_k = st.slider("Top K results", 1, 10, 3)

    st.markdown(f"*Powered by {provider.title()}*")

    # Query input
    query = st.text_area(
        "Enter your query:",
        "What are the benefits of exercise?",
        height=80,
        placeholder="Enter your search query...",
    )

    # Texts input
    default_texts = """Exercise improves cardiovascular health and reduces disease risk.
The weather is nice today with sunny skies.
Regular physical activity boosts mental health and mood.
Cooking pasta requires boiling water and adding salt.
Physical exercise helps with weight management and muscle building.
My favorite movie is about space exploration.
Running and swimming are excellent forms of cardio exercise."""

    texts_input = st.text_area(
        "Enter texts to rerank (one per line):",
        default_texts,
        height=150,
        placeholder="Enter texts separated by new lines...",
    )

    if st.button("🎯 Rerank", type="primary", use_container_width=True):
        if not query.strip():
            st.error("Please enter a query.")
            return

        if not texts_input.strip():
            st.error("Please enter texts to rerank.")
            return

        texts = [line.strip() for line in texts_input.split("\n") if line.strip()]

        if len(texts) < 2:
            st.error("Please enter at least 2 texts to rerank.")
            return

        reranker = create_reranker(Provider(provider), model=model)

        with st.spinner("Reranking..."):
            response = await reranker.rerank(query, texts, top_k=top_k)

            st.subheader("🏆 Reranked Results")

            reranked_texts = response.content
            scores = response.metadata.get("scores", [])
            original_indices = response.metadata.get("original_indices", [])

            for i, (text, score, orig_idx) in enumerate(
                zip(reranked_texts, scores, original_indices, strict=False)
            ):
                with st.container():
                    col1, col2, col3 = st.columns([0.8, 0.1, 0.1])

                    with col1:
                        st.markdown(f"**{i+1}.** {text}")

                    with col2:
                        st.metric("Score", f"{score:.3f}")

                    with col3:
                        st.metric("Original #", orig_idx + 1)

                    st.divider()

            # Show metadata
            with st.expander("📊 Response Details", expanded=False):
                metadata_dict = {
                    "provider": response.provider.value if response.provider else None,
                    "model": model,
                    "total_results": len(reranked_texts),
                    "metadata": response.metadata,
                }
                st.json(metadata_dict)

    st.markdown("---")
    st.caption("Built with Streamlit • Powered by Celeste")


if __name__ == "__main__":
    asyncio.run(main())
