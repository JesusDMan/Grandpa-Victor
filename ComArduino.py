import serial

START_MARKER = b'<'
END_MARKER = b'>'
READY_MSG = 'Arduino is ready!'

SERIAL_PORT = "COM7"
BAUD_RATE = 9600
SERIAL_CONNECTION = serial.Serial(SERIAL_PORT, BAUD_RATE)
print(F'Serial port:{SERIAL_PORT} opened\nBaud rate: {BAUD_RATE}')


def send_to_arduino(message: bytes):
    SERIAL_CONNECTION.write(message)


def receive_from_arduino():
    message = ""
    char = ""  # any value that is not an end- or startMarker

    # wait for the start character
    while char != START_MARKER:
        char = SERIAL_CONNECTION.read()

    # save data until the end marker is found
    while char != END_MARKER:
        if char != START_MARKER:
            message = message + char.decode('UTF-8')
        char = SERIAL_CONNECTION.read()
    return message


def wait_for_arduino():
    message = ""
    while message != READY_MSG:
        message = receive_from_arduino()

    print(f'{message}\n\n\n')


def close_connection():
    SERIAL_CONNECTION.close()
