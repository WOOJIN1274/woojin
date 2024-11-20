import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 사이드바에 페이지 선택 메뉴 추가
page = st.sidebar.selectbox("페이지 선택", ["홈", "메인 엔진", "발전기", "보일러", "보조기계"])

# 각 페이지의 내용 정의
if page == "홈":
    st.title('캡스톤 디자인')

    st.header("RAG를 이용한 선박 기기 관리 시스템")

    st.subheader('조장:홍승진')

    st.write("M/E Jacket Cooling Water Temperature")
    data = pd.DataFrame({
        'No.1': [74, 73, 75, 75, 74, 76],
        'No.2': [76, 77, 77, 76, 78, 76],
        'No.3': [77, 77, 77, 75, 78, 77],
        'No.4': [78, 79, 77, 77, 78, 78],
        'No.5': [77, 77, 78, 76, 78, 76],
        'No.6': [76, 77, 77, 75, 78, 77],
    })
    st.dataframe(data, use_container_width=True)

    plt.figure(figsize=(10, 6))
    for column in data.columns:
        plt.plot(data[column], marker='o', label=column)

    # 그래프 제목 및 레이블 설정
    plt.title('M/E Jacket Cooling Water Temperature')
    plt.xlabel('')
    plt.ylabel('Temperature')
    plt.yticks(range(68, 85))
    plt.xticks(ticks=range(len(data)), labels=range(1, len(data)+1))
    plt.legend()
    plt.grid()

    # Streamlit에 그래프 표시
    st.pyplot(plt)
    
    st.metric(label="온도", value="10℃", delta="1.2℃")
    st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
    col2.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
    col3.metric(label="달러USD", value="1,228 원", delta="-12.00 원")

elif page == "메인 엔진":
    st.header("메인 엔진")
    st.write("이곳은 첫 번째 페이지입니다.")

elif page == "발전기":
    st.header("발전기")
    st.write("이곳은 두 번째 페이지입니다.")

elif page == "보일러":
    st.header("페이지 2")
    st.write("이곳은 두 번째 페이지입니다.")

elif page == "보조기계":
    st.header("페이지 2")
    st.write("이곳은 두 번째 페이지입니다.")