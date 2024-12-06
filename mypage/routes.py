from flask import render_template, session
from dbconn.DBconn import dbconn

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