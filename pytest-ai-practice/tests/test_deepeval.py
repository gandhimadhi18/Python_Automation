import pytest

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import OpenAIModel
from config.settings import Settings

print("Deepeval imports successful")
def test_deepeval_installation():
    print("Deepeval test file is running")
    assert True

def test_chatbot_response():
    question = "What is the refund policy?"
    expected_answer ="Customer can request a refund with in 30 days."
    actual_answer ="Customers are eligible for a refund within 30 days of purchase"

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_answer,
        expected_output=expected_answer
    )

    evaluator_model = OpenAIModel(
        model="openai/gpt-oss-120b",
        api_key=Settings.API_KEY,
        base_url="https://api.groq.com/openai/v1" ,
        temperature=0
    )

    metric = AnswerRelevancyMetric(
        threshold=0.7,
        model=evaluator_model
    )
    assert_test(test_case,[metric])
    metric.measure(test_case)
    print("Evaluation score:", metric.score)
    print("Thresold Value:", metric.threshold)
    print("Evaluation Reason:", metric.reason)
    assert metric.score >=0.7