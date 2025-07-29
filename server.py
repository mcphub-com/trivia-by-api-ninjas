import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apininjas/api/trivia-by-api-ninjas'

mcp = FastMCP('trivia-by-api-ninjas')

@mcp.tool()
def v1_trivia(category: Annotated[Union[str, None], Field(description='Category of trivia. Possible values are: artliterature language sciencenature general fooddrink peopleplaces geography historyholidays entertainment toysgames music mathematics religionmythology sportsleisure')] = None,
              limit: Annotated[Union[int, float, None], Field(description='How many results to return. Must be between 1 and 30. Default is 1. Default: 0')] = None) -> dict: 
    '''API Ninjas Trivia API endpoint'''
    url = 'https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia'
    headers = {'x-rapidapi-host': 'trivia-by-api-ninjas.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
