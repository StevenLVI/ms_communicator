import os


class ConfigEnv(object):

    def __init__(self):
        self.__load__()

    def __load__(self):
        self.ENVIRONMENT = os.environ.get('ENVIRONMENT', 'localhost')
        self.DEBUG = os.environ.get('DEBUG', 'True')

        # Hash
        self.HASH_IDS_SALT = os.environ.get('HASH_IDS_SALT', 'L0HK7TChWt71aq5ZVpw905HY')
        self.HASH_MIN_SIZE = os.environ.get('HASH_MIN_SIZE', 5)
        self.HASH_DOMAIN = os.environ.get('HASH_DOMAIN', 'localhost')

        # Postgres
        self.POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
        self.POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5418')
        self.POSTGRES_USER = os.environ.get('POSTGRES_USER', 'communicator')
        self.POSTGRES_PWD = os.environ.get('POSTGRES_PWD', 'communicator')

        # Redis
        self.CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
        self.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
        self.REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
