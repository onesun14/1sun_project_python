import streamlit as st
count = 0
st.title("아주아주 신뢰도가 높은 간단한 설문조사!!")

st.header("나쁘지 않는 착한 설문조사!")

st.subheader("믿고 해도 좋다!")

st.write("이 설문조사는 설문자의 특징과 성향을 잘 캐치하여 [[[[좋은 곳]]]] 에 쓰기 위해 만든 것 입니다.")

selected_item = st.radio("Q1. 당신의 성별은?", ("남성", "여성", "모르겠다"))
if selected_item == "모르겠다":
    st.write("당신의 성별도 모르나요?")
else:
    st.write("좋습니다!")

values = st.slider('Q2. 당신의 나이는?', 0, 100)
st.write('당신의 나이는...', values, "세 로군요!")
if values == 100:
    st.write("와우! 정말 놀라운 분이시군요!")













@st.cache
def load_data():
    pass