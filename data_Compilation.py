import openai
import requests
from bs4 import BeautifulSoup
import search
# from googlesearch import search
import os
from dotenv import load_dotenv
# 1. 載入 .env 檔
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# ✅ 設定 API 金鑰
# openai.api_key = "YOUR_API_KEY"

# ✅ 模擬上下文
conversation_history = [
    {"role": "user", "content": "我想建立一個 AI 助理幫助分析 Excel 資料"},
]

# ✅ 步驟 1：根據任務產生搜尋查詢
def mission_search_query(mission, model="gpt-4o-mini"):
    try:
        prompt_messages = [
            {
                "role": "system",
                "content": f"先根據使用者的內容，請判斷輸入哪些query可以搜尋到能幫助完成任務的資訊，並產生數個具體的搜尋查詢語句[\"Query1\",\"Query2\"...]，不要解釋，只輸出 Query 本身，用中括弧包圍成list格式。"
            },
            {
                "role": "user",
                "content":f"你的任務是{mission}，請輸出Query"
            }
        ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=prompt_messages,
            temperature=0.5,
            max_tokens=100
        )
        return eval(response["choices"][0]["message"]["content"].strip())
    except Exception as e:
        return f"❌ 發生錯誤: {e}"

# ✅ 步驟 2：Google 搜尋
# def get_info(query: str, num_results=2):
#     try:
#         items = search(query, num_results=num_results, advanced=True)
#         return [item.url for item in items]
#     except Exception as e:
#         return [f"❌ 搜尋錯誤: {e}"]

# ✅ 步驟 3：抓取網頁文字內容
def fetch_page_text(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        # 移除 script, style
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines[:150])  # 最多抓前 200 行，避免太長
    except Exception as e:
        return f"[讀取失敗: {e}]"

# ✅ 步驟 4：LLM 生成彙整報告
def summarize_report(mission, texts, model="gpt-4o-mini", max_chars=60000):
    prompt_prefix = f"""你是一個知識彙整助手。使用者的任務是：{mission}
以下是從不同網頁擷取的資訊段落，你需要將其綜合整理成一份清晰、條理分明的報告：

{"-"*60}
""" + "\n\n".join([f"【資料 {i+1}】\n{text}" for i, text in enumerate(texts)])

    combined = ""
    current_len = len(prompt_prefix)
    for i, text in enumerate(texts):
        entry = f"【資料 {i+1}】\n{text}\n\n"
        if current_len + len(entry) > max_chars:
            break
        combined += entry
        current_len += len(entry)

    prompt = prompt_prefix + combined
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800
    )
    return response["choices"][0]["message"]["content"].strip()

# ✅ 主流程
def mission_based_search_and_report(mission: str):
    print(f"🎯 任務目標：{mission}\n")

    # 1. 生成查詢語句
    queries = mission_search_query(mission)
    if isinstance(queries, str): return queries
    print(f"🔍 建議查詢語句：{queries}\n")

    # 2. 搜尋每個 query 並抓取文字內容
    all_texts = []
    for q in queries:
        print(f"➡️ 搜尋：{q}")
        urls = search.get_info(q)
        for url in urls:
            print(f"  🌐 擷取：{url}")
            page_text = fetch_page_text(url)
            if not page_text.startswith("[讀取失敗"):
                all_texts.append(page_text)
            else:
                print(f"  ⚠️ {page_text}")
        print()

    # 3. 將所有內容交給 LLM 彙整報告
    if not all_texts:
        return "❌ 無法擷取任何有效資料"
    print("🧠 正在生成彙整報告...\n")
    report = summarize_report(mission, all_texts)
    return report


# ✅ 範例執行
if __name__ == "__main__":
    mission = "幫助使用者找到可能會購買AI相關產品的廠商出沒地方，你可以從展覽或活動下手"
    result = mission_based_search_and_report(mission)
    print("📄 最終彙整報告：\n")
    print(result)
