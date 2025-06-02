# TRPG Web App (Streamlit + Supabase + WebSocket 기반)

## 📁 파일 설명

- `streamlit_app.py`: 앱의 메인 진입점입니다.
- `character_creator.py`: 캐릭터 생성 페이지. Supabase와 연동되어 캐릭터 저장.
- `board.py`: 게임 보드 페이지. 채팅, 주사위, 격자 기능을 포함할 예정.

## 🔧 변경해야 할 부분

1. **Supabase 설정**
   - `character_creator.py` 내 다음 줄을 본인의 Supabase 정보로 수정:

     ```python
     SUPABASE_URL = "https://YOUR_PROJECT_ID.supabase.co"
     SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"
     ```

2. **Supabase Storage**
   - `characters`라는 이름의 Storage Bucket이 존재해야 합니다.

3. **Supabase 테이블**
   - `characters`라는 테이블이 존재해야 하며 다음과 같은 스키마를 가집니다:

     - `id`: UUID (Primary Key)
     - `name`: text
     - `image_url`: text
     - `stats`: text
     - `delete_password`: text

## 🚀 실행 방법

```bash
streamlit run streamlit_app.py
```