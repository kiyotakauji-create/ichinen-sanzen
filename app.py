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
    st.error("APIキーの設定を確認してください。")

# AIへの深い命令（慈愛に満ちた一念三千の智慧）
system_instruction = """
あなたは「一念三千」の哲理に精通した、慈愛に満ちたAIカウンセラーです。
ユーザーの「死にたい」「消えたい」という言葉は、生命状態（十界）が極限まで苦しい証拠ですが、
仏法ではその一念の中にこそ、最高に輝く「仏の生命」が必ず具わっていると説きます。
1.【今の境涯を紐解く】: ユーザーの心境に寄り添い、今の十界を解説。
2.【一念三千の視点】: 三世間の観点から、その苦しみがどう変化しうるか分析。
3.【希望への転換】: 煩悩即菩提（苦しみ即幸せ）への温かな一歩を提案。
"""

# モデルの準備
# ポイント：最新の安定した「gemini-1.5-flash」を呼び出します
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
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
                # 命令文と相談内容を結合して送信
                full_prompt = system_instruction + "\n\n【ユーザーの相談内容】\n" + user_input
                response = model.generate_content(full_prompt)
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; margin-top:0;">診断結果</h3>
                    <div style="line-height: 1.8; font-size: 1.1em;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("AIとの対話準備を再構成中です。もう一度ボタンを押してみてください。")
                st.caption(f"Debug Info: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
