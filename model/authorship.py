from dataclasses import dataclass

from model.artist import Artist


@dataclass
class Authorship:
    object_id: int
    role: str
    artist: Artist

    def __str__(self):
        return f"{self.object_id} {self.role} {self.artist}"

    def __repr__(self):
        return f"{self.object_id} {self.role} {self.artist}"
