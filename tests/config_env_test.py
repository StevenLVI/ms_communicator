import os


class ConfigEnvTest(object):

    def __init__(self):
        self.__load__()

    def __load__(self):
        self.ENVIRONMENT = os.environ.get('ENVIRONMENT', 'testing')
        self.POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
        self.POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5455')
        self.POSTGRES_USER = os.environ.get('POSTGRES_USER', 'communicator_api')
        self.POSTGRES_PWD = os.environ.get('POSTGRES_PWD', 'communicator_api')
        self.DEBUG = os.environ.get('DEBUG', 'True')
        self.CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6378/0')
        self.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6378/0')
        self.REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6378/0')
