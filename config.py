class Basic:
    HOST = 'localhost'
    PORT = 8080


class Development(Basic):
    SECRET_KEY = 'compaodif'
    DEBUG = True
class Production(Basic):
    SECRET_KEY = 'docmeaoddinglodjneojsoeudkloieosoejfosiejsodjodkshaejidkoisjdcid'