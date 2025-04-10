from aioinject import Object

from app.settings import DatabaseSettings
from lib.settings import get_settings
from lib.types import Providers

providers: Providers = [Object(get_settings(DatabaseSettings))]
