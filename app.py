import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# Streamlit CloudのSecretsからAPIキーを読み込みます
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error("APIキーが設定されていません。Secretsの設定を確認してください。")

# システム命令
system_instruction = """
あなたは「一念三千」の深遠な哲理に基づき、ユーザーの悩みを救うAIメンタルカウンセラーです。
以下の3ステップで誠実に回答してください。
1.【生命境涯（十界）】: 現在の心が十界のどこにあるか判定し、解説。
2.【一念三千の分析】: 仏法の観点から現状を分析。
3.【境地転換のアドバイス】: 前向きなアクションを提案。
"""

# モデルの設定（もっとも確実な呼び出し方に固定）
# ポイント：models/ をつけることで、古い通信ルール(v1beta)との衝突を避けます
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# ==========================================
# 2. デザイン（CSS）
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 100%); color: white; }
    h1 { color: #f8b500 !important; text-align: center; }
    .stButton>button { background-color: #d3381c !important; color: white !important; width: 100%; border-radius: 20px; border: none; }
    .result-card { background-color: rgba(0, 0, 0, 0.6); padding: 20px; border-radius: 15px; border-left: 5px solid #f8b500; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")

user_input = st.text_area("今の心境を入力してください", height=120, placeholder="例：死にそうです！仕事が本当につらい...")

if st.button("一念を診断する"):
    if not user_input:
        st.warning("心境を入力してください。")
    else:
        with st.spinner("曼荼羅を解析中..."):
            try:
                # 回答を生成（システム命令を結合）
                response = model.generate_content(system_instruction + "\n\nユーザーの悩み：" + user_input)
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500;">診断結果</h3>
                    <div style="line-height: 1.8;">{response.text.replace(chr(10), "<br>")}</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                # もしエラーが出ても、原因がわかるように詳細を表示します
                st.error("AIとの接続でエラーが発生しました。")
                st.caption(f"エラー詳細: {str(e)}")

st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
