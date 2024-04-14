import json
import logging.config


def configure_logging():
    with open("app/config/logging_config.json", encoding="utf-8") as config_file:
        logging_config = json.load(config_file)
        logging.config.dictConfig(logging_config)
