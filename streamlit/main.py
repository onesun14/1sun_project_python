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

if st.button("Click Button"):
    st.write("Hello test")

# 2. Check Box
checkbox_btn = st.checkbox("Checkbox button")
if checkbox_btn:
    st.write("Good!")

# If you want to default value = True
checkbox_btn2 = st.checkbox("Checkbox button2", value=True)

if checkbox_btn2:
    st.write("hello")

# Radio Button
selected_item = st.radio("Radio Button", ("hi", "hello", "bye"))

if selected_item == "hi":
    st.write("hi!")
elif selected_item == "hello":
    st.write("hello!")
elif selected_item == "bye":
    st.write("bye!")

option = st.selectbox("Please selectin selectbox!", ('hi', 'hhi', 'hiii'))
st.write("option is ", option)

multi_option = st.multiselect("Please select multi box", ("a", "b", "c"))
st.write('you selected', multi_option)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 25.0))
st.write('Values:', values)

@st.cache
def load_data():
    pass
