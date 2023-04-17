from image import Image
import ComArduino
from time import time, sleep
from video_player import VideoPlayer

MINIMUM_TIME_BETWEEN_PRESSES = 1
MAXIMUM_TIME_FOR_IMAGE = 5

IMAGE_PRESENTER_PATH = r'C:\Users\Yuval Mantin\OneDrive\Documents\Arduino\Grandpa-Victor\image_presenter.py'

CONFIGURATION = 'image'
if CONFIGURATION == 'image':
    YES_IMAGE = Image(name='Yes', image_path='yes.png', presenter_path=IMAGE_PRESENTER_PATH,
                      max_display_time=MAXIMUM_TIME_FOR_IMAGE)
    NO_IMAGE = Image(name='No', image_path='no.png', presenter_path=IMAGE_PRESENTER_PATH,
                     max_display_time=MAXIMUM_TIME_FOR_IMAGE)
elif CONFIGURATION == 'video':
    YES_VIDEO = VideoPlayer(name='Yes', video_path='sample3.mp4')
    NO_VIDEO = VideoPlayer(name='No', video_path='sample.mp4')
time_from_last_yes = 0
time_from_last_no = 0




def present_image(image: Image):
    NO_IMAGE.close()
    YES_IMAGE.close()

    image.open()


def present(name: str):
    global time_from_last_yes, time_from_last_no
    print(name)

    if name == 'Yes':
        if CONFIGURATION == 'video':
            item = YES_VIDEO
        elif CONFIGURATION == 'image':
            item = YES_IMAGE
    elif name == 'No':
        if CONFIGURATION == 'video':
            item = NO_VIDEO
        elif CONFIGURATION == 'image':
            item = NO_IMAGE

    if (name == 'Yes' and time() - time_from_last_yes < MINIMUM_TIME_BETWEEN_PRESSES) or \
            (name == 'No' and time() - time_from_last_no < MINIMUM_TIME_BETWEEN_PRESSES):
        return

    if CONFIGURATION == 'video':
        open_video(item)
    elif CONFIGURATION == 'image':
        present_image(item)

    if name == 'Yes':
        time_from_last_yes = time()
    if name == 'No':
        time_from_last_no = time()


def open_video(video_player: VideoPlayer):
    print('si!')
    YES_VIDEO.stop_video()
    NO_VIDEO.stop_video()
    sleep(1)
    video_player.play_video()


if __name__ == '__main__':
    ComArduino.wait_for_arduino()

    while True:
        msg = ComArduino.receive_from_arduino()
        print(msg)
        present(msg)
