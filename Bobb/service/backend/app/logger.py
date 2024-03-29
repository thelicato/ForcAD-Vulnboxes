from datetime import datetime

# Colors
SUCCESS_COLOR = "\033[92m"
ERROR_COLOR = "\033[91m"
DEBUG_COLOR = "\033[93m"
BOLD_FORMAT = "\033[1m"
END_FORMAT = "\033[0m"


class Logger:
    silent_mode: bool = False
    debug_mode: bool = False

    """Implement it as a Singleton"""

    def __new__(cls) -> "Logger":
        if not hasattr(cls, "instance"):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def init(self, silent_mode: bool, debug_mode: bool) -> None:
        self.silent_mode = silent_mode
        self.debug_mode = debug_mode

    def log(self, msg: str, end: str | None = None) -> None:
        if not self.silent_mode and self.debug_mode:
            print(msg, flush=True, end=end)

    def bold(self, msg: str, end: str | None = None) -> None:
        if not self.silent_mode:
            print(f"{BOLD_FORMAT}{msg}{END_FORMAT}", flush=True, end=end)

    def info(self, msg: str, end: str | None = None) -> None:
        if not self.silent_mode:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}] - [INFO] - {msg}", flush=True, end=end)

    def success(self, msg: str, end: str | None = None) -> None:
        if not self.silent_mode:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(
                f"{SUCCESS_COLOR}[{current_time}] - [SUCC] - {msg}{END_FORMAT}",
                flush=True,
                end=end,
            )

    def error(self, msg: str, end: str | None = None) -> None:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(
            f"{ERROR_COLOR}[{current_time}] - [ERRO] - {msg}{END_FORMAT}",
            flush=True,
            end=end,
        )

    def debug(self, msg: str, end: str | None = None) -> None:
        if not self.silent_mode and self.debug_mode:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(
                f"{DEBUG_COLOR}[{current_time}] - [DEBU] - {msg}{END_FORMAT}",
                flush=True,
                end=end,
            )


def init(silent_mode: bool, debug_mode: bool) -> None:
    Logger().init(silent_mode, debug_mode)


log = Logger().log
bold = Logger().bold
info = Logger().info
success = Logger().success
error = Logger().error
debug = Logger().debug
