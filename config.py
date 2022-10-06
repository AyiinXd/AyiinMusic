from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("5110852446:AAEKOtJLcUet20LSJLJQR1e01cSMU6_bl3w")
API_ID = int(getenv("18572275", ""))
API_HASH = getenv("09c853c71df1072cc18f7b7d41495456")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
ASSISTANT_PREFIX = list(getenv("play", ".").split())
MONGO_DB_URI = getenv("mongodb+srv://eldika:<password>@cluster0.txxp1ev.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("5 3 9 2 4 9 2 6 4 3", "").split()))
OWNER_ID = list(map(int, getenv("2120680469", "").split()))
LOG_GROUP_ID = int(getenv("1001700716779", ""))
MUSIC_BOT_NAME = getenv("musim")
HEROKU_API_KEY = getenv("273474bf-1028-44ee-9f25-020c3618edd0")
HEROKU_APP_NAME = getenv("El Dika")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/AyiinXd/MultiAssistant"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = https://t.me/dikalikemusic
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = https://t.me/dklikesong
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(BQCpHZZSUMflja-Pu__3apEZWgyybcH2XfOHvxc3XSAZENu2P0C1MrNfumOadiYKi96efMLs8njp94N5A7IM8_7U88aUnSoT6we-IfscUBEq4LgsjRssbx5WU2SYZ7OcopuV2NbDLPiQSp1u_fziQSfmlHSGMuEW0cXdUAGHLh1hYNpfqInRj4su6rKXD6P86sZq5Nzru8EvrhMhB2kk3NcnHATqytSIm69NhezBCv_2JCZeWRQ-bV1EYxf_9o_GfWAM7eIA1eX0MhSshDbO62ys8t6s82wJFlliqyyMnKbmtR9vVsUmxMyup840RXwL-7UzZOZBhiobIoW5Zcwv9vBmAAAAAUFq6GMA)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(BQBl_SsamYv3sjnjzf9ZqfDJsJiE4ExUxA7JP87_L547fpC5Z_pkqW4aaiWyNu3mOM4HehuzEqLI6Rpv7Jgj41nuPfNUGO0_M6HuY4D3LWp41B1wWpkdBu8yvS7k6ZTZdk1_Y10-GFtIsjFfzOTeZpRiGxvfNRgCyXNI9om-vAUJ9fbCIMNfJ0SCIz3Gn3iCAOCEs-M8BnfHJceNmICtuHH-mK6Aqa0BBdJgDzoinLCjf5I9D2ygVcYdbqk-G8vjycIjMbGi1Xhhp8Ib8jXureYdMzNdOArSRrdBKKLh8_3_fmtAf9fue01lq4UFTqUTntqVWnKseLgkAQ0aAGZpciocAAAAAUFq6GMA)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(BQCrZFy_1RtQd_86T2ZLtm2BIM8wK8_nu-w_U_JgndbFpiecs5raX_6eX7jJnWACnQKbztrG0sLwPUQZvfXqhi2RuUH9F5Gx4Arr0P8sxu2kajvlgrx69HUrjPP9BGCJO2kAOEbGJIrXSlOTdpqneSgw7ibO25sJUqynIaY5ngMPRWdEzSfE-zjrJDL0IXd6ee5ScbFGhGlSazv9ZUV78IiVozLU5MxNnn1DYd93BR2TOfmvg77NX46yGMENk9prk-egr1LgztZwDrQTwHR2PQTCeEzhndOj1MLtYQWxJwuB27Quc5afXYCfZfKplDANnadMtvMvvpEug63cCm7nO3q-AAAAAUFq6GMA)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(BQAPPqzcwu9OvMYYpxt2tcZ2M3Jlf2lwUuKTD4TdVdKFdmBIJXAhvpUW9eg78K4JGVAvhvb_AuJgPg69rIdjVxAUAZwiKslxdTU-BiydopfDQC1ghuy_7GYo4-DUGKjP3z-WKYBV4VhdLMXN2kNwTRFMiVXsRDJWBr5F4juzkI8p8TOrH2xKmfUjFtBuSm_X7uYfDNYKAljHe9dCucwhZgru4i0sjfGSgGddUZ_3-CFcVZVMoY8N5qrb1LBHYO_rjVmZfLKQ1Zfg2WZ-eXxjvDqwuzjhv3MfUApD6Y4J2JIQOGdLMR3v1Z9sOFOm13IWSqS9S4rB_jQNODBG4ery5tZaAAAAAUFq6GMA)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(BQAzyDTRe5KPuACtkfU6pzPVAHMWnrL6tPA1sAd0xpah_GG49NZGPfLRmuwzzvEQ3t8SwPIr0_G-HVuCRYmoyZHc6vIU97RHjIslF5yAkt25YW_-CEjH-OpZSOpRTD_XJqcyq6FwFQXee5HuSmhYlMPaa02dMNJfWyPY8XB_E4ERVelLCwWFgnJuXOkRShMLRzW8HxSKcip-1pByXSlHwsurlSkJ_YF7sDYx_CAgWmR7fKEfAgKgA5kj0f7YkwxcKN7kCv73l7ZxEWEOia9q0fvswE2O4_3VXWPXN0BnlPhkVWQ94VQNwzh6mHtTqRjvsdLhS-qAAwx4cYym6uAbpb5bAAAAAUFq6GMA)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(BQDBf36mhCiqmxBNgmHdWv76LNhp5kyhQN1C0hOhZzYpFYkczA0kJlek7m8k7rt23ve7neAOay38EBtVLI2jew8zk405df8iy_Ur0i92zbz8TA0mU7y3x4mzd9xj4RwKTHejZf26yivJnzMN1Ro-CSxx5qzcO3Fl8xZrOeejUmkqNnV1chEdUyRQSecDiwBSr2bpo3QSdNxfcJdhqIYjLsjmEI57-JGeCcGzex1MmyRHCgnC64t51vRImV1rtxpNJ6iPFH97vIWn_kBNjP5jZEFgJolmSGxZTeYEVNMd-U_XSHBHvK1QH7cQcWB5l1Kg61rZdLYUKlpOMRKrolsZEgJjAAAAAUFq6GMA)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
