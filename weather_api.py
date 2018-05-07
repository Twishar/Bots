
import pyowm
import config
owm = pyowm.OWM(config.weather_token)

obs = owm.weather_at_place('Kyiv,UA')
w = obs.get_weather()
print(w)

print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature('celsius'))
