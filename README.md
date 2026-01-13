# AI-for-marketing

一個基於 AI 的智慧行銷助手，透過 OpenAI GPT 模型與網路搜尋技術，協助分析產品市場定位並尋找潛在客戶。

## 📋 專案簡介

本專案是一個整合 AI 對話、網路搜尋與資料彙整的行銷分析工具。主要功能包括：

1. **產品分析**：分析產品描述，找出市場定位與競爭優勢
2. **潛在客戶尋找**：透過展覽、活動等場合，找出可能接觸到目標客戶的地點
3. **銷售策略分析**：針對特定廠商，提供客製化的銷售建議

## 🚀 功能特色

- 🤖 **AI 對話系統**：使用 OpenAI GPT-4o-mini 進行智慧對話與分析
- 🔍 **智慧搜尋**：自動產生搜尋查詢，從網路資源中擷取相關資訊
- 📊 **資料彙整**：將多個網路來源的資訊整合成結構化報告
- 📝 **對話記錄**：自動記錄所有對話內容到日誌檔案
- 🎯 **任務導向搜尋**：基於任務目標自動產生搜尋策略

## 📁 專案結構

```
AI-for-marketing/
├── gen.py                 # 主程式，執行產品分析與客戶尋找流程
├── data_Compilation.py    # 任務導向搜尋與報告生成模組
├── search.py              # Google 搜尋功能模組
├── product.txt            # 產品描述輸入檔案
├── requirements.txt       # Python 套件依賴
├── .env                   # 環境變數設定檔（需自行建立）
└── log/                   # 日誌檔案目錄
```

## 🛠️ 安裝與設定

### 1. 環境需求

- Python 3.9 或更高版本

### 2. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 3. 設定環境變數

在專案根目錄建立 `.env` 檔案，並加入以下內容：

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. 準備產品描述

編輯 `product.txt` 檔案，輸入您的產品描述。範例格式可參考現有的 `product.txt` 檔案。

## 📖 使用方式

### 執行主程式

```bash
python gen.py
```

### 使用流程

1. **第一階段：產品分析**
   - 程式會自動讀取 `product.txt` 中的產品描述
   - AI 會分析產品並從網路資源中找出市場定位
   - 您可以補充更多市場資訊，或輸入 `exit` 進入下一階段

2. **第二階段：潛在客戶尋找**
   - AI 會分析哪些展覽、活動適合推廣您的產品
   - 分析不同展覽的優勢與契合度
   - 選擇特定展覽後，AI 會列出可能出現在該活動的潛在廠商
   - 選擇特定廠商後，AI 會提供針對該廠商的銷售策略建議

## 🔧 核心模組說明

### `gen.py`
主程式檔案，包含：
- `chat_with_gpt()`: 與 GPT 模型對話
- `mission_search_query()`: 根據任務產生搜尋查詢
- `summarize_report()`: 生成總結報告
- 主要執行流程：產品分析 → 客戶尋找 → 銷售策略分析

### `data_Compilation.py`
資料彙整模組，包含：
- `mission_search_query()`: 根據任務產生搜尋查詢語句
- `fetch_page_text()`: 從網頁擷取文字內容
- `summarize_report()`: 將多個資料來源彙整成報告
- `mission_based_search_and_report()`: 完整的任務導向搜尋與報告生成流程

### `search.py`
搜尋功能模組：
- `get_info()`: 使用 Google 搜尋取得相關網址

## 📝 日誌系統

程式會自動將所有對話記錄到 `log/` 目錄下，檔案名稱格式為 `YYYY-MM-DD.log`。

## 🔑 主要依賴套件

- `openai==0.28.0`: OpenAI API 客戶端
- `googlesearch-python==1.3.0`: Google 搜尋功能
- `beautifulsoup4==4.13.4`: 網頁解析
- `requests==2.32.4`: HTTP 請求
- `python-dotenv==1.1.1`: 環境變數管理

完整依賴清單請參考 `requirements.txt`。

## ⚠️ 注意事項

1. **API 金鑰安全**：請勿將 `.env` 檔案提交到版本控制系統
2. **搜尋限制**：Google 搜尋可能有頻率限制，程式已加入延遲機制
3. **網路連線**：程式需要網路連線以進行搜尋與 API 呼叫
4. **費用考量**：使用 OpenAI API 會產生費用，請注意使用量

## 📄 授權

本專案僅供學習與研究使用。

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request 來改善本專案。

## 📧 聯絡方式

如有問題或建議，請透過 Issue 與我們聯繫。

