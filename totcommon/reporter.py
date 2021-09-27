import traceback
import sys

class ErrorReporter:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print('There is a problem with ' + self.name)
            print('Please report issues here: ' + self.url +'/issues\n')
            traceback.print_exc()
            sys.stdout.flush()
            exit(1)