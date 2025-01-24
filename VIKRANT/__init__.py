from VIKRANT.core.bot import Sona
from VIKRANT.core.dir import dirr
from VIKRANT.core.git import git
from VIKRANT.core.userbot import Userbot
from VIKRANT.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
