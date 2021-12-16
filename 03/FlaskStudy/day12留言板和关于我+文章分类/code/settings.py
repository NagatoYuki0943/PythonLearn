import os


class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 测试设置设为Ture
    SECRET_KEY = 'faea3a8fe31sfe4a6e7a6fe84'    # 给session设置key

    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # os.path.abspath(__file__) 获取文件路径,再通过dirname删除掉文件名
    # 静态文件夹的路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 头像的上传目录
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')
    # 相册的上传目录
    UPLOAD_PHOTO_DIR = os.path.join(STATIC_DIR, 'upload/photo')


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DDEBUG = False


if __name__ == "__main__":
    print(os.path.abspath(__file__))# d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code\settings.py
    print(Config.BASE_DIR)          # d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code
    print(Config.STATIC_DIR)        # d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code\static
    print(Config.TEMPLATE_DIR)      # d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code\templates
    print(Config.UPLOAD_ICON_DIR)   # d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code\static\upload/icon
    print(Config.UPLOAD_PHOTO_DIR)  # d:\Python\Pycharm\03\FlaskStudy\day10图片上传和文章展示\code\static\upload/photo
