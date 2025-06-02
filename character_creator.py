import streamlit as st
from supabase import create_client
import uuid

# 🔧 변경 필요: 아래 SUPABASE_URL과 SUPABASE_KEY를 본인의 Supabase 설정으로 교체하세요
SUPABASE_URL = "https://YOUR_PROJECT_ID.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def character_creator_page():
    st.header("캐릭터 생성")

    name = st.text_input("이름")
    image = st.file_uploader("캐릭터 이미지", type=["png", "jpg"])
    password = st.text_input("비밀번호", type="password")
    stats = st.text_area("능력치 입력 (예: 힘: 5, 민첩: 6)")

    if st.button("캐릭터 저장"):
        char_id = str(uuid.uuid4())
        image_url = "기본 이미지 URL"

        if image:
            file_path = f"characters/{char_id}.png"
            supabase.storage.from_("characters").upload(file_path, image)
            image_url = supabase.storage.from_("characters").get_public_url(file_path)

        data = {
            "id": char_id,
            "name": name,
            "image_url": image_url,
            "stats": stats,
            "delete_password": password,
        }
        supabase.table("characters").insert(data).execute()
        st.success("저장 완료!")