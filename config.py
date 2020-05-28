import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
DATABASE_URL = """postgres://grjpvsmpqjhecy:
                  3ee69ebf1c9bf503d0982108b5fc6e0da6a86b8443875ba5405ef37caceadcdc@ec2-34-198-243-120
                  .compute-1.amazonaws.com:5432/dbfmt3uid29nfi"""
SQLALCHEMY_TRACK_MODIFICATIONS = False
