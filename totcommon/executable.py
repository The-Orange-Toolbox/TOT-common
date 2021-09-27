from totcommon.logger import print_header, stdout
from totcommon.updater import check_updates
from totcommon.reporter import ErrorReporter
from totcommon.stopwatch import StopWatch

class TOTExecutable:
    def __init__(self, name, orgname, url, version, build_date):
        self.name = name
        self.orgname = orgname
        self.url = url
        self.version = version
        self.build_date = build_date
        
        print_header(orgname, name, build_date)
        check_updates(name, version, url)

    def __enter__(self):
        self.timer = StopWatch()
        self.error = ErrorReporter(self.name, self.url)

        self.timer.__enter__()
        self.error.__enter__()

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.error.__exit__(exc_type, exc_value, exc_tb)
        self.timer.__exit__(exc_type, exc_value, exc_tb)