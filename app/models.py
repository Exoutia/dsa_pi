from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
strnull = Annotated[str, mapped_column(String, nullable=True)]


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[strnull]
    link: Mapped[strnull]
    solution_link: Mapped[strnull]
    difficulty: Mapped[strnull]
    category: Mapped[strnull]


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[strnull]
