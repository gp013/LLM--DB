import os

from dotenv import load_dotenv

from project1.doc import DocumentProcessor
from project1.jsonparser import JsonParser
from project1.llm import LanguageModel


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    model = LanguageModel(api_key)

    DocumentProcessor.proccess_documents()

    # Runs through all the articles in the Articles folder and processes them into JSON files

    num = 0

    for filename in os.listdir("Articles"):
        num += 1

        if filename.endswith(".txt"):
            filepath = os.path.join("Articles", filename)

            print("Processing:", filename)

            with open(filepath, "r", encoding="utf-8") as file:
                article_text = file.read()

            response = model.article_to_json(article=article_text)
            JsonParser.create_json(response, num)

    # Runs through all the JSON files in the Json folder and adds them to the SQLite database

    for filename in os.listdir("Json"):
        if filename.endswith(".json"):
            json_file_path = os.path.join("Json", filename)
            JsonParser.json_to_sqlite(json_file_path)


if __name__ == "__main__":
    main()
