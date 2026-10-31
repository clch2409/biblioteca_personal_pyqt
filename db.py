import pymysql
import os
from dotenv import load_dotenv


class DataBase:

  def __init__(self):
    load_dotenv()
    self.servername = "localhost"
    self.database = "biblioteca_personal"
    self.username = "root"
    self.password = os.getenv("DB_PASSWORD")

  def conectar(self):
    return pymysql.connect(
      host=self.servername,
      user=self.username,
      password=self.password,
      port=3306,
      database=self.database,
      charset='utf8mb4'
    )
