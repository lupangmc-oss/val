import streamlit as st
import tempfile
import time
import numpy as np

# 1. 페이지 설정
st.set_page_config(
    page_title="발로란트 티어 예측기",
    page_icon="🎯",
    layout="centered"
)

# 2. 앱 제목 및 설명
st.title("🎯 발로란트 플레이 영상 티어 예측기")
st.write("클립 영상을 업로드하면 AI가 에임, 반응 속도, 움직임을 분석하여 예상 티어를 측정합니다.")

# 3. 비디오 분석 함수 (추후 AI 모델 연동 위치)
def analyze_video_and_predict(video_bytes):
    # 테스트용 임의 결과 반환 (AI 모델 연동 시 실제 예측 결과값으로 대체)
    tiers = ["아이언", "브론즈", "실버", "골드", "플래티넘", "다이아몬드", "초월자", "임모탈", "레디언트"]
    predicted_tier = np.random.choice(tiers)
    confidence = np.random.uniform(75.0, 98.5)
    
    return predicted_tier, confidence

# 4. 파일 업로드
uploaded_file = st.file_uploader(
    "발로란트 플레이 영상(MP4, MOV, AVI)을 업로드하세요", 
    type=["mp4", "mov", "avi"]
)

if uploaded_file is not None:
    # 비디오 재생 화면
    st.video(uploaded_file)
    
    # 분석 시작 버튼
    if st.button("티어 분석 시작", type="primary"):
        with st.spinner("영상을 분석하는 중입니다... (헤드라인 유지율, 크로스헤어 움직임 추적)"):
            # 비디오 데이터 분석 실행
            tier, conf = analyze_video_and_predict(uploaded_file.read())
            
            # 분석 대기 연출
            time.sleep(2.0)

        # 결과 출력
        st.success("분석이 완료되었습니다!")
        st.markdown("---")
        
        # 티어 및 신뢰도 표시
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="예측 티어", value=tier)
        with col2:
            st.metric(label="신뢰도", value=f"{conf:.1f}%")

        # 세부 결과 피드백
        st.subheader("📊 상세 분석 피드백")
        st.write("• **헤드라인 유지율**: 교전 중 조준선 높이가 안정적으로 유지됨")
        st.write("• **무빙 및 브레이킹**: 사격 전 정지 타이밍 적절함")
        st.write("• **개선점**: 첫발 집탄률 및 스킬 활용 연계 반응 속도 보완 필요")
