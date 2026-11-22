from urllib import response

from utils import rag_validator


class TestRagValidation:
    def test_rag_answer_exists(
self, rag_client, rag_validator):
        response = rag_client.ask_question(
            "How many annual leave days are available?"
        )
rag_validator.validate_answer_exists(response)
def test_rag_source_exists(
self, rag_client, rag_validator
):

    response = rag_client.ask_question(
        "How many annual leave days are available?"
    )
    rag_validator.validate_source_exists(response)
    def test_rag_answer_grounding(
            self,rag_client, rag_validator
        ):
    response = rag_client.ask_question(
        "How many annual leave days are available?"
        )
rag_validator.validate_answer_grounding(response)
