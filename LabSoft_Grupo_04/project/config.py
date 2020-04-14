import os


class Config:
    SECRET_KEY = '4fe1b39c0b1cfadd33d3cb31b82e1af8'#os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:bulbasaur@localhost/project'