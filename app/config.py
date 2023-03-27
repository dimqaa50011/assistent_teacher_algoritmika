from dataclasses import dataclass
from pathlib import Path, PosixPath
from typing import Optional, Union

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass
class BotConf:
    BOT_TOKEN: str
    USE_REDIS: str
    ADMIN: int
