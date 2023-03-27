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


@dataclass
class DbConf:
    DB_NAME: str
    DB_USER: str
    DB_PASSWD: str
    DB_HOST: str
    DB_PORT: str
    SCHEME: str
    SQLALCHEMY_DATABASE_URI: str


@dataclass
class AppConfig:
    bot_config: BotConf
    db_conf: DbConf


def get_config(path_to_file: Optional[Union[str, PosixPath]] = None) -> AppConfig:
    env = Env()
    env.read_env(path_to_file)

    db_name = env.str("DB_NAME")
    db_user = env.str("DB_USER")
    db_passwd = env.str("DB_PASSWD")
    db_host = env.str("DB_HOST")
    db_port = env.str("DB_PORT")
    scheme = env.str("SCHEME")
    sqlalchemy_database_uri = "{}://{}:{}@{}:{}/{}".format(
        scheme, db_user, db_passwd, db_host, db_port, db_name
    )

    return AppConfig(
        bot_config=BotConf(BOT_TOKEN=env.str("BOT_TOKEN"), USE_REDIS=env.str("USE_REDIS"), ADMIN=env.int("ADMIN")),
        db_conf=DbConf(
            DB_PORT=db_port, DB_NAME=db_name, DB_HOST=db_host,
            DB_USER=db_user, DB_PASSWD=db_passwd, SCHEME=scheme,
            SQLALCHEMY_DATABASE_URI=sqlalchemy_database_uri
        )
    )
