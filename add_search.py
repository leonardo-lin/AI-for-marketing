import openai
import os
from dotenv import load_dotenv
import logging
from datetime import datetime
import requests

# 載入 .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 設定 log（依照日期命名）
log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def get_web_search_summary(query: str) -> str:
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_redirect": 1,
            "no_html": 1
        }
        response = requests.get(url, params=params)
        data = response.json()

        # 嘗試抓摘要
        abstract = data.get("AbstractText", "")
        if abstract:
            return f"[🔎 來自網路摘要] {abstract}"

        # 嘗試 fallback 到 RelatedTopics 第一筆
        related = data.get("RelatedTopics", [])
        for item in related:
            if isinstance(item, dict) and "Text" in item:
                return f"[🔎 來自相關主題] {item['Text']}"

        return "[🔎 沒有找到明確的網路摘要]"
    except Exception as e:
        return f"[❌ 查詢失敗] {e}"

# GPT 回覆函數
def chat_with_gpt(prompt: str, model: str = "gpt-4o-mini"):
    # 🕸️ 檢查是否需要連網查詢
    need_search = any(keyword in prompt.lower() for keyword in ["天氣", "新聞", "現在", "股價", "匯率", "查詢", "搜尋", "最近"])

    web_info = ""
    if need_search:
        # print("inside")
        web_info = get_web_search_summary(prompt)
        print(web_info)

    try:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        if web_info:
            messages.append({"role": "user", "content": web_info})
        messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        reply = response["choices"][0]["message"]["content"].strip()

        # 記錄 log
        logging.info(f"[USER] {prompt}")
        if web_info:
            logging.info(f"[WEB]  {web_info}")
        logging.info(f"[GPT]  {reply}")
        logging.info("-" * 50)

        return reply
    except Exception as e:
        error_message = f"❌ 發生錯誤: {e}"
        logging.error(error_message)
        return error_message

# 主程式
if __name__ == "__main__":
    # user_input = input("請輸入你的問題：")
    user_input = "請問現在台灣天氣如何"
    reply = chat_with_gpt(user_input)
    print("\n🤖 GPT-4o-mini 回覆：\n" + reply)
