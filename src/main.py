from fastapi import FastAPI
from src.model import Model


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
def healthcheck():
    return {"status": "healthy"}


@app.get("/chat")
def chat_controller(query: str):
    model = Model(model_name="gpt-4.1-mini", temperature=0.0)
    response = model.get_completion(query)
    return {"answer": response}
