from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from pprint import pprint, PrettyPrinter

from model import *

def parse_datetime(value: str | None) -> datetime | None:
    if value is None:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

class TrelloParser:

    def __init__(self, filename: str):
        self._filename = Path(filename)

    def parse(self) -> Board:
        data = self._load_json()

        board = self._parse_board(data)

        self._parse_lists(board, data)
        self._parse_labels(board, data)
        self._parse_cards(board, data)
        self._parse_checklists(board, data)

        return board

    def _load_json(self) -> dict:
        with self._filename.open("r", encoding="utf-8") as fp:
            return json.load(fp)

    def _parse_board(self, data: dict) -> Board:
        return Board(
            id=data["id"],
            name=data["name"],
            description=data.get("desc", "")
        )

    def _parse_lists(self, board: Board, data: dict):
        for item in data.get("lists", []):
            board.lists.append(
                List(
                    id=item["id"],
                    name=item["name"],
                    closed=item["closed"]
                )
            )

    def _parse_labels(self, board: Board, data: dict):
        for item in data.get("labels", []):
            board.labels.append(
                Label(
                    id=item["id"],
                    name=item["name"],
                    color=item["color"]
                )
            )

    def _parse_cards(self, board: Board, data: dict):
        for item in data.get("cards", []):
            board.cards.append(
                Card(
                    id=item["id"],
                    name=item["name"],
                    description=item.get("desc", ""),
                    closed=item.get("closed", False),
                    due=parse_datetime(item["due"])
                )
            )

    def _parse_checklists(self, board: Board, data: dict):
        for item in data.get("checklists", []):
            chk = Checklist(
                id=item["id"],
                name=item["name"]
            )
            for sitem in item.get("checkItems", []):
                chk.items.append(
                    ChecklistItem(
                        id=sitem["id"],
                        name=sitem["name"],
                        state=sitem["state"]
                    )
                )
            board.checklists.append(chk)


if __name__ == '__main__':
    f = Path(__file__).parent.parent / "test/tests.json"
    x = TrelloParser(str(f.absolute())).parse()
    pprint (x)
