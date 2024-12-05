import pymysql
# from flask import g
# class dbconn:
#     @classmethod
#     def get_db(self):
#         return pymysql.connect(
#             host = 'database-1.cvgatyvcfvop.ap-northeast-2.rds.amazonaws.com',
#             user = 'admin',
#             password = 'qwer1234',
#             db = 'dreammelody',
#             charset = 'utf8',
#             port = 3306,
#             autocommit = True            
#         )
        
        

from flask import g

class DBconn:
    def get_db(self):
        """데이터베이스 연결 생성 및 반환"""
        if 'db' not in g:
            g.db = pymysql.connect(
                host='database-1.cvgatyvcfvop.ap-northeast-2.rds.amazonaws.com',         # MySQL 서버 주소
                user='admin',     # MySQL 사용자 이름
                password='qwer1234', # MySQL 비밀번호
                db='dreammelody',       # 데이터베이스 이름
                charset='utf8mb4',        # 문자 인코딩
                port = 3306,
                autocommit = True,    
                cursorclass=pymysql.cursors.DictCursor
            )
        return g.db

    def close_db(self, e=None):
        """요청 종료 시 데이터베이스 연결 닫기"""
        db = g.pop('db', None)
        if db is not None:
            db.close()

dbconn = DBconn()