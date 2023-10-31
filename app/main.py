from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import database, models, schemas

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "This is questions"}


@app.get("/questions", response_model=List[schemas.Problem])
def get_all_questions(db: Session = Depends(database.get_db)):
    return db.query(models.Problem).all()


@app.post("/questions", response_model=schemas.Problem)
def create_question(
    problem: schemas.ProblemCreate, db: Session = Depends(database.get_db)
):
    db_problem = models.Problem(
        title=problem.title,
        description=problem.description,
        link=problem.link,
        solution_link=problem.solution_link,
        difficulty=problem.difficulty,
    )
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem
