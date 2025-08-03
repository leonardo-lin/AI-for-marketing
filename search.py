# import googlesearch
# googlesearch.get_useragent()
from googlesearch import search
def get_info(query: str):
    items = search(query,num_results=2, advanced = True)
    for item in items:
        print(item)
    return items
if __name__ == "__main__":
    get_info('Lanchain')


