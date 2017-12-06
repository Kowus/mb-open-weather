import pyowm
import serial

KEY = 'ecb475efcaa6bc04fa9a35435dfd25bb'
location = 'Accra,GH'

owm = pyowm.OWM(KEY)
fc = owm.daily_forecast(location)
f = fc.get_forecast()
icons = [weather.get_weather_icon_name() for weather in f]

print(icons)

PORT = '/dev/ttyACM0'
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.readline()

icon = 0

while True:
    s.write(icons[icon].encode('utf-8'))
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split('')
    try:
        a,b = data_list
        if a == 'True':
            icon -= 1
            print(icon%len(icons))
        if b=='True':
            icon+=1
            print(icon%len(icons))
    except:
        pass

s.close()
