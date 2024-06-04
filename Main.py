from temperature import Temp_Freezing, Temp_Cool, Temp_Warm, Temp_Hot
from weather import Weather_Sunny, Weather_PartiallyCloudy, Weather_Overcast
import matplotlib.pyplot as plt
import numpy as np

def min(a, b):
    return a if a < b else b

def fuzzy_rule(temperature, cover):
    sunny = Weather_Sunny(cover)
    warm = Temp_Warm(temperature)
    cloudy = Weather_PartiallyCloudy(cover)
    cool = Temp_Cool(temperature)

    R1_Fast = min(sunny, warm)
    y1 = R1_Fast
    R2_Slow = min(cloudy, cool)
    y2 = R2_Slow

    return sunny, warm, cool, cloudy, y1, y2

def SpeedMeasure(y1, y2):
    # Define the speed membership functions for Fast and Slow
    speed_fast_points = [(0, 0), (25, 0), (75, y1), (110, 1)]
    speed_slow_points = [(0, y2), (25, 1), (75, y2), (110, 0)]
    
    # Combine the points for SpeedMeasure
    aggregated_points = speed_fast_points + speed_slow_points
    
    # Calculate the COG
    numerator = sum(x * y for x, y in aggregated_points)
    denominator = sum(y for _, y in aggregated_points)
    
    if denominator == 0:
        return 0
    
    speed = numerator / denominator
    
    return speed


if __name__ == "__main__":
    # Input temperature and cloud cover values
    temperature = float(input("Enter temperature: "))
    cloudCover = float(input("Enter cloud cover: "))

    sunny, warm, cool, cloudy, y1, y2 = fuzzy_rule(temperature, cloudCover)

    print(f'Sunny {sunny:.2f} & Warm {warm:.2f}')
    print(f'Cloudy {cloudy:.2f} & Cool {cool:.2f}')
    print(f'y1 {y1:.2f} & y2 {y2:.2f}')

    # SpeedMeasure to find the speed
    speed = SpeedMeasure(y1, y2)
    print(f'Speed: {speed:.2f} mph')

    temps = np.linspace(0, 110, 500)
    cloud_covers = np.linspace(0, 100, 500)

    # Membership values for temperature
    freezing_values = [Temp_Freezing(temp) for temp in temps]
    cool_values = [Temp_Cool(temp) for temp in temps]
    warm_values = [Temp_Warm(temp) for temp in temps]
    hot_values = [Temp_Hot(temp) for temp in temps]

    # Membership values for weather
    sunny_values = [Weather_Sunny(cover) for cover in cloud_covers]
    partially_cloudy_values = [Weather_PartiallyCloudy(cover) for cover in cloud_covers]
    overcast_values = [Weather_Overcast(cover) for cover in cloud_covers]

    plt.figure(figsize=(12, 5))

    # Plot temperature functions
    plt.subplot(1, 2, 1)
    plt.plot(temps, freezing_values, label='Freezing')
    plt.plot(temps, cool_values, label='Cool')
    plt.plot(temps, warm_values, label='Warm')
    plt.plot(temps, hot_values, label='Hot')

    # Dot points for warm and cool
    plt.scatter([temperature], [warm], color='red', label=f'Warm: {warm:.2f}')
    plt.scatter([temperature], [cool], color='blue', label=f'Cool: {cool:.2f}')

    plt.xlabel('Temperature (°F)')
    plt.ylabel('Membership Value')
    plt.title('Temperature Membership Functions')
    plt.xticks(np.arange(0, 115, 5))
    plt.yticks(np.arange(0, 1.1, 0.2))
    plt.legend()
    plt.grid(True)

    # Plot weather functions
    plt.subplot(1, 2, 2)
    plt.plot(cloud_covers, sunny_values, label='Sunny')
    plt.plot(cloud_covers, partially_cloudy_values, label='Partially Cloudy')
    plt.plot(cloud_covers, overcast_values, label='Overcast')

    # Dot points for sunny and cloudy
    plt.scatter([cloudCover], [sunny], color='orange', label=f'Sunny: {sunny:.2f}')
    plt.scatter([cloudCover], [cloudy], color='gray', label=f'Cloudy: {cloudy:.2f}')

    plt.xlabel('Cloud Cover (%)')
    plt.ylabel('Membership Value')
    plt.title('Weather Membership Functions')
    plt.xticks(np.arange(0, 105, 5))
    plt.yticks(np.arange(0, 1.1, 0.2))
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

