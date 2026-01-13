# AI-for-marketing

An AI-powered intelligent marketing assistant that helps analyze product market positioning and find potential customers through OpenAI GPT models and web search technology.

## 📋 Project Overview

This project is a marketing analysis tool that integrates AI conversation, web search, and data compilation. Main features include:

1. **Product Analysis**: Analyze product descriptions to identify market positioning and competitive advantages
2. **Potential Customer Discovery**: Find locations where you can reach target customers through exhibitions, events, and other venues
3. **Sales Strategy Analysis**: Provide customized sales recommendations for specific vendors

## 🚀 Features

- 🤖 **AI Conversation System**: Uses OpenAI GPT-4o-mini for intelligent conversations and analysis
- 🔍 **Intelligent Search**: Automatically generates search queries to extract relevant information from web resources
- 📊 **Data Compilation**: Integrates information from multiple web sources into structured reports
- 📝 **Conversation Logging**: Automatically records all conversation content to log files
- 🎯 **Task-Oriented Search**: Automatically generates search strategies based on task objectives

## 📁 Project Structure

```
AI-for-marketing/
├── gen.py                 # Main program, executes product analysis and customer discovery workflow
├── data_Compilation.py    # Task-oriented search and report generation module
├── search.py              # Google search functionality module
├── product.txt            # Product description input file
├── requirements.txt       # Python package dependencies
├── .env                   # Environment variables configuration file (create manually)
└── log/                   # Log files directory
```

## 🛠️ Installation & Setup

### 1. Requirements

- Python 3.9 or higher

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory and add the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Prepare Product Description

Edit the `product.txt` file and enter your product description. You can refer to the existing `product.txt` file for example format.

## 📖 Usage

### Run Main Program

```bash
python gen.py
```

### Workflow

1. **Phase 1: Product Analysis**
   - The program automatically reads the product description from `product.txt`
   - AI analyzes the product and finds market positioning from web resources
   - You can supplement more market information, or type `exit` to proceed to the next phase

2. **Phase 2: Potential Customer Discovery**
   - AI analyzes which exhibitions and events are suitable for promoting your product
   - Analyzes the advantages and fit of different exhibitions
   - After selecting a specific exhibition, AI lists potential vendors that may appear at the event
   - After selecting a specific vendor, AI provides sales strategy recommendations tailored to that vendor

## 🔧 Core Modules

### `gen.py`
Main program file, includes:
- `chat_with_gpt()`: Converses with GPT model
- `mission_search_query()`: Generates search queries based on tasks
- `summarize_report()`: Generates summary reports
- Main execution flow: Product Analysis → Customer Discovery → Sales Strategy Analysis

### `data_Compilation.py`
Data compilation module, includes:
- `mission_search_query()`: Generates search query statements based on tasks
- `fetch_page_text()`: Extracts text content from web pages
- `summarize_report()`: Compiles multiple data sources into reports
- `mission_based_search_and_report()`: Complete task-oriented search and report generation workflow

### `search.py`
Search functionality module:
- `get_info()`: Uses Google search to obtain relevant URLs

## 📝 Logging System

The program automatically records all conversations to the `log/` directory, with file names in the format `YYYY-MM-DD.log`.

## 🔑 Key Dependencies

- `openai==0.28.0`: OpenAI API client
- `googlesearch-python==1.3.0`: Google search functionality
- `beautifulsoup4==4.13.4`: Web page parsing
- `requests==2.32.4`: HTTP requests
- `python-dotenv==1.1.1`: Environment variable management

For the complete dependency list, please refer to `requirements.txt`.

## ⚠️ Notes

1. **API Key Security**: Do not commit the `.env` file to version control systems
2. **Search Limitations**: Google search may have rate limits; the program includes delay mechanisms
3. **Network Connection**: The program requires network connection for search and API calls
4. **Cost Considerations**: Using OpenAI API will incur costs; please monitor usage

## 📄 License

This project is for learning and research purposes only.

## 🤝 Contributing

Contributions via Issues or Pull Requests are welcome to improve this project.

## 📧 Contact

For questions or suggestions, please contact us through Issues.
