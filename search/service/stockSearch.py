import search.util.dataGrabber as grabber
import search.util.parser as parser
import search.util.responseFormatter as response
import json
import sys

def stock_API_Response(stock_symbol):
    # grabs Nasdaq & market Watch HTML
    nasdaq_html = grabber.grab_nasdaq_stock_html(stock_symbol)
    market_watch_html = grabber.grab_market_watch_stock_html(stock_symbol)

    # stock symbol validation check
    if not parser.validate_symbol(nasdaq_html, market_watch_html):
        return response.not_found_response("Invalid Stock Symbol")

    # using Beautiful Soup to parse and get data from nasdaq & market watch
    key_stock_info = parser.parse_key_stock_info(nasdaq_html)
    basic_stock_info = parser.parse_basic_stock_info(market_watch_html)

    stock_data = join_stock_info(key_stock_info, basic_stock_info)

    return response.successful_response(stock_data)

# join data of nasdaq & stock watch together
def join_stock_info(key_stock_info, basic_stock_info):
    basic_stock_info["keyInfo"] = key_stock_info
    return json.dumps(basic_stock_info, ensure_ascii=False)