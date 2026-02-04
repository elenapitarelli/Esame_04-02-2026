from dataclasses import dataclass

@dataclass
class Artist:
    artist_id = int
    name = str


    def __str__(self):
        return f"{self.name} (ID: {self.artist_id})"

    def __repr__(self):
        return f"{self.name} (ID: {self.artist_id})"
