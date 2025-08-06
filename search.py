# import googlesearch
# googlesearch.get_useragent()
from googlesearch import search
def get_info(query: str, num_results = 2):
    # def get_info(query: str, num_results=2):
    try:
        items = search(query, num_results=num_results, advanced=True)
        return [item.url for item in items]
    except Exception as e:
        return [f"❌ 搜尋錯誤: {e}"]
if __name__ == "__main__":
    get_info('Lanchain')


