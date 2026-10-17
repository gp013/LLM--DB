from openai import OpenAI
from pydantic import BaseModel


class ArticleResponse(BaseModel):
    players: list[str]
    teams: list[str]
    sport: str
    summary: str


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

    def __init__(self, api_key: str):
        self._client = OpenAI(api_key=api_key)

    def article_to_json(self, article: str):
        """Convert article text to a document summary in JSON."""
        response = self._client.responses.parse(
            model="gpt-4o-mini",
            input=self._create_prompt(text=article),
            text_format=ArticleResponse,
        )

        return response.model_dump_json()

    def _create_prompt(self, text: str) -> str:
        """Configure the prompt for the LLM.

        We move this inside a helper to reduce the amount of noise at the call site.
        This change makes it easier to parse
            1. Exactly what the prompt is saying (since we can indent it).
            2. What the LLM call looks like.

        This function is almost identical to the prompt you originally had except some
        different formatting to make it more readable.
        """

        prompt = f"""Read the text from the following file and turn 
        its contents into a JSON object with the following keys:
        players, teams, sport, and summary.

        The JSON should be structured as follows: 

            'players': [], 
            'teams': [], 
            'sport': '', 
            'summary': ''. 

        Please only return the JSON object, no json label or apostrophes at the 
        start and end of the object. players will be a list of strings, teams will 
        be a list of strings, sport will be a string, and summary will be a string.
        Sport will be referred to as the sport not the league that the sport takes place 
        in, American Football will be listed as 'Football', Soccer/Futbol will be listed as 
        'Soccer'. Sport should also start with a captial letter and the rest be lowercase.

        Article Text:
        {text}"""

        return prompt
