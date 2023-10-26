class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song1 = Music("Godzilla", "Eminem", "test lyrics")
print(song1.print_info())
print(song1.play())