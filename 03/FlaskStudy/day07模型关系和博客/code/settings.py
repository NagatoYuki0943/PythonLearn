class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 测试设置设为Ture


class DevelopmentConfig(Config):
    ENV = "development"


class ProductionConfig(Config):
    ENV = "production"
    DDEBUG = False
