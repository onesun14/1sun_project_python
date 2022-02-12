import streamlit as st

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
