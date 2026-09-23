# LLM--DB
This project consists of a python pipeline that takes in links to articles (ESPN articles in this case), scrapes the text from these articles and stores them in Articles/article(num).txt file. Each article is in a different txt file. Then the articles go into the LLM/ChatGPT API with the model gpt-4o-mini. The LLM converts the articles into a JSON object with the parameters of:
        {
        "players": [],
        "teams": [],
        "sport": "",
        "summary": ""
        }
These JSON objects each go into their own JSON file under JSON/j(num).json. These JSON files are then parsed into a dictionary and then put into a sqlite3 database named espn.db. 
