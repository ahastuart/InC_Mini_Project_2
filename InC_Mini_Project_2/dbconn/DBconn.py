import pymysql
class dbconn:
    @classmethod
    def get_db(self):
        return pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'qwer1234',
            db = 'subway_station_proj',
            charset = 'utf8',
            port = 3306,
            autocommit = True            
        )