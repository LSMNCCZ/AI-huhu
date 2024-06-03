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






