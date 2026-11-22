
import pytest

from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness

from settings import Settings


def test_ragas_installation():
    print("Ragas import successful")
    assert True


@pytest.mark.asyncio
async def test_ragas_evaluation():

    # Step 1: User question
    question = "What is the refund policy?"

    # Step 2: Retrieved RAG documents
    retrieved_contexts = [
        "Customer can request a refund within 30 days of purchase.",
        "Refunds are processed to the original payment method.",
        "Standard delivery usually takes 5 to 7 business days."
    ]

    # Step 3: Actual LLM answer
    actual_answer = (
        "Customer can request a refund within 30 days "
        "of purchase. The refund is processed to the "
        "original payment method."
    )

    # Step 4: Connect to LLM
    client = AsyncOpenAI(
        api_key=Settings.API_KEY,
        base_url=Settings.LLM_API_URL
    )

    # Step 5: Create evaluator LLM
    evaluator_llm = llm_factory(
        model=Settings.MODEL,
        provider="openai",
        client=client,
        temperature=0
    )

    # Step 6: Create Faithfulness metric
    faithfulness = Faithfulness(
        llm=evaluator_llm
    )

    # Step 7: Evaluate answer against retrieved context
    result = await faithfulness.ascore(
        user_input=question,
        response=actual_answer,
        retrieved_contexts=retrieved_contexts
    )

    # Step 8: Display result
    print("Faithfulness Score:", result.value)

    assert 0 <= result.value <= 1

    await client.close()
