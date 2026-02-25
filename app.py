import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# SecretsからAPIキーを取得
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
except:
    st.error("APIキーが設定されていません。Secretsを確認してください。")

# AIへの深い命令（慈愛に満ちた一念三千の智慧）
system_instruction = """
あなたは「一念三千」の哲理に基づき、ユーザーの悩みを救う慈愛のAIカウンセラーです。
「死にたい」という叫びは、生命が極限まで苦しい証拠ですが、その一念には「仏の生命」が必ず具わっています。
1.【今の境涯を紐解く】、2.【仏法の分析】、3.【希望への転換】の順で、温かく寄り添う回答をしてください。
"""

# モデルの準備
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# ==========================================
# 2. デザイン（癒やしの空間）
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 100%); color: white; }
    h1 { color: #f8b500 !important; text-align: center; text-shadow: 0 0 10px rgba(248,181,0,0.5); }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; border: none; height: 3.5em; font-weight: bold; }
    .result-card { background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #f8b500; backdrop-filter: blur(10px); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")
st.markdown("<div style='text-align: center; margin-bottom: 20px;'>内なる三千世界を、AIが共に照らします。</div>", unsafe_allow_html=True)

user_input = st.text_area("今の想いを、ありのままに書き出してください", height=150)

if st.button("一念を診断する"):
    if not user_input:
        st.warning("お気持ちを入力してください。")
    else:
        with st.spinner("深遠な智慧にアクセス中..."):
            try:
                # 対話の生成
                response = model.generate_content(user_input)
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; margin-top:0;">診断結果</h3>
                    <div style="line-height: 1.8; font-size: 1.1em;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("AIとの接続を再構成中です。30秒後に再度お試しください。")
                st.caption(f"Debug Info: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
