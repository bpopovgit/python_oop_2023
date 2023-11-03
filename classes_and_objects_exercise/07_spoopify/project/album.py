from project.song import Song

class Album:
    def __init__(self, name: str, *songs):
        self.songs = songs
        self.name = name
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}"

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}"
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f"Album: {self.name}"]
        for song in self.songs:
            info.append(f"== {song.get_info()}")
        return '\n'.join(info)

