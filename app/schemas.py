from enum import Enum

from pydantic import BaseModel, HttpUrl


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Problem(BaseModel):
    id: int
    title: str
    description: str | None
    difficulty: Difficulty | None
    link: HttpUrl | None
    solution_link: HttpUrl | None
