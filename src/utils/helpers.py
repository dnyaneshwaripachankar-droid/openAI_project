
def format_timestamp():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def slugify_text(text):
    return text.lower().replace(" ", "-")