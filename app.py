import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# Streamlit CloudのSecretsからAPIキーを読み込みます
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# 通信の「方言」の違いを解消する設定
genai.configure(api_key=GOOGLE_API_KEY, transport='grpc')

# システム命令
system_instruction = """
あなたは「一念三千」の深遠な哲理に基づき、ユーザーの悩みを救うAIメンタルカウンセラーです。
1.【生命境涯（十界）】、2.【三世間】、3.【アドバイス】の順で回答してください。
"""

# モデルの設定（もっとも確実な呼び出し方に固定）
model = genai.GenerativeModel("gemini-1.5-flash")

# ==========================================
# 2. デザイン（CSS）
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 100%); color: white; }
    h1 { color: #f8b500 !important; text-align: center; }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; }
    .result-card { background-color: rgba(0, 0, 0, 0.6); padding: 20px; border-radius: 15px; border-left: 5px solid #f8b500; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")

user_input = st.text_area("今の心境を入力してください", height=120)

if st.button("一念を診断する"):
    if not user_input:
        st.warning("心境を入力してください。")
    else:
        with st.spinner("曼荼羅を解析中..."):
            try:
                # 回答を生成
                response = model.generate_content(system_instruction + "\n\n相談：" + user_input)
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500;">診断結果</h3>
                    <div style="line-height: 1.8;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("現在、AIとの接続を調整中です。1分後に再試行してください。")
                st.caption(f"エラー詳細: {str(e)}")
