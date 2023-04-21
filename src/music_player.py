# MUSIC
from os import add_dll_directory, path
from threading import Thread
from vlc import MediaPlayer
from time import time, sleep

add_dll_directory(r'C:\My Apps\VLC')


class MusicPlayer:
    def __init__(self, video_path, log_file):
        self.song = MediaPlayer(video_path)
        self.log_file = log_file
        self.starting_time = time()

    def play(self):
        Thread(target=self._play_song).start()

    def pause(self):
        self.song.stop()

    def reset_song(self):
        self._update_file(0)


    def _play_song(self):
        if not path.isfile(self.log_file):
            self._update_file(0)

        with open(self.log_file) as f:
            time_in_song = int(f.read())

        print(f"Playing song from time {time_in_song}")
        self.song.play()
        self.song.set_time(time_in_song)
        self._keepalive()

    def _keepalive(self):
        while not self.song.is_playing() == 1:
            pass
        while self.song.is_playing() == 1:
            print("Keeping alive")
            self._update_file(self.song.get_time())
            sleep(0.5)

    def _update_file(self, time_in_song):
        with open(self.log_file, 'w') as f:
            f.write(str(time_in_song))


# t = MusicPlayer("sample2.mp3", "temp.txt")
# t.play_from_beginning()
# sleep(3)
# t.pause()
# print('wa!')
