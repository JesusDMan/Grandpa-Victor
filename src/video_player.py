import cv2
from time import sleep, time
from ffpyplayer.player import MediaPlayer
from threading import Thread


class VideoPlayer(object):
    def __init__(self, name: str, video_path):
        self.name = name
        self._cap = cv2.VideoCapture(video_path)
        self._running = False
        self.__window_name__ = 'video'
        self.video_path = video_path
        self.fps = self._cap.get(cv2.CAP_PROP_FPS)

    def stop_video(self):
        
        self._running = False

    def play_video(self):
        self._running = True
        t = Thread(target=self._play_video, args=())
        t.start()

    def _play_video(self):
        self._player = MediaPlayer(self.video_path)
        self._cap = cv2.VideoCapture(self.video_path)

        sleep_seconds = 1 / self.fps
        cv2.namedWindow(self.__window_name__, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(self.__window_name__, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while True:
            if not self._running:
                break

            start = time()
            grabbed, frame = self._cap.read()
            audio_frame, val = self._player.get_frame()

            if not grabbed:
                print("End of video")
                self._running = False
                break
            cv2.imshow(self.__window_name__, frame)
            cv2.waitKey(1)

            if val == 'eof':
                break

            # Wait to preserve correct fps
            diff = time() - start
            if diff < sleep_seconds:
                sleep(sleep_seconds - diff)

        self._cap.release()
        self._player.close_player()
        cv2.destroyAllWindows()
