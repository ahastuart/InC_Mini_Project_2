from flask import Blueprint, render_template, request, redirect, url_for

# Blueprint 생성
bp = Blueprint('dream_page', __name__, url_prefix='/dream')

# 폼 페이지 라우트
@bp.route('/', methods=['GET', 'POST'])
def dream_form():
    if request.method == 'POST':
        # 폼 데이터 가져오기
        dream_content = request.form.get('dream_content', '')
        return redirect(url_for('dream_page.result_page', dream_content=dream_content))

    # GET 요청 시 form.html 렌더링
    return render_template('form.html')

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

