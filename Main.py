from temperature import Temp_Freezing, Temp_Cool, Temp_Warm, Temp_Hot
from weather import Weather_Sunny, Weather_PartiallyCloudy, Weather_Overcast
from speed import Speed_Fast, Speed_Slow 

def min(a, b):
    return a if a < b else b

def fuzzy_rule(temperature, cover):
    sunny = Weather_Sunny(cover)
    warm = Temp_Warm(temperature)
    cloudy = Weather_PartiallyCloudy(cover)
    cool = Temp_Cool(temperature)

    #if sunny!=0 and warm != 0:
    R1_Fast = min(sunny, warm)
    y1 = R1_Fast
    #if cloudy != 0 and cool !=0:
    R2_Slow = min(cloudy, cool)
    y2 = R2_Slow

    return sunny, warm, cool, cloudy,y1,y2


if __name__ == "__main__":
    # Input temperature and cloud cover
    temperature = float(input("Enter temperature: "))
    cloudCover = float(input("Enter cloud cover: "))

    sunny, warm, cool, cloudy,y1,y2=fuzzy_rule(temperature, cloudCover)

    print(f'Sunny {sunny:.2f} & Warm {warm:.2f}')
    print(f'Cloudy {cloudy:.2f} & Cool {cool:.2f}')
    print("y1 and y2:",y1,y2)

    

'''if __name__ == "__main__":


    # Input temperature and cloud cover
    temperature = float(input("Enter temperature: "))
    cover = float(input("Enter cloud cover: "))

    # Evaluate speed
    #speed1, speed2, sunny, warm, cloudy, cool = evaluateSpeed(temperature, cloudCover)
    slow, fast = fuzzy_rule(temperature, cover)
    cog_slow, cog_fast = crisp_output(slow, fast)

    print("Center of Gravity (COG) for Slow Speed:", cog_slow)
    print("Center of Gravity (COG) for Fast Speed:", cog_fast)
    # Print the speed
    #print(f"Recommended speed: {speed:.2f} mph")
    #print(f"Sunny & Warm:  {sunny:.2f} & {warm:.2f}")
    #print(f"Cloudy & Cool:  {cloudy:.2f} & {cool:.2f}")
    #print("Sunny and Warm:", speed1)
    #print("Cloudy and Cool:", speed2)'''
