import time
import board
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
DATA_SOURCE = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BCH,ETH,BTC&tsyms=USD"
BCH_LOCATION = ['BCH', 'USD']
ETH_LOCATION = ['ETH', 'USD']
BTC_LOCATION = ['BTC', 'USD']

def text_transform(val):
    return "$%d" % val

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(BCH_LOCATION, ETH_LOCATION, BTC_LOCATION),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/bitcoin_background3.bmp",
                    text_font=cwd+"/fonts/Arial-Bold-24-Complete.bdf",
                    text_position=((150, 55),  # BCH
                                   (150, 130),
                                   (150, 200)), # BTC
                    text_color=(0x00,  # BCH
                                0x00,  # ETH
                                0x00), # BTC
                    text_transform=(text_transform, text_transform, text_transform),
                   )

# speed up projects with lots of text by preloading the font!
pyportal.preload_font()

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
    time.sleep(60)
