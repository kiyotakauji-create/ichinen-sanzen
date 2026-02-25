import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 設定エリア
# ==========================================
# ★ここにAI Studioで取得したAPIキー(AIza...で始まるやつ)を入れてください
# GitHub公開用：Streamlitの設定から読み込むように変更
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

# システムプロンプト
system_instruction = """
あなたは「一念三千」の深遠な哲理に基づき、ユーザーの悩みを救うAIメンタルカウンセラーです。
以下の3ステップで診断・回答してください。
1.【生命境涯の特定（十界）】: 現在の心が十界のどこにあるか判定し、優しく解説。
2.【一念三千の分析（三世間）】: 五陰世間、衆生世間、国土世間の観点から分析。
3.【境地転換のアドバイス（煩悩即菩提）】: 苦しみをエネルギーに変える具体的なアクションを提案。
"""

# モデル設定
model = genai.GenerativeModel("gemini-pro")

# ==========================================
# 2. デザイン（CSS）の魔法をかけるエリア
# ==========================================
st.set_page_config(page_title="一念三千 診断", page_icon="🧘", layout="centered")

# カスタムCSS（ここでおしゃれにしています）
st.markdown("""
    <style>
    /* 全体の背景：深い藍色から黒へのグラデーション（宇宙・深海をイメージ） */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
        font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
    }
    
    /* タイトル：金色で輝かせる */
    h1 {
        color: #f8b500 !important;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
        font-weight: bold;
        padding-bottom: 20px;
        border-bottom: 1px solid rgba(248, 181, 0, 0.3);
    }
    
    /* 入力ボックス：半透明の和紙風 */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid #f8b500 !important;
        border-radius: 10px;
    }
    
    /* ボタン：朱色（鳥居の色） */
    .stButton>button {
        background-color: #d3381c !important;
        color: white !important;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff5e3a !important;
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(211, 56, 28, 0.7);
    }
    
    /* 結果表示エリア：カード風 */
    .result-card {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #f8b500;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. アプリ画面
# ==========================================
st.title("🧘 一念三千 診断")

st.markdown("""
<div style='text-align: center; margin-bottom: 30px; opacity: 0.8;'>
今の「一念（こころ）」を入力してください。<br>
三千世界があなたの心にどう映っているか、紐解きます。
</div>
""", unsafe_allow_html=True)

# 入力エリア
user_input = st.text_area("今の心境を入力", height=120, placeholder="例：先が見えなくて不安だ。誰かと比べて焦ってしまう…。")

# 診断ボタン
if st.button("一念を診断する"):
    if not user_input:
        st.warning("心境を入力してください。")
    else:
        with st.spinner("曼荼羅を解析中..."):
            try:
                # AIに問い合わせ
                full_prompt = system_instruction + "\n\n【ユーザーの悩み】\n" + user_input
                response = model.generate_content(full_prompt)
                
                # 結果の表示（特製カードデザインの中に表示）
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#f8b500; border-bottom:1px solid #555; padding-bottom:10px;">診断結果</h3>
                    <div style="line-height: 1.8;">
                        {response.text.replace(chr(10), "<br>")}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

# フッター
st.markdown("<div style='text-align: center; margin-top: 50px; color: #888; font-size: 0.8em;'>一念三千 診断所</div>", unsafe_allow_html=True)
