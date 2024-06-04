def Speed_Slow(speed):
    if 0 <= speed <= 25:
        slow = 1
    elif 25 < speed < 75:
        slow = -0.02 * speed + 1.5
    elif 75 <= speed <= 110:
        slow = 0
    return slow

def Speed_Fast(speed):
    if 0 <= speed <= 25:
        fast = 1
    elif 25 < speed < 75:
        fast = 0.02 * speed - 0.5
    elif 75 <= speed <= 110:
        fast = 1
    return fast

def Speed_Slow_From_Y(y):
    if 0 <= y <= 1.5:
        speed = (1.5 - y) / 0.02
        if 25 < speed < 75:
            return speed
    return None  # Returns None if y is outside the valid range

def Speed_Fast_From_Y(y):
    if -0.5 <= y <= 1:
        speed = (y + 0.5) / 0.02
        if 25 < speed < 75:
            return speed
    return None  # Returns None if y is outside the valid range






