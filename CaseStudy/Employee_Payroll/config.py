import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Neethu%40123456@localhost/employee"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")

