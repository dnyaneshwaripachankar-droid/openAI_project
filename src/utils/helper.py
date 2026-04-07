import datetime
import re

def print_banner():
    """
    Prints a simple project banner
    """
    print("=== OpenEnv Hackathon Project ===")


def format_timestamp():
    """
    Returns current timestamp as string
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def clean_string(text):
    """
    Cleans a string by removing extra spaces
    """
    return text.strip()


def slugify_text(text):
    """
    Converts text into URL-friendly format
    Example: 'Hello World' → 'hello-world'
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text