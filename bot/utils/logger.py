import sys
from loguru import logger


logger.remove()
logger.add(sink=sys.stdout, format="<white>BUMS 2.1</white>"
                                   " | <white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                   " | <level>{level: <8}</level>"
                                   " | <cyan><b>{line}</b></cyan>"
                                   " - <white><b>{message}</b></white>")
logger = logger.opt(colors=True)