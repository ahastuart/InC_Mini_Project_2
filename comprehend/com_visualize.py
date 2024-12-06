def create_sentiment_chart_text(analysis_result):
    """
    감정 분석 결과를 텍스트 기반으로 시각화합니다.

    Parameters:
        analysis_result (dict): 감정 분석 결과

    Returns:
        str: 텍스트 기반의 감정 비율 표시
    """
    labels = ['Positive', 'Negative', 'Neutral', 'Mixed']
    scores = [
        analysis_result['positive'],
        analysis_result['negative'],
        analysis_result['neutral'],
        analysis_result['mixed']
    ]
    
    # 텍스트 기반 출력 생성
    chart = "\nSentiment Analysis Results:\n"
    total = sum(scores)  # 모든 감정 점수의 합
    for label, score in zip(labels, scores):
        percentage = (score / total) * 100 if total > 0 else 0
        chart += f"{label}: {percentage:.1f}% {'#' * int(percentage // 5)}\n"

    return chart


# import matplotlib.pyplot as plt
# import io
# import base64

# def create_sentiment_chart(analysis_result):
#     """
#     감정 분석 결과로 원형 차트를 생성하고 이미지로 반환합니다.
    
#     Parameters:
#         analysis_result (dict): 감정 분석 결과
        
#     Returns:
#         str: Base64로 인코딩된 이미지 데이터
#     """
#     # 데이터 준비
#     labels = ['Positive', 'Negative', 'Neutral', 'Mixed']
#     sizes = [
#         analysis_result['positive'],
#         analysis_result['negative'],
#         analysis_result['neutral'],
#         analysis_result['mixed']
#     ]
#     colors = ['#2ecc71', '#e74c3c', '#3498db', '#f1c40f']  # 색상 지정
#     explode = (0.1, 0, 0, 0)  # 강조할 섹션(Positive)을 약간 분리

#     # 차트 생성
#     plt.figure(figsize=(6, 6))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, startangle=140)
#     plt.title('Sentiment Analysis Results')

#     # 차트를 이미지로 저장
#     img_buffer = io.BytesIO()
#     plt.savefig(img_buffer, format='png')
#     img_buffer.seek(0)
#     chart_data = base64.b64encode(img_buffer.getvalue()).decode()
#     plt.close()

#     return chart_data
