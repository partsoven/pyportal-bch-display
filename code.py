"""
This example will access the coindesk API, grab a number like bitcoin value in
USD and display it on a screen
If you can find something that spits out JSON data, we can display it!
"""
import time
import board
from adafruit_pyportal import PyPortal

# You can display in 'GBP', 'EUR' or 'USD'
CURRENCY = 'USD'
# Set up where we'll be fetching data from
#DATA_SOURCE = "https://api.coindesk.com/v1/bpi/currentprice.json"
#DATA_SOURCE = "https://api.coinbase.com/v2/prices/BCH-USD/spot.json"
DATA_SOURCE = "https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD"
#DATA_LOCATION = ['bpi', CURRENCY, 'rate_float']
DATA_LOCATION = ["USD"]


def text_transform(val):
    return "$%d" % val


# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE, json_path=DATA_LOCATION,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/bitcoin_background2.bmp",
                    text_font=cwd+"/fonts/Arial-Bold-24-Complete.bdf",
                    text_position=(195, 130),
                    text_color=0x0,
                    text_transform=text_transform)
pyportal.preload_font(b'$012345789')  # preload numbers
pyportal.preload_font((0x00A3, 0x20AC)) # preload gbp/euro symbol

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)

    time.sleep(3*60)  # wait 3 minutes
