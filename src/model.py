from dataclasses import dataclass, field
from datetime import datetime

@dataclass(slots=True)
class Label:
    id: str
    name: str
    color: str

@dataclass(slots=True)
class Member:
    id: str
    full_name: str
    username: str


@dataclass(slots=True)
class Comment:
    id: str
    author: Member | None
    text: str
    created: datetime


@dataclass(slots=True)
class ChecklistItem:
    id: str
    name: str
    state: str

@dataclass(slots=True)
class Checklist:
    id: str
    name: str
    items: list[ChecklistItem] = field(default_factory=list)


@dataclass(slots=True)
class List:
    id: str
    name: str
    closed: bool


@dataclass(slots=True)
class Card:
    id: str
    name: str
    description: str

    closed: bool

    due: datetime | None = None

    labels: list[Label] = field(default_factory=list)
    members: list[Member] = field(default_factory=list)
    comments: list[Comment] = field(default_factory=list)
    checklists: list[Checklist] = field(default_factory=list)

@dataclass(slots=True)
class Board:
    id: str
    name: str
    description: str

    lists: list[List] = field(default_factory=list)
    checklists: list[Checklist] = field(default_factory=list)
    cards: list[Card] = field(default_factory=list)
    members: list[Member] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)