import streamlit as st
list = []
Q4 = "아래 3개중 하나를 골라주세요"
Q6 = 0
Q7 = ""
Q8 = "이곳에 작성해 주세요."
id = ""
ps = ""


st.title("GAME 설문조사")

st.header("쉽게 할 수 있는 설문조사")

st.subheader("당신이 즐기는 게임이란?")

st.write("이 설문조사는 당신의 게임 등을 조사하는 아주 간단한 설문조사 입니다.")
st.write("*Q0 같이 *가 붙은 질문은 필수로 작성해야 하는 질문입니다.")
st.write("설문을 작성해야 생기는 질문들이 있습니다. 우선 Q3 까지 작성해주세요.")

Q1 = st.radio("Q1. 당신의 성별은?", ("남성", "여성", "모르겠다"))

Q2 = st.slider('Q2. 당신의 나이는?', 0, 100)

Q3 = st.selectbox("*Q3. 당신이 좋아하는 게임 종류는?", ('이곳을 클릭하여 선택해 주세요.', '어드벤처', '아케이드', '스포츠', 'MMORPG', '롤플레잉', '시뮬레이션', '퍼즐', 'MOBA', '기타'))
if Q3 == "기타":
    Q3_1 = st.text_area("*Q3_1그렇다면 어떤 종류를 좋아하시나요?", "이곳에 작성해 주세요.")
else:
    Q3_1 = ""
if Q3 != "이곳을 클릭하여 선택해 주세요.":
    if Q3 == "기타":
        if Q3_1 != "" and Q3_1 != "이곳에 작성해 주세요.":
            Q4 = st.radio("*Q4. 당신이 즐겨하는 직업군은?", ("아래 3개중 하나를 골라주세요", "딜러", "탱커", "힐러"))
    else:
        Q4 = st.radio("*Q4. 당신이 즐겨하는 직업군은?", ("아래 3개중 하나를 골라주세요", "딜러", "탱커", "힐러"))


if Q4 != "아래 3개중 하나를 골라주세요":
    Q5 = st.slider('Q5. 당신의 게임을 플레이하는 시간대는?', 0.0, 24.0, (8.0, 10.0))
    st.write('당신은', Q5, '사이 시간대에 플레이 하시는 군요')
    Q6 = st.number_input("Q6. 당신이 원하는 게임의 만렙대는? (-, +로 설정 or 직접 입력)", 0)
if Q6 != 0:
    Q7 = st.text_input("Q7. 당신이 최근에 했거나 재밌게 했던 게임의 이름을 입력해 주세요.")

if Q7 != "":
    Q8 = st.text_area("Q8. 당신이 방금 위에서 작성했던 게임을 리뷰해 주세요. (게임의 이름만 입력하여도 됩니다.)", "이곳에 작성해 주세요.")

if Q8 != "이곳에 작성해 주세요.":
    Q9 = st.date_input("Q9. 마지막으로 게임을 했던 날짜를 작성해주세요. (직접 입력 or 클릭하여 날짜를 직접 설정 가능합니다..)")
    Q10 = st.selectbox("Q10. 당신이 희망하는 게임 이벤트의 종류는?", ("퀴즈형 문답 이벤트", "참여형 이벤트", "공모전 형태의 이벤트", "할인 이벤트", "기타"))
    if Q10 == "기타":
        Q10_1 = st.text_area("그렇다면 어떤 종류의 이벤트를 희망하시나요?", "이곳에 작성해 주세요.")
    else:
        Q10_1 = ""
    if Q10_1 != "이곳에 작성해 주세요.":
        if Q10 == "기타":
            if Q10_1 != "" and Q10_1 != "이곳에 작성해 주세요.":
                Q11 = st.time_input("Q11. 당신이 희망하는 게임 이벤트의 시작 시간은?")
                st.header("Q12.")
                st.image("./test/모코코.png", use_column_width=True)
                Q12 = st.radio("이 사진을 보고 사진과 관련된 게임을 바로 떠올릴수 있다.", ("바로 떠올랐다.", "이 사진은 본적이 있지만 게임은 모른다.", "도저히 모르겠다"))

                id = st.text_input("enter the input")

                ps = st.text_input("enter the number", type="password")
        else:
            Q11 = st.time_input("Q11. 당신이 희망하는 게임 이벤트의 시작 시간은?")
            st.header("Q12.")
            st.image("./test/모코코.png", use_column_width=True)
            Q12 = st.radio("이 사진을 보고 사진과 관련된 게임을 바로 떠올릴수 있다.", ("바로 떠올랐다.", "이 사진은 본적이 있지만 게임은 모른다.", "도저히 모르겠다"))

            id = st.text_input("enter the input")

            ps = st.text_input("enter the number", type="password")


if id != "" and ps != "":
    st.header("이상으로 설문조사를 마치겠습니다 설문에 응답해주셔서 감사합니다.")
    if st.button("설문조사 종료"):
        st.write("설문조사를 저장합니다...")
        path = "./josa/"
        f = open(path + "{}_{}.txt".format(id, ps), 'w')
        f.write("설문자의 아이디:" + id)
        f.write("\n")
        f.write("설문자의 페스워드:"+ps)
        f.write("\n")
        f.write("설문자의 성별:"+Q1)
        f.write("\n")
        f.write("설문자의 나이:"+ str(Q2))
        f.write("\n")
        f.write("설문자가 좋아하는 게임의 종류:"+Q3)
        f.write("\n")
        f.write("설문자의 3번 질문의 기타 설명:"+Q3_1)
        f.write("\n")
        f.write("설문자가 즐겨하는 직업군:"+str(Q4))
        f.write("\n")
        f.write("설문자가 게임을 플레이하는 시간대:"+str(Q5))
        f.write("\n")
        f.write("설문자가 원하는 게임의 만렙대:"+str(Q6))
        f.write("\n")
        f.write("설문자가 최근에 했거나 재밌게 했던 게임의 이름:"+Q7)
        f.write("\n")
        f.write("설문자가 7번 질문의 게임 리뷰:"+Q8)
        f.write("\n")
        f.write("설문자가 마지막으로 게임을 했던 날짜:"+str(Q9))
        f.write("\n")
        f.write("설문자가 희망하는 게임 이벤트의 종류:"+Q10)
        f.write("\n")
        f.write("설문자가 희망하는 게임 이벤트의 기타 종류:"+Q10_1)
        f.write("\n")
        f.write("설문자가 희망하는 게임 이벤트의 시작 시간:"+str(Q11))
        f.write("\n")
        f.write("우리가 생각하는 요즘 트렌드가 맞는지 확인하기 위한 설문자의 답변:"+Q12)

        f.close()






