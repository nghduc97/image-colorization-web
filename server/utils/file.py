''' utilities for files '''
import pathlib
import base64


IMAGE_PATH = pathlib.Path('/storage/image_posts')


def read_text(filepath):
    ''' read all text from a file '''
    with open(filepath, 'r') as file:
        return file.read()


def write_bytes(filepath, data):
    with open(filepath, 'wb') as file:
        file.write(data)


def write_base64_image_to_file(name, data):
    i1 = data.find('/')
    i2 = data.find(';')

    ext = data[i1 + 1:i2]
    data = base64.b64decode(data[i2 + 8:])

    path = IMAGE_PATH.joinpath('original', '{}.{}'.format(name, ext))
    write_bytes(path, data)
