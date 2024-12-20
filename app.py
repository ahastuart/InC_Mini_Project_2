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

from flask import Flask, render_template, redirect, url_for, session
from flask_cors import CORS
import logging
from mypage import mypage_bp


# 블루프린트 임포트
from route.user_route import user_page
from route.dream_page import bp as dream_page
# from music.music import music_bp

# 로깅 설정
logging.basicConfig(level=logging.INFO)
# logging.info(f"Session set: {session}")


app = Flask(__name__)
CORS(app)
app.secret_key = 'zl934h23i23I23lsc94b'

# 블루프린트 등록
app.register_blueprint(user_page)
app.register_blueprint(dream_page)
# app.register_blueprint(music_bp)
app.register_blueprint(mypage_bp)

if __name__ == '__main__':
    app.run(debug=True)