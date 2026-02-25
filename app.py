import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# SecretsからAPIキーを取得
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
    # 接続を安定させるための初期設定
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error("APIキーの設定を確認してください。")

# AIへの深い命令（一念三千の智慧）
system_instruction = """
あなたは「一念三千」の哲理に精通した、慈愛に満ちたAIカウンセラーです。
ユーザーの「死にたい」「消えたい」という言葉は、現在の生命状態（十界）が極限まで苦しい証拠ですが、
仏法ではその一念の中にこそ、最高に輝く「仏の生命」が必ず具わっていると説きます。
以下の構成で、ユーザーの心に灯をともすような対話を行ってください。
1.【今の境涯を紐解く】: ユーザーの心境が十界のどこにあるか寄り添いながら解説。
2.【一念三千の視点】: その苦しみがどう変化しうるか、三世間の観点から分析。
3.【希望への転換】: 煩悩即菩提（苦しみ即幸せ）への具体的な一歩を提案。
"""

# モデルの準備
# ポイント：最新の安定した「gemini-1.5-flash」を、正式な通信ルールで使用します
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# ==========================================
# 2. デザイン（和モダン・癒やしの空間）
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 100%); color: white; }
    h1 { color: #f8b500 !important; text-align: center; font-size: 2.5em; text-shadow: 0 0 10px rgba(248,181,0,0.5); }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; border: none; height: 3em; font-weight: bold; }
    .result-card { background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #f8b500; backdrop-filter: blur(10px); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")

st.markdown("<div style='text-align: center; margin-bottom: 20px;'>あなたの内なる三千世界を、AIが照らし出します。</div>", unsafe_allow_html=True)

user_input = st.text_area("今の心境を教えてください", height=150, placeholder="ここにあなたの想いを書き出してください...")

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
                # 具体的な解決策を提示
                st.error("AIとの通信に一時的な乱れがあります。")
                st.info("解決策：Google AI Studioで『新しいAPIキー』を作り直し、Secretsに貼り直してみてください。それが一番確実な方法です。")
                st.caption(f"技術詳細: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>",
