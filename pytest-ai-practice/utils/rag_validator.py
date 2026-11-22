class RAGResponseValidator:
    def validate_answer_exists(self,response):
        assert "answer" in response

        assert response["answer"] is not None
        assert len(response["answer"].strip()) > 0

        def validate_context_exists(self, response):
            assert "context" in response
            assert response["context"] is not None
            assert len(response["context"]) > 0

            def validate_source_exists(self, response):
                assert "sources" in response
                assert len(response["sources"]) > 0

            def validate_answer_grounding(self, response):
                answer = response["answer"].lower()

            context = " ".join(
                    response["context"]
            ).lower()
            important_words = [
                word for word in answer.split()
                if len(word) > 5
            ]
            assert  any(
                    word in context for word in imporant_words
                ),"Answer may not be supported by retrived context"


