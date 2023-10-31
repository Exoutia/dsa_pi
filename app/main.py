from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import database, models, schemas

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Dsa_pi"}


@app.post("/problems", response_model=schemas.Problem)
def create_problem(
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


@app.get("/problems", response_model=List[schemas.Problem])
def get_all_problems(
    db: Session = Depends(database.get_db),
    limit: int = 10,
    skip: int = 0,
    search: str | None = None,
):
    query = db.query(models.Problem)
    if search:
        problems = (
            query.filter(models.Problem.title.contains(search))
            .limit(limit)
            .offset(skip).all()
        )
    else:
        problems = query.limit(limit).offset(skip).all()
    if not problems:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Problem Found"
        )
    return problems


@app.get("/problems/{problem_id}", response_model=schemas.Problem)
def get_problem(problem_id: int, db: Session = Depends(database.get_db)):
    query = db.query(models.Problem).filter(models.Problem.id == problem_id)
    problem = query.first()
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Problem with {problem_id} is not found.",
        )
    return problem


@app.put(
    "/problems/{problem_id}",
    response_model=schemas.ProblemCreate,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_problem(
    problem_id: int,
    update_problem: schemas.ProblemCreate,
    db: Session = Depends(database.get_db),
):
    query = db.query(models.Problem).filter(models.Problem.id == problem_id)
    problem = query.first()
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"problem with {problem_id} is not found.",
        )
    query.update(update_problem.dict(), synchronize_session=False)
    db.commit()
    return update_problem


@app.delete("/problems/{problem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_problem(problem_id: int, db: Session = Depends(database.get_db)):
    query = db.query(models.Problem).filter(models.Problem.id == problem_id)
    if query.first is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The problem with {problem_id} id is not found",
        )
    query.delete(synchronize_session=False)
    db.commit()
    return
