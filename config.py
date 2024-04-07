import os
import dotenv
import enum
from typing import Final


dotenv.load_dotenv(".env")


class AppConfig(enum.Enum):
    DATABASE_URL: Final[str] = os.environ["DATABASE_URL"]