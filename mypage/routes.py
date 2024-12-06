from flask import app, redirect, render_template, session, url_for
from dbconn.DBconn import dbconn
import pymysql
from . import mypage_bp

@mypage_bp.route('/mypage')
def mypage():
    # 세션에서 현재 로그인된 사용자 이메일 가져오기
    user_email = session.get('email')

    if not user_email:
        return "로그인이 필요합니다. 로그인 후 이용해주세요.", 403

    # 데이터베이스에서 사용자 정보 가져오기
    connection = dbconn.get_db()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (user_email,))
        user_data = cursor.fetchone()  # 단일 사용자 데이터

        if not user_data:
            return "사용자 정보를 찾을 수 없습니다.", 404

        return render_template('mypage.html', user_data=user_data)
    except Exception as e:
        return f"오류 발생: {e}", 500
    finally:
        cursor.close()
        connection.close()
        
        
from flask import render_template, session, redirect, url_for
import pymysql
from dbconn.DBconn import dbconn  # 데이터베이스 연결 객체 사용


from flask import render_template, session, redirect, url_for
import pymysql
from dbconn.DBconn import dbconn  # 데이터베이스 연결 객체 사용
from . import mypage_bp  # Blueprint import

@mypage_bp.route('/user_info')
def user_info():
    # 세션에서 현재 로그인된 사용자 이메일 가져오기
    user_email = session.get('email')

    if not user_email:
        return "로그인이 필요합니다. 로그인 후 이용해주세요.", 403

    # 데이터베이스에서 사용자 정보 가져오기
    connection = dbconn.get_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)  # DictCursor로 결과를 딕셔너리로 반환

    try:
        query = "SELECT id, email, username, created_date FROM users WHERE email = %s"
        cursor.execute(query, (user_email,))
        user_data = cursor.fetchone()  # 단일 사용자 데이터 가져오기

        if not user_data:
            return "사용자 정보를 찾을 수 없습니다.", 404

        # user_info.html 템플릿으로 데이터 전달
        
        return render_template('mypage.html', user=user_data)
        
    except Exception as e:
        return f"오류 발생: {e}", 500
    finally:
        cursor.close()
        connection.close()
