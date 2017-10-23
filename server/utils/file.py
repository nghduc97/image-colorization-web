''' utilities for files '''


def read_text(filepath):
    ''' read all text from a file '''
    with open(filepath, 'r') as file:
        return file.read()
