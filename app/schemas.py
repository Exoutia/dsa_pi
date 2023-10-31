from enum import Enum

from pydantic import BaseModel, HttpUrl


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class BaseProblem(BaseModel):
    title: str


class Problem(BaseProblem):
    id: int
    title: str
    description: str | None
    difficulty: Difficulty | None
    link: HttpUrl | None
    solution_link: HttpUrl | None


class ProblemCreate(BaseProblem):
    description: str | None = None
    difficulty: Difficulty | None = None
    link: HttpUrl | None = None
    solution_link: HttpUrl | None = None
