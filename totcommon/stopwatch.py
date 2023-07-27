from datetime import datetime


class StopWatch:
    def __init__(self):
        pass

    def __enter__(self):
        self.initial_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            return
        elapsed_time = datetime.now() - self.initial_time
        elapsed_secs = elapsed_time.total_seconds()
        print('{:.1f} seconds elapsed'.format(elapsed_secs),
              end="\n", flush=True)
