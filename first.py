import openai
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# 1. 載入 .env 檔
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 2. 設定 log 檔案（依照日期命名）
log_filename = "log\\"+datetime.now().strftime("%Y-%m-%d") + ".log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def chat_with_gpt(prompt: str, model: str = "gpt-4o-mini"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        reply = response["choices"][0]["message"]["content"].strip()

        # 3. 紀錄對話到 log
        logging.info(f"[USER] {prompt}")
        logging.info(f"[GPT]  {reply}")
        return reply
    except Exception as e:
        error_message = f"❌ 發生錯誤: {e}"
        logging.error(error_message)
        return error_message

if __name__ == "__main__":
    user_input = input("請輸入你的問題：")
    reply = chat_with_gpt(user_input)
    print("\n🤖 GPT-4o-mini 回覆：\n" + reply)
