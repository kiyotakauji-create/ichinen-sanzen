import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
try:
    # SecretsからAPIキーを取得
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
    # 最新の通信ルール(v1)を指定して設定
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error("APIキーの設定を確認してください。")

# AIへの深い命令
system_instruction = """
あなたは「一念三千」の哲理に精通した、慈愛に満ちたAIカウンセラーです。
ユーザーの「死にたい」という苦しみも、仏法では「煩悩即菩提」として大きな光に変えられると説きます。
1.【今の境涯を紐解く】: 心境に寄り添い、今の十界を解説。
2.【一念三千の視点】: 苦しみがどう変化しうるか分析。
3.【希望への転換】: 温かな一歩を提案。
"""

# モデルの準備（models/ をつけることで、古いbeta版との衝突を避けます）
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash"
)

# ==========================================
# 2. デザイン（癒やしの和モダン空間）
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
                # 命令文とユーザーの想いを結合して送信
                response = model.generate_content(system_instruction + "\n\nユーザーの悩み：" + user_input)
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; margin-top:0;">診断結果</h3>
                    <div style="line-height: 1.8; font-size: 1.1em;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("AIが回答を生成中です。もう一度ボタンを押してみてください。")
                st.caption(f"Debug Info: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
