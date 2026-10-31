import pymysql
import os
from dotenv import load_dotenv


class DataBase:

  def __init__(self):
    load_dotenv()
    self.host = os.getenv("HOST")
    self.database = os.getenv("DATABASE")
    self.username = os.getenv("USER")
    self.password = os.getenv("DB_PASSWORD")
    self.port = int(os.getenv("PORT"))

  def conectar(self):
    return pymysql.connect(
      host=self.host,
      user=self.username,
      password=self.password,
      port=self.port,
      database=self.database,
      charset='utf8mb4'
    )
