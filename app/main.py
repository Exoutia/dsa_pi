from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "This is questions"}


@app.get("/questions")
def get_all_questions():
    return {"message": "All questions"}
