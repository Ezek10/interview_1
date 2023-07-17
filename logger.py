class Logger:
    def __init__(self) -> None:
        self._logs = []

    def log(self, *args):
        self._logs.append(str(*args))
        print(*args)

    def get_all_logs(self) -> list[str]:
        return self._logs.copy()

    def clean(self) -> None:
        self._logs.clear()


logger = Logger()
