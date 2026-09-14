class InvalidConfiguration(Exception):
    """Error Class"""
    def __init__(self, error: str) -> None:
        """Error wrapper function"""
        super().__init__(f"Input Error: {error}")
