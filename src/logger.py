class Logger:
    """Responsable for print in console and save the logs
    """
    def __init__(self) -> None:
        self._logs = []

    def log(self, *args):
        """add a new log
        """
        self._logs.append(str(*args))
        print(*args)

    def get_all_logs(self) -> list[str]:
        """returns a copy of all the logs until now

        Returns:
            list[str]: logs
        """
        return self._logs.copy()

    def clean(self) -> None:
        """clean all the logs saved
        """
        self._logs.clear()


logger = Logger()
