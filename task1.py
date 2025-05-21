import matplotlib.pyplot as plt
import requests
import seaborn as sns
from datetime import datetime


API_KEY = 'f0aba14eb8f5ba6389b4041411ae2e90'
CITY = 'Hyderabad'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()
# Extract relevant data
dates, temps, humidity, wind_speed = [], [], [], []
for entry in data['list']:
    dt =datetime.fromtimestamp(entry["dt"])
    dates.append(dt)
    temps.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speed.append(entry['wind']['speed'])
sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
sns.lineplot(x=dates, y=temps, color='orange')
plt.title(f'Temperature Forecast for {CITY}')
plt.ylabel('Temperature (°C)')


plt.subplot(3, 1, 2)
sns.lineplot(x=dates, y=humidity, color='blue')
plt.title('Humidity Forecast')
plt.ylabel('Humidity (%)')


plt.subplot(3, 1, 3)
sns.lineplot(x=dates, y=wind_speed, color='green')
plt.title('Wind Speed Forecast')
plt.ylabel('Wind Speed (m/s)')
plt.xlabel('Date and Time')

plt.tight_layout()
plt.show()

 
