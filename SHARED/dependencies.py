import chromadb
import psycopg2
import os
from openai import OpenAI
from dotenv import load_dotenv

from SHARED.config import settings


client = chromadb.PersistentClient(settings.chroma_path)

collection = client.get_or_create_collection(
    name= "course_chunks",
    metadata={"hnsw:space": "cosine"}
)

def get_collection():
    return collection



def get_user_db():
   
    url = f"postgresql://{settings.postgresql_user}:{settings.postgresql_password}@{settings.postgresql_host}:{settings.postgresql_port}/{settings.postgresql_name}"
    connection = psycopg2.connect(url)
    try:
        yield connection
        
    finally:
        connection.close() 
        

load_dotenv()


class LLM:

    def __init__(self):

        self.client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url= settings.base_url,
)

        self.model = settings.teacher_model

    def generate(self, prompt):


        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content.strip()

    def generate_from_question(
        self,
        question,
        retrieved_chunks,
        prompt_engineer
    ):
        """
        Build the prompt internally and generate
        the first draft answer.
        """

        prompt = prompt_engineer.build_prompt(
            question,
            retrieved_chunks
        )

        return self.generate(prompt)
# Shared singleton used across the entire project.
llm_client = LLM()


ROUTER_TEMPERATURE = 0.0
TEACHER_TEMPERATURE = 0.2
MEMORY_TEMPERATURE = 0.0