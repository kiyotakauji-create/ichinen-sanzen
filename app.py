import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# ★Streamlit CloudのSecretsからAPIキーを読み込みます
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GOOGLE_API_KEY = "YOUR_LOCAL_KEY_HERE" # ローカルテスト用

genai.configure(api_key=GOOGLE_API_KEY)

# システムプロンプト
system_instruction = """
あなたは「一念三千」の深遠な哲理に基づき、ユーザーの悩みを救うAIメンタルカウンセラーです。
以下の3ステップで診断・回答してください。
1.【生命境涯の特定（十界）】: 現在の心が十界のどこにあるか判定し、優しく解説。
2.【一念三千の分析（三世間）】: 五陰世間、衆生世間、国土世間の観点から分析。
3.【境地転換のアドバイス（煩悩即菩提）】: 苦しみをエネルギーに変える具体的なアクションを提案。
"""

# モデルの準備（最新の安定した呼び出し方に変更しました）
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
)

# ==========================================
# 2. デザイン（CSS）
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
        font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
    }
    h1 { color: #f8b500 !important; text-align: center; }
    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid #f8b500 !important; }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; }
    .result-card { background-color: rgba(0, 0, 0, 0.6); padding: 20px; border-radius: 15px; border-left: 5px solid #f8b500; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")

st.markdown("<div style='text-align: center; margin-bottom: 30px; opacity: 0.8;'>今の心境を入力してください。三千世界を紐解きます。</div>", unsafe_allow_html=True)

user_input = st.text_area("今の心境を入力", height=120, placeholder="例：仕事がうまくいかず、焦っている...")

if st.button("一念を診断する"):
    if not user_input:
        st.warning("心境を入力してください。")
    else:
        with st.spinner("曼荼羅を解析中..."):
            try:
                # 修正ポイント：明示的にコンテンツを生成
                response = model.generate_content(
                    system_instruction + "\n\n【ユーザーの悩み】\n" + user_input
                )
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; border-bottom:1px solid #555; padding-bottom:10px;">診断結果</h3>
                    <div style="line-height: 1.8;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                # エラーが出た場合、詳細を表示して原因を特定しやすくします
                st.error(f"診断中にエラーが発生しました。設定を確認してください。")
                st.caption(f"Debug Info: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
