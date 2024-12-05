import pymysql
from config import DB_CONFIG

class dbconn:
    @classmethod
    def get_db(cls):
        try:
            return pymysql.connect(**DB_CONFIG)
        except Exception as e:
            print(f"데이터베이스 연결 실패: {e}")
            raise