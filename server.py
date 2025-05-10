from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import httpx

mcp = FastMCP("alphavantage")

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

API_END_POINT = "https://www.alphavantage.co/"

if not API_KEY:
    raise EnvironmentError("API_KEY is not set in .env")

@mcp.tool()
async def get_stock_data(symbol, interval="60min", function="TIME_SERIES_INTRADAY"):
    """
    Get stock data from Alpha Vantage API.
    Args:
        symbol (str): The stock symbol to query.
        interval (str): The interval for the stock data. Default is "60min".
        function (str): The function to use for the query. Default is "TIME_SERIES_INTRADAY".
    Returns:
        dict: The response from the Alpha Vantage API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"query",
            params={
                "apikey": API_KEY,
                "symbol": symbol,
                "interval": interval,
                "function": function,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()