def Temp_Freezing(temp):
    if 0 <= temp < 30:
        freezing = 1
    elif 30 < temp < 50:
        freezing = -0.05 * temp + 2.5
    elif 50 <= temp <= 110 :
        freezing = 0
    return freezing

def Temp_Cool(temp):
    if 0 <= temp <= 30:
        cool = 0
    elif 30 < temp < 50:
        cool = 0.05 * temp - 1.5
    elif temp == 50:
        cool = 1
    elif 50 < temp < 70:
        cool = -0.05 * temp + 3.5
    elif 70 <= temp <= 110:
        cool = 0
    return cool
 
def Temp_Warm(temp):
    if 0<= temp <= 50:
        warm = 0
    elif 50 < temp < 70:
        warm = 0.05 * temp -2.5
    elif temp == 70:
        warm = 1
    elif 70 < temp < 90:
        warm = -0.05 * temp + 4.5
    elif 90 <= temp <= 110:
        warm = 0
    return warm

def Temp_Hot(temp):
    if 0 <= temp <= 70:
        hot = 0
    elif 70 < temp < 90:
        hot = 0.05 * temp - 3.5
    elif 90 <= temp <= 110:
        hot = 1
    return hot

    





