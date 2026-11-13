import logging
from pathlib import Path
from time import asctime

config = logging.getLogger("config")
config.setLevel(logging.INFO)
config.info("app started")
HOME_DIR = Path(__file__).parent.parent.resolve()


class Directories:
    Home = HOME_DIR
    Model = Home / "model"
    Logs = Home / "logs"
    Data = Home / "data"
    Cache = Home / "cache"

    @classmethod
    def ensure(cls):
        for d in (cls.Model, cls.Logs, cls.Data, cls.Cache):
            d.mkdir(parents=True, exist_ok=True)

class Setup:
    def logging:
DIRS = Directories()
DIRS.ensure()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
