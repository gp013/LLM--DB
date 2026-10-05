import requests
from bs4 import BeautifulSoup

class DocumentProcessor:
    """
    process_documents reads URLS from text file named "links.txt", it scrapes the text from the articles and then saves them to a new text file in the "Articles" directory.
    """
    def proccess_documents():

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.9"
        }
        num = 0
        with open("links.txt", "r") as file:
    
            for line in file:
                num += 1
                url = line.strip()
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, "lxml")
                article_body = soup.find_all("p")
                text = "\n".join(p.get_text(strip=True) for p in article_body)
                with open("Articles/article" + str(num) + ".txt", "w", encoding="utf-8") as f:
                    f.write(text)