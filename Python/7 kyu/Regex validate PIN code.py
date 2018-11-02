def validate_pin(pin):
    try:
        if int(pin) < 0 or len(pin) not in [4, 6]:
            return False
        return True
    except:
        return False
