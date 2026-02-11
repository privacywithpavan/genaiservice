import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class Model:
    def __init__(self, model_name: str, temperature: float):
        self.model = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            temperature=temperature,
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [("system", "You are a helpful assistant."), ("human", "{question}")]
        )

        self.parser = StrOutputParser()

        self.chain = self.prompt | self.model | self.parser

    def get_completion(self, query: str) -> str:
        return self.chain.invoke({"question": query})
