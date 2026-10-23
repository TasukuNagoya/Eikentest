import random
import streamlit as st

# ページの設定
st.set_page_config(
    page_title="英検1級 単語＆例文ジェネレーター", page_icon="📚", layout="wide"
)

st.title("📚 英検1級 トレンド単語・例文ジェネレーター")
st.markdown(
    "英検1級レベルの高度な頻出・トレンド語彙をランダムに抽出し、実用的な例文とともに対話形式で表示するアプリです。"
)


# 英検1級の頻出・トレンド単語データを取得する関数
@st.cache_data
def get_eiken_words():
  """厳選された英検1級レベルの高度な語彙データプール"""
  words_data = [
      {
          "word": "Ubiquitous",
          "meaning": "至る所にある、偏在する",
          "sentence": (
              "Smartphones have become ubiquitous in modern daily life."
          ),
          "translation": (
              "スマートフォンは現代の日常生活において至る所に見られるようになった。"
          ),
      },
      {
          "word": "Meticulous",
          "meaning": "細部にわたる、非常に慎重な",
          "sentence": (
              "The architect paid meticulous attention to every detail of the"
              " building."
          ),
          "translation": (
              "その建築家は建物のあらゆる細部に細心の注意を払った。"
          ),
      },
      {
          "word": "Pragmatic",
          "meaning": "実用的な、現実的な",
          "sentence": (
              "We need to adopt a pragmatic approach to solve this economic"
              " issue."
          ),
          "translation": (
              "この経済問題を解決するために、私たちは現実的なアプローチを採用する必要がある。"
          ),
      },
      {
          "word": "Candid",
          "meaning": "率直な、隠し立てのない",
          "sentence": (
              "She gave a candid interview about her struggles during the"
              " startup phase."
          ),
          "translation": (
              "彼女は立ち上げ期における苦労について率直なインタビューに応じた。"
          ),
      },
      {
          "word": "Ambiguous",
          "meaning": "曖昧な、多義的な",
          "sentence": (
              "The instructions provided by the manager were somewhat"
              " ambiguous."
          ),
          "translation": "マネージャーから提供された指示は、やや曖昧だった。",
      },
      {
          "word": "Vindicate",
          "meaning": "無罪を証明する、正当性を立証する",
          "sentence": (
              "The new DNA evidence helped to vindicate the wrongly accused"
              " man."
          ),
          "translation": (
              "新しいDNA証拠が、不当に告発された男の無罪を証明する助けとなった。"
          ),
      },
      {
          "word": "Scrutinize",
          "meaning": "細かく調べる、吟味する",
          "sentence": (
              "Auditors will scrutinize the company's financial records"
              " thoroughly."
          ),
          "translation": "監査人は会社の財務記録を徹底的に吟味する予定だ。",
      },
      {
          "word": "Alleviate",
          "meaning": "（苦痛などを）軽減する、和らげる",
          "sentence": (
              "New medication was prescribed to alleviate his chronic pain."
          ),
          "translation": "彼の慢性的な痛みを和らげるために新しい薬が処方された。",
      },
      {
          "word": "Deteriorate",
          "meaning": "悪化する、低下する",
          "sentence": (
              "Diplomatic relations between the two nations began to deteriorate"
              " rapidly."
          ),
          "translation": "両国間の外交関係は急速に悪化し始めた。",
      },
      {
          "word": "Resilient",
          "meaning": "回復力のある、弾力性のある",
          "sentence": (
              "The local community proved to be remarkably resilient after the"
              " natural disaster."
          ),
          "translation": (
              "地域社会は自然災害の後、驚くほど高い回復力を見せた。"
          ),
      },
      {
          "word": "Eradicate",
          "meaning": "根絶する、撲滅する",
          "sentence": (
              "Global efforts are underway to eradicate infectious diseases"
              " completely."
          ),
          "translation": "感染症を完全に根絶するための世界的努力が進行中である。",
      },
      {
          "word": "Innovative",
          "meaning": "革新的な、画期的な",
          "sentence": (
              "The company introduced an innovative solution to reduce carbon"
              " emissions."
          ),
          "translation": (
              "その会社は二酸化炭素排出量を削減するための画期的な解決策を導入した。"
          ),
      },
      {
          "word": "Substantiate",
          "meaning": "立証する、裏付ける",
          "sentence": (
              "There is no scientific evidence to substantiate his bold claim."
          ),
          "translation": "彼の大胆な主張を裏付ける科学的証拠はない。",
      },
      {
          "word": "Transient",
          "meaning": "束の間の、一時的な",
          "sentence": (
              "A rainbow is a transient phenomenon that disappears quickly."
          ),
          "translation": "虹はすぐに消えてしまう束の間の現象だ。",
      },
      {
          "word": "Gullible",
          "meaning": "だましやすい、信じやすい",
          "sentence": (
              "Don't be so gullible as to believe every online advertisement."
          ),
          "translation": (
              "ネットの広告をなんでも信じるほど騙されやすくなってはいけない。"
          ),
      },
  ]
  return words_data


# メイン処理
if st.button("🔄 新しい英検1級単語を10件シャッフル・読み込む", type="primary"):
  st.rerun()

# データの取得とランダムサンプリング
all_words = get_eiken_words()
word_list = random.sample(all_words, min(10, len(all_words)))

st.success(f"厳選された英検1級トレンド単語 {len(word_list)}件 を読み込みました！")

# 1つずつカード形式で表示
for i, item in enumerate(word_list, 1):
  with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    with col1:
      st.markdown(f"### **{i}. {item['word']}**")
      st.caption(f"意味: {item['meaning']}")
    with col2:
      st.markdown(f"**📝 例文:** `{item['sentence']}`")
      st.markdown(f"**🇯🇵 和訳:** {item['translation']}")

# フッター
st.markdown("---")
st.markdown("💡 *Tip: ボタンを押すたびに異なる単語セットが表示されます。*")