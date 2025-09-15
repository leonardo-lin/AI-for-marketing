import openai

import logging
from datetime import datetime
import search
import data_Compilation
import json
import os
from dotenv import load_dotenv
import data_Compilation
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
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]
def chat_with_gpt(prompt: str, model: str = "gpt-4o-mini"):
    
    try:
        # 加入使用者輸入到歷史
        

        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation_history,
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"].strip()

        # 加入模型回覆到歷史
        conversation_history.append({"role": "assistant", "content": reply})

        # 紀錄對話到 log
        logging.info(f"[USER] {prompt}")
        logging.info(f"[GPT]  {reply}")
        return reply
    except Exception as e:
        error_message = f"❌ 發生錯誤: {e}"
        logging.error(error_message)
        return error_message
    

def mission_search_query(mission, model="gpt-4o-mini"):
    try:
        # 加入指示系統提示
        prompt_messages = conversation_history + [
            {"role": "system", "content": "你的任務是{mission}，先根據上面與使用者的內容，請判斷輸入哪些query可以搜尋到能幫助完成任務的資訊，並產生數個具體的搜尋查詢語句[\"Query1\",\"Query2\"...]，不要解釋，只輸出 Query 本身，用中括弧包圍成list格式。"}
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=prompt_messages,
            temperature=0.5,
            max_tokens=100
        )
        query = response["choices"][0]["message"]["content"].strip()

        return query
    except Exception as e:
        return f"❌ 發生錯誤: {e}"

def summarize_report(system_prompt, model = "gpt-4o-mini"):
    
    try:
        # 加入指示系統提示
        prompt_messages = conversation_history + [
            {"role": "system", "content": system_prompt}
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=prompt_messages,
            temperature=0.5,
            max_tokens=100
        )
        query = response["choices"][0]["message"]["content"].strip()
        
        return query
    except Exception as e:
        return f"❌ 發生錯誤: {e}"

if __name__ == "__main__":
    print("第一階段: 產品分析")
    product = ''
    # user_input = input("\n請輸入你的問題：")
    with open("product.txt",'r',encoding='utf-8')as f:
        product = f.read()
    # user_input = input("請描述你的產品，越詳細越好，我來幫你分析你在市場上的定位：")
    print('產品內容'+product)
    # user_input = product
    conversation_history.append({"role": "user", "content": f'以下為我的產品描述\n{product}'})
    system_prompt = '請針對我的產品幫我從各項網路資源上找到我的優勢產品定位'
    anay = data_Compilation.mission_based_search_and_report(system_prompt+'\n'+product)
    print(anay)
    conversation_history.append({"role": "assistant", "content": f'以下為我的產品描述\n{product}'})
    # reply = chat_with_gpt(user_input)
    # print("\n🤖 GPT-4o-mini 回覆：\n" + reply)
    #需要一個RAG找資料與資料分析
    # print(generate_search_query())
    
    
    
    while True:
        #RAG 分析上一則對話
        user_input = input("你可以在這邊補充你的市場地位，或是輸入exit進入客戶尋找階段：")
        conversation_history.append({"role": "user", "content": user_input})
        # print(mission_search_query())
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 進入下一階段！")
            break
        reply = chat_with_gpt(user_input)
        print("\n🤖 GPT-4o-mini 回覆：\n" + reply)
    summary_report = summarize_report("請針對這段對話做一份針對於商品的詳情與市場定位做一份詳細的總結報告")
    # conversation_history = [{"role": "system", "content": f"以下是一份我們剛剛討論關於產品的市場定位報告\n{summary_report}\n\n現在你是一位潛在客戶開發專家，你要負責幫我分析哪邊可以幫我找到潛在客戶"}]
    conversation_history.append({"role": "system", "content": f"現在你是一位潛在客戶開發專家，你要負責幫我分析哪邊可以幫我找到潛在客戶"})
    

    
    
    print("產品分析結束，現在進入潛在客戶尋找階段")
    #先做第一個RAG找資料
    report = data_Compilation.mission_based_search_and_report(mission = f'根據使用者對於產品的描述{summary_report}\n\n請列出這樣的產品可以在甚麼樣的場合、展覽、活動找到潛在客戶')
    print(report)
    # activities_info = mission_search_query(mission='找到數個可能能找到大量客戶的展覽與活動')
    # print(activities_info)
    conversation_history.append({"role": "assistant", "content": report})

    # user_input = input("你可以在這邊補充有哪些場合可以取得客戶資料：")
    user_input = '你已經幫我找到我能推廣在哪些場合，現在請幫我分析我的產品針對這些廠商有分別有哪些優勢，越詳細越好'
    print(user_input)
    conversation_history.append({"role": "user", "content": user_input})
    response = data_Compilation.mission_based_search_and_report(user_input)
    print(response)
    conversation_history.append({"role": "assistant", "content": response})
    #mission = 找到適合的展覽與活動組合成list
    
    #分析不同展覽的優勢與契合度
    user_input = input("選擇你要尋找的展覽：") 
    user_input = f"現在我想合作的活動是{user_input}，請幫我分析有哪些潛在廠商會在該活動中出現"
    conversation_history.append({"role": "user", "content": user_input})
    response = data_Compilation.mission_based_search_and_report(user_input)
    print(response)
    conversation_history.append({"role": "assistant", "content": response})
    
    #撈取所有該展覽的廠商
    user_input = input("選取你要的廠商")
    user_input = f"現在我想合作的廠商是{user_input}，請幫我分析我要怎麼對這家廠商進行銷售"
    conversation_history.append({"role": "user", "content": user_input})
    response = data_Compilation.mission_based_search_and_report(user_input)
    print(response)
    conversation_history.append({"role": "assistant", "content": response})
    
      



