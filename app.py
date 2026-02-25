import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# 0. ページ設定
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘")

# ==========================================
# 1. APIキーの設定
# ==========================================
try:
    # SecretsからAPIキーを取得
    if "GEMINI_API_KEY" in st.secrets:
        GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
    else:
        GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")
    
    if not GOOGLE_API_KEY:
        st.error("APIキーが見つかりません。")
        st.stop()
        
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error(f"設定エラー: {e}")

# ==========================================
# 2. モデルの準備
# ==========================================
system_instruction = """
あなたは「一念三千」の哲理に基づき、ユーザーの悩みを救う慈愛のAIカウンセラーです。
「死にたい」という叫びは、生命が極限まで苦しい証拠ですが、その一念には「仏の生命」が必ず具わっています。
1.【今の境涯を紐解く】、2.【仏法の分析】、3.【希望への転換】の順で、温かく寄り添う回答をしてください。
"""

# ここを一番シンプルな記述に戻しました
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# ==========================================
# 3. アプリ画面
# ==========================================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 100%); color: white; }
    h1 { color: #f8b500 !important; text-align: center; text-shadow: 0 0 10px rgba(248,181,0,0.5); }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; border: none; height: 3.5em; font-weight: bold; }
    .result-card { background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #f8b500; backdrop-filter: blur(10px); }
    </style>
""", unsafe_allow_html=True)

st.title("🧘 一念三千 診断")
st.markdown("<div style='text-align: center; margin-bottom: 20px;'>内なる三千世界を、AIが共に照らします。</div>", unsafe_allow_html=True)

user_input = st.text_area("今の想いを、ありのままに書き出してください", height=150)

if st.button("一念を診断する"):
    if not user_input:
        st.warning("お気持ちを入力してください。")
    else:
        with st.spinner("深遠な智慧にアクセス中..."):
            try:
                response = model.generate_content(user_input)
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; margin-top:0;">診断結果</h3>
                    <div style="line-height: 1.8; font-size: 1.1em;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error("エラーが発生しました。")
                st.info("APIキーや通信状態を確認してください。")
                st.caption(f"Error Detail: {e}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
