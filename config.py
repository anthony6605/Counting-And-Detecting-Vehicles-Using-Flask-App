class Config(object):

    SECRET_KEY = 'Made By Anthony'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
