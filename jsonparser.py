import json
import sqlite3


class JsonParser:

    """
    create_json takes in a string representation of a JSON object and a number, and writes the JSON object to a file named "j{num}.json" in the "Json" directory. The function opens the file in write mode with UTF-8 encoding and writes the JSON string to the file.
    """
    def create_json(response_text, num):
        
        with open("Json/j" + str(num) + ".json", "w", encoding="utf-8") as json_file:
            json_file.write(response_text)

    """
    json_to_sqlite takes in the path to a JSON file, reads the contents of the file, and inserts the data into an SQLite database named "espn.db". The function creates a table named "articles", with columns for id, players, teams, sport, and summary. It then inserts the data from the JSON file into the table.
    """
    def json_to_sqlite(json_file_path):
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            data = {}
            
            data = json.load(json_file)
            print("Adding JSON file to SQLite database:", json_file_path)
            

        con = sqlite3.connect("espn.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS articles(id INTEGER PRIMARY KEY, players TEXT, teams TEXT, sport TEXT, summary TEXT)")
        cursor.execute("INSERT INTO articles (players, teams, sport, summary) VALUES (?, ?, ?, ?)",((json.dumps(data['players'])), (json.dumps(data['teams'])), data['sport'], ((data['summary']))))
        con.commit()
       

    
    




