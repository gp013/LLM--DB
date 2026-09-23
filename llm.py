from openai import OpenAI
import os
from dotenv import load_dotenv


class LanguageModel:
    
    """
    article_to_json takes in a text file and uses the OpenAI API to convert the contents of the file into a JSON object with specific keys: players, teams, sport, and summary. The function reads the text from the file, sends it to the OpenAI API with a prompt that specifies the desired JSON structure, and returns the resulting JSON object as a string.
    The JSON object will have the following structure:
    {
        "players": [],
        "teams": [],
        "sport": "",
        "summary": ""
    }
    """

    def article_to_json(article):
        load_dotenv()
        client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY")
        )
        
        with open(article, "r", encoding="utf-8") as file:
            article_text = file.read()
            response = client.responses.create(
            model="gpt-4o-mini",
            input=f"Read the text from the file {article_text} and turn its contents into a JSON object with the following keys: player(s), team(s), sport, and summary. The JSON should be structured as follows: 'players': [], 'teams': [], 'sport': '', 'summary': ''. Please only return the JSON object, no json label or apostrophes at the start and end of the object. players will be a list of strings, teams will be a list of strings, sport will be a string, and summary will be a string. Sport will be referred to as the sport not the league that the sport takes place in, American Football will be listed as 'Football', Soccer/Futbol will be listed as 'Soccer'. Sport should also start with a captial letter and the rest be lowercase.",
        )

        return response.output_text
    