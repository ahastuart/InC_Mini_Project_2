# from flask import Flask
# from flask_cors import CORS
# # import pymysql  # 필요 CHECK
# import logging
# # from datetime import datetime  # 필요 CHECK

# # 블루프린트 임포트

# from route.user_route import user_page
# from route.dream_page import bp as dream_page

# # 로깅 설정
# logging.basicConfig(level=logging.INFO)

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'zl934h23i23I23lsc94b'

# # 블루프린트 등록

# app.register_blueprint(user_page)
# app.register_blueprint(dream_page)



# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
import logging

# 블루프린트 임포트
from route.user_route import user_page
from route.dream_page import bp as dream_page

# 로깅 설정
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)
app.secret_key = 'zl934h23i23I23lsc94b'

# 블루프린트 등록
app.register_blueprint(user_page)
app.register_blueprint(dream_page)

# # 기본 라우트 설정
# @app.route('/')
# def home():
#     # 기본 경로에서 dream_page.start_service로 리디렉션
#     return redirect(url_for('dream_page.start_service'))

if __name__ == '__main__':
    app.run(debug=True)