class NotConfiguredError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"cannot find config {name}")
        self.not_configured_var = name
