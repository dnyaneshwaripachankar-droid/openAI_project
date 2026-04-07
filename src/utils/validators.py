def is_valid_email(email):
    return "@" in email

def validate_config(config):
    return isinstance(config, dict)