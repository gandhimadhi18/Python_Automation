import json
class LLMResponseValidator:
    def validate_not_empty(self,answer):
        assert answer is not None
        assert isinstance(answer,str)
        assert len(answer.strip()) > 0
    def validate_minimum_length(self, answer):
        assert len(answer.strip()) >= 10

#     def validate_json_response(self, answer):
#         try:
#             json.loads(answer)
#         except json.JSONDecodeError:
#             raise AssertionError("Invalid json response")
#         def validate_expected_keyword(self, answer, keyword):
#             assert keyword.lower() in answer.lower(),(
#             f"Expected keyword '{keyword}' not found"
# )