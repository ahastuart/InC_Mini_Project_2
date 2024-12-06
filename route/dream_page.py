from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from comprehend.comprehend_utils import analyze_dream_content
from comprehend.com_visualize import create_sentiment_chart_text
from comprehend.com_db import save_dream, save_analysis_result
from music.music import get_playlist
from music.deepL import translate

# Blueprint 생성
bp = Blueprint('dream_page', __name__, url_prefix='/dream')

# 폼 페이지 라우트
@bp.route('/', methods=['GET', 'POST'])
def dream_form():
    if request.method == 'POST':
        # 폼 데이터 가져오기
        dream_content = request.form.get('dream_content', '')
        if not dream_content:
            flash("꿈 내용을 입력해주세요.")
            return redirect(url_for('dream_page.dream_form'))

        try:
            # 현재 로그인된 사용자 ID (세션에서 가져온다고 가정)
            user_id = session.get('user_id')
            if not user_id:
                flash("로그인이 필요합니다.")
                return redirect(url_for('user_page.user_login_service'))

            # 1. 꿈 내용 저장
            dream_id = save_dream(user_id, dream_content)

            # 2. AWS Comprehend로 꿈 내용 분석
            analysis_result = analyze_dream_content(dream_content)

            # 3. 분석 결과 저장
            en_dream_content = translate(dream_content)
            save_analysis_result(dream_id, analysis_result)

            # 4. 감정 분석 차트 생성
            chart_data = create_sentiment_chart_text(analysis_result)

            # 5. 추천 음악 로직 추가 (간단히 문자열로 설정)
            recommended_music = get_playlist(dream_id, analysis_result)

            # 결과 페이지 렌더링
            return render_template(
                'result.html',
                dream_content=dream_content,
                chart_data=chart_data,
                recommended_music=recommended_music
            )

        except Exception as e:
            flash(f"오류 발생: {str(e)}")
            return redirect(url_for('dream_page.dream_form'))

    # GET 요청 시 form.html 렌더링
    return render_template('result.html')

# 결과 페이지 라우트
@bp.route('/result', methods=['GET'])
def result_page():
    # URL 파라미터에서 데이터 가져오기
    dream_content = request.args.get('dream_content', '작성된 꿈이 없습니다.')
    return render_template('result.html', dream_content=dream_content)

# 시작 서비스 라우트
@bp.route('/start_service', methods=['GET'])
def start_service():
    # main.html 렌더링
    return render_template('main.html')

def inject_user():
    return {
        'email': session.get('email'),
    }

