def Weather_Sunny(cover):
    if 0 <= cover <=20:
        sunny = 1
    elif 20 < cover < 40:
        sunny = -0.05 * cover + 2
    elif cover >= 40 and cover <=110:
        sunny = 0
    return sunny

def Weather_PartiallyCloudy(cover):
    if 0 <= cover <= 20 or 80 <= cover <=110:
        cloudy = 0
    elif 20 < cover < 50:
        cloudy = 0.0333 * cover - 0.667
    elif cover == 50:
        cloudy = 1
    elif  50 < cover < 80:
        cloudy = -0.0333 * cover + 2.667
    return cloudy
    
def Weather_Overcast(cover):
    if 0 < cover <= 60:
        overcast = 0
    elif 60 < cover < 80:
        overcast = -0.05 * cover -3
    elif 80 <= cover <= 110:
        overcast = 1
    return overcast









