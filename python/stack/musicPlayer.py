class musicPlayer :
    def __init__(self, songs) :
         self.songs = songs
         self.index = 0
         self.playing = False
    def play(self) :
         self.playing = True
         print(f"▶ Playing: {self.songs[self.index]} " )
    def pause(self) :
         self.playing = False
         print(f"⏸ Paused: {self.songs[self.index]}")
    def next(self) :
         self.index = (self.index + 1) % len(self.songs)
         self.play()
    def previous(self) :
         self.index = (self.index -1) % len(self.songs)
         self.play()
    def status(self):
         song = self.songs[self.index]
         if self.playing:
             print(f"Status : PLAYING -> {song} " )
         else:
             print(f"Status : PAUSED -> {song} " )

if __name__ == "__main__":
    songs = ["Song 1", "Song 2", "Song 3"]
    player = musicPlayer(songs)
    player.status()
    player.play()
    player.status()
    player.next()
    player.status()
    player.pause()
    player.status()
    player.previous()
    player.status()

    player1 = musicPlayer(["Song A", "Song B", "Song C"])
    player1.status()
    player1.play()
    player1.status()
    player1.next()
    player1.status()
    player1.pause()
    player1.status()
    player1.previous()
    player1.status()