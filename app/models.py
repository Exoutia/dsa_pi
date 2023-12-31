from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
strnull = Annotated[str, mapped_column(String, nullable=True)]
required_str = Annotated[str, mapped_column(String, nullable=False)]

class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[intpk]
    title: Mapped[required_str]
    description: Mapped[strnull]
    link: Mapped[strnull]
    solution_link: Mapped[strnull]
    difficulty: Mapped[strnull]
    category: Mapped[strnull]


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[required_str]
    description: Mapped[strnull]
