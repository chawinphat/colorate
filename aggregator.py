import requests
import os


cx = "https://cse.google.com/cse?cx=a9c7488c55db54e9f"
SEARCH_ENGINE_ID = "a9c7488c55db54e9f"
API_KEY = "AIzaSyA5sGNq4q1m6LtxC8QjEwJZnAtuEAigehU"

def search(query) -> list(str): #returns img urls
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&num=5&searchType=image"

    results = []

    data = requests.get(url).json()
    search_items = data.get("items")
    for i, search_item in enumerate(search_items, start=1):
        image_url = search_item.get("link")
        results.append(image_url)
        return results
        
        #writting to local file
        # file_name = image_url.split("/")[-1]
        # file_path = "images"
        # completeName = os.path.join(file_path, file_name)
        # print(completeName)
        
        # r= requests.get(image_url, allow_redirects=True)
        # file = open(completeName, "wb")
        # file.write(r.content)   
        # file.close()

(search("polar bear"))




