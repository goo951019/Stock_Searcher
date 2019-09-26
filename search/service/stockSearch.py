import search.util.dataGrabber as grabber
import search.util.parser as parser
import search.util.responseFormatter as response
import json
import sys

def stock_API_Response(stock_symbol):
    # grabs Nasdaq & market Watch HTML
    market_watch_html = grabber.grab_market_watch_stock_html(stock_symbol)

    # stock symbol validation check
    if not parser.validate_symbol(market_watch_html):
        return response.not_found_response("Invalid Stock Symbol")

    # using Beautiful Soup to parse and get data from market watch
    basic_stock_info = parser.parse_basic_stock_info(market_watch_html)
    
    return response.successful_response(basic_stock_info)
