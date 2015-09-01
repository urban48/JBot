import requests
requests.packages.urllib3.disable_warnings()

LOG_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ["consoleHandler"],
        'level': 'DEBUG',
        'formatters': 'simpleFormatter',
    },

    'loggers': {
        "requests": {
            "handlers": ['consoleHandler'],
            "level": "ERROR",
            "propagate": False,
            "qualname": requests.packages.urllib3.connectionpool
        },
    },
    'handlers': {

        'consoleHandler': {
           "class": "logging.StreamHandler",
           "level": "DEBUG",
           'formatter': 'simpleFormatter',
           "stream": "ext://sys.stdout"
       },
    },

    'formatters': {
        "simpleFormatter": {
            "format": "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
        },

    }
}