from VIKRANT.core.bot import vikrant
from VIKRANT.core.dir import dirr
from VIKRANT.core.git import git
from VIKRANT.core.userbot import Userbot
from VIKRANT.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = vikrant()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
