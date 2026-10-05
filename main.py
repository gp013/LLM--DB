from src.project1.doc import DocumentProcessor
from src.project1.llm import LanguageModel
from src.project1.jsonparser import JsonParser
import os

def main():
    DocumentProcessor.proccess_documents()


    # Runs through all the articles in the Articles folder and processes them into JSON files

    num = 0

    for filename in os.listdir("Articles"):
        num += 1

        if filename.endswith(".txt"):

            filepath = os.path.join("Articles", filename)
        
            print("Processing:", filename)
        
            response = LanguageModel.article_to_json(filepath)
            JsonParser.create_json(response, num)

    # Runs through all the JSON files in the Json folder and adds them to the SQLite database

    for filename in os.listdir("Json"):
        if filename.endswith(".json"):
        
            json_file_path = os.path.join("Json", filename)
            JsonParser.json_to_sqlite(json_file_path)

        
if __name__ == "__main__":
    main()

       
