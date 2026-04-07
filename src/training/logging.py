import datetime

def log(message, level="INFO"):
    """
    Simple logging function with timestamp and level.
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] [{level}] {message}")