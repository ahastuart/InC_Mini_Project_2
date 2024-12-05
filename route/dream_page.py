from flask import Blueprint, render_template, request, redirect, url_for, flash
from comprehend.comprehend_utils import analyze_dream_content

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
            # AWS Comprehend로 꿈 내용 분석
            analysis_result = analyze_dream_content(dream_content)

            # 결과 페이지로 데이터 전달
            return render_template(
                'result.html',
                dream_content=dream_content,
                analysis=analysis_result
            )
        
        except Exception as e:
            flash(f"분석 중 오류가 발생했습니다: {str(e)}")
            return redirect(url_for('dream_page.dream_form'))

    # GET 요청 시 form.html 렌더링
    return render_template('form.html')

# 결과 페이지 라우트
@bp.route('/result', methods=['GET'])
def result_page():
    # URL 파라미터에서 데이터 가져오기
    dream_content = request.args.get('dream_content', '작성된 꿈이 없습니다.')
    return render_template('result.html', dream_content=dream_content)
