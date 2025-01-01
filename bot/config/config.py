from pydantic_settings import BaseSettings, SettingsConfigDict
from bot.utils import logger
import sys

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 1234
    API_HASH: str = 'abcd'
    
    SUPPORT_AUTHOR: bool = True
    
    AUTO_UPGRADE_TAP_CARDS: bool = False
    JACKPOT_LEVEL: int = 1
    CRIT_LEVEL: int = 1
    ENERGY_LEVEL: int = 1
    TAP_LEVEL: int = 1
    ENERGY_REGEN_LEVEL: int = 1
    
    AUTO_UPGRADE_MINE_CARDS: bool = True
    MAX_CARD_PRICE_PURCHASE: int = 100000000000
    PROFIT_UPGRADE: bool = True
    
    AUTO_TAP: bool = True
    TAPS_PER_BATCH: list[int] = [45, 60]
    DELAY_BETWEEN_TAPS: list[int] = [10, 20]
    
    AUTO_TASK: bool = True
    AUTO_JOIN_CHANNELS: bool = True
    AUTO_NAME_CHANGE: bool = True
    
    COLLECT_REFER_BALANCE: bool = True
    
    JOIN_GANG: bool = True
    GANG_USERNAME: str = 'mainecode'
    
    SOLVE_COMBO: bool = True
    
    AUTO_SIGN_IN: bool = True
    AUTO_OPEN_FREE_BOX: bool = True
    
    AUTO_SPINS: bool = True
    SPIN_COUNT: int = 10

    SLEEP_TIME: list[int] = [2700, 4200]
    START_DELAY: list[int] = [5, 100]
    
    REF_KEY: str = 'ref_4ZYOUF2o' #KEY AFTER 'startapp=' from invite link
    IN_USE_SESSIONS_PATH: str = 'bot/config/used_sessions.txt'
    
    TRACK_BOT_UPDATES: bool = False
    
    MAX_REQUEST_RETRY: int = 3
    
    SAVE_RESPONSE_DATA: bool = False
    
    NIGHT_MODE: bool = False
    NIGHT_TIME: list[int] = [0, 7] #TIMEZONE = UTC, FORMAT = HOURS, [start, end]
    NIGHT_CHECKING: list[int] = [3600, 7200]

settings = Settings()

if settings.API_ID == 1234 and settings.API_HASH == 'abcd':
    sys.exit(logger.info("<r>Please edit API_ID and API_HASH from .env file to continue.</r>"))

if settings.API_ID == 1234:
    sys.exit(logger.info("Please edit API_ID from .env file to continue."))

if settings.API_HASH == 'abcd':
    sys.exit(logger.info("Please edit API_HASH from .env file to continue."))
    
if settings.AUTO_SPINS == True and settings.SPIN_COUNT not in [1, 2, 3, 5, 10, 50]:
    sys.exit(logger.info("Make sure SPIN_COUNT should be: 1/2/3/5/10/50."))