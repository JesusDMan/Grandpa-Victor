from image import Image
from src import ComArduino
from time import time, sleep
from video_player import VideoPlayer
from music_player import MusicPlayer

MINIMUM_TIME_BETWEEN_PRESSES = 1
MAXIMUM_TIME_FOR_IMAGE = 5

IMAGE_PRESENTER_PATH = r'image_presenter.py'
CONFIGURATIONS_FILE_PATH = '../CONFIGURATIONS.txt'

CONFIGURATION = open(CONFIGURATIONS_FILE_PATH, 'r').readlines()[3]
print(CONFIGURATION)

if CONFIGURATION == 'image':
    YES_ITEM = Image(name='Yes', image_path='../media/yes.png', presenter_path=IMAGE_PRESENTER_PATH,
                     max_display_time=MAXIMUM_TIME_FOR_IMAGE)
    NO_ITEM = Image(name='No', image_path='../media/no.png', presenter_path=IMAGE_PRESENTER_PATH,
                    max_display_time=MAXIMUM_TIME_FOR_IMAGE)

elif CONFIGURATION == 'video':
    YES_ITEM = VideoPlayer(name='Yes', video_path='../media/sample3.mp4')
    NO_ITEM = VideoPlayer(name='No', video_path='../media/sample.mp4')

elif CONFIGURATION == 'music':
    MUSIC_PATH = '../media/sample2.mp3'
    YES_ITEM = NO_ITEM = MusicPlayer(MUSIC_PATH, '~music_player_time_stamps')
    YES_ITEM.reset_song()

else:
    print(f'{CONFIGURATION} is not valid.')
    exit(1)

time_from_last_yes = 0
time_from_last_no = 0


def present_image(image: Image):
    NO_ITEM.close()
    YES_ITEM.close()

    image.open()


def present(name: str):
    global time_from_last_yes, time_from_last_no

    if (name == 'Yes' and time() - time_from_last_yes < MINIMUM_TIME_BETWEEN_PRESSES) or \
            (name == 'No' and time() - time_from_last_no < MINIMUM_TIME_BETWEEN_PRESSES):
        return
    print(name)

    if name == 'Yes':
        item = YES_ITEM

    elif name == 'No':
        item = NO_ITEM

    if CONFIGURATION == 'video':
        open_video(item)
    elif CONFIGURATION == 'image':
        present_image(item)

    elif CONFIGURATION == 'music':
        play_music(item)

    if name == 'Yes':
        time_from_last_yes = time()
    if name == 'No':
        time_from_last_no = time()


def open_video(video_player: VideoPlayer):
    YES_ITEM.stop_video()
    NO_ITEM.stop_video()
    sleep(1)
    video_player.play_video()


def play_music(music_player: MusicPlayer):
    if YES_ITEM.song.is_playing() == 1:
        YES_ITEM.pause()
    else:
        YES_ITEM.play()


if __name__ == '__main__':
    ComArduino.wait_for_arduino()

    while True:
        msg = ComArduino.receive_from_arduino()
        # msg = input()
        # msg = 'Yes' if msg == '1' else 'No'

        present(msg)
