import pytest

from clients.llm_client import LLMClient
from clients.rag_client import RAGClient

from utils.response_validator import LLMResponseValidator
from utils.rag_validator import RAGResponseValidator

from dotenv import  load_dotenv
load_dotenv()

@pytest.fixture
def llm_client():
    return LLMClient()


@pytest.fixture
def rag_client():
    return RAGClient()


@pytest.fixture
def llm_validator():
    return LLMResponseValidator()


@pytest.fixture
def rag_validator():
    return RAGResponseValidator()
