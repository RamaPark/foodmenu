
import streamlit as st
import random

# 식단 데이터
lunch_options = [
    "소고기 미역국 + 쌀밥", "참치야채비빔밥", "닭가슴살 샐러드 + 고구마", "돼지고기 김치찌개 + 쌀밥",
    "낙곱새 + 쌀밥", "김치볶음밥 + 계란프라이", "오므라이스", "차돌된장찌개 + 쌀밥",
    "감자국 + 쌀밥", "참치마요덮밥", "낙지볶음 + 쌀밥", "고등어조림 + 쌀밥", "김치제육덮밥", "소고기 카레라이스"
]

dinner_options = [
    "제육볶음 + 쌀밥", "된장찌개 + 쌀밥", "고등어구이 + 쌀밥", "버섯불고기 + 쌀밥",
    "삼겹살구이 + 쌈채소", "감자탕 + 쌀밥", "닭볶음탕 + 쌀밥", "닭갈비 + 쌀밥", 
    "소불고기 + 쌀밥", "된장찌개 + 쌀밥", "돼지고기 수육 + 쌈채소", "해물순두부찌개 + 쌀밥", 
    "차돌박이 샤브샤브", "닭강정 + 쌀밥"
]

side_dishes = [
    "콩나물무침", "두부조림", "감자채볶음", "숙주나물", "무생채", "애호박볶음", "양배추샐러드",
    "오뎅볶음", "브로콜리무침", "미역줄기볶음", "버섯볶음", "깻잎절임", "장조림", "연근조림"
]

# Streamlit UI 구성
st.title("랜덤 식단 생성기")
st.write("한 주 또는 하루 식단을 랜덤으로 추천해드립니다!")

# 한 주 식단 생성 버튼
if st.button("한 주 식단 생성"):
    st.subheader("이번 주 식단")
    for day in ["월", "화", "수", "목", "금", "토", "일"]:
        lunch = random.choice(lunch_options)
        dinner = random.choice(dinner_options)
        side1 = random.choice(side_dishes)
        side2 = random.choice(side_dishes)
        st.write(f"**{day}요일**")
        st.write(f"🍱 점심: {lunch}")
        st.write(f"🍽️ 저녁: {dinner}")
        st.write(f"🥗 반찬: {side1}, {side2}")
        st.write("---")

# 하루 식단 생성 버튼
if st.button("오늘의 식단 생성"):
    st.subheader("오늘의 식단")
    lunch = random.choice(lunch_options)
    dinner = random.choice(dinner_options)
    side1 = random.choice(side_dishes)
    side2 = random.choice(side_dishes)
    st.write(f"🍱 점심: {lunch}")
    st.write(f"🍽️ 저녁: {dinner}")
    st.write(f"🥗 반찬: {side1}, {side2}")
