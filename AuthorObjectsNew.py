from dataclasses import dataclass, field
from typing import List, Iterator

@dataclass
class Author:
    firstName: str = ""
    lastName: str = ""

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"

class Authors:
    def __init__(self):
        self._list: List[Author] = []

    def add(self, author: Author):
        self._list.append(author)

    @property
    def count(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        return ', '.join(str(author) for author in self._list)
    
    def __iter__(self) -> Iterator[Author]:
        return iter(self._list)

@dataclass
class Book:
    title: str = ""
    authors: Authors = field(default_factory=Authors)

    def __str__(self) -> str:
        return f"{self.title} by {self.authors}"