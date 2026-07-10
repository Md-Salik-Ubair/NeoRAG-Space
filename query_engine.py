import os
import sys
from dotenv import load_dotenv
from groq import Groq

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.embedder import TextEmbedder
from src.vector_store import LocalVectorStore

load_dotenv()


class LocalRAGQueryEngine:

    def __init__(self):

        print("Initializing NeoRAG Query Engine...")

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.3-70b-versatile"

        self.embedder = TextEmbedder()

        self.vector_db = LocalVectorStore(
            storage_file="./vault_manager/vector_index.bin"
        )

        if not self.vector_db.load_index():

            raise RuntimeError(
                "Vector database could not be loaded."
            )

        print("Knowledge Base Loaded Successfully.")

    def execute_inference(self, user_question):

        query_vector = self.embedder.model.encode(
            user_question
        ).tolist()

        retrieved_nodes = self.vector_db.query_similarity(
            query_vector,
            top_k=3
        )

        if not retrieved_nodes:

            return "No relevant knowledge was found."

        context = "\n\n".join(
            node["text"] for node in retrieved_nodes
        )

        system_prompt = f"""
You are NeoRAG Space.

You are a Retrieval Augmented Generation assistant.

Rules:

1.
Answer using the retrieved knowledge.

2.
If the retrieved context is insufficient,
say so clearly.

3.
Do not hallucinate.

4.
Keep answers professional.

=======================

Knowledge Base

{context}

=======================
"""

        try:

            completion = self.client.chat.completions.create(

                model=self.model,

                temperature=0.3,

                messages=[

                    {
                        "role": "system",
                        "content": system_prompt
                    },

                    {
                        "role": "user",
                        "content": user_question
                    }

                ]

            )

            return completion.choices[0].message.content.strip()

        except Exception as e:

            return f"Groq Error : {str(e)}"


if __name__ == "__main__":

    engine = LocalRAGQueryEngine()

    print()

    print("NeoRAG Interactive Console")

    print("Type exit to quit.")

    print()

    while True:

        question = input("Query : ")

        if question.lower() in ["exit", "quit"]:

            break

        if not question.strip():

            continue

        print()

        answer = engine.execute_inference(question)

        print(answer)

        print()

        print("-" * 80)