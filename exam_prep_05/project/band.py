from typing import List
from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
