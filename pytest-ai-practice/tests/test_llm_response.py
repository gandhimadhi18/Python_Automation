from urllib import response


class TestLLMResponse:
    def test_llm_response_status(self, llm_client, llm_validator):
        prompt = "Explain what RAG means in simple words"
        response = llm_client.generate_response(prompt)
        assert response["choices"]
        answer = response["choices"][0]["message"]["content"]
        assert  answer is not None
        assert len(answer.strip()) > 0
        print("\n AIGenerated answer:")
        print(answer)

        llm_validator.validate_not_empty(answer)
        llm_validator.validate_minimum_length(answer)

#         def test_llm_response_relevance(
#                 self,llm_client, llm_validator
#         ):
#             response = llm_client.generate_response(
#                 "What is python programming"
#             )
# answer = response["choices"][0]["message"]["content"]
# llm_validator.validate_not_empty(answer)
# llm_validator.validate_expected_keyword(answer, "python"
#                                         )