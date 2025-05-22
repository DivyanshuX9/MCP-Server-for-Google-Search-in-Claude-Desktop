import urllib.parse
from mcp.server.fastmcp import FastMCP
import webbrowser
import urllib
mcp = FastMCP("Google Search")

@mcp.tool()
def open_gooogle_search(query):
    """search in google with query"""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)
    
    


@mcp.resource("greetings://{name}")
def get_greetings(name: str) -> str:
    """get a personalised greeting"""
    return f"Hello {name}!"