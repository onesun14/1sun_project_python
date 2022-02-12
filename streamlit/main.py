import streamlit as st

st.title("Title")

st.header("Header")

st.subheader("Subheader")

st.write("Hello world")

import streamlit as st
'''
데이터가 많을때 중간에 캐쉬를 놓아서 속도를 개선 시킨다.
1. 함수이름 확인
2. 함수를 구성하는 코드 확인
3. 함수 호출시 사용한 매개변수
4. 위 3개를 로컬에 저장해두고 다시 호출시 사용할 수 있으면 그대로 사용한다.
'''
#데코레이션, 함수를 꾸며주는건데
#함수에서 반복적으로 사용되는게 있을때 그거를 모아놓은거라고 생각하지면 될것 같아요.

@st.cache
def load_data():
    pass
