#----------------Dockerfile 내용----------------
# 베이스 이미지 선택 (Python 사용)
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 환경 변수 파일 복사
COPY .env .env

# 애플리케이션 실행 포트 설정
EXPOSE 5000

# 애플리케이션 실행 명령어
CMD ["gunicorn", "--bind", "127.0.0.1:5000", "app:app"]
