from urllib.request import urlopen as request
import search.util.parser as parser

# returns HTML of stock symbol input from nasdaq
def grab_nasdaq_stock_html(stock_symbol):
    request_result = request('https://www.nasdaq.com/symbol/' + stock_symbol)
    html = request_result.read()
    request_result.close()
    return html

# returns HTML of stock symbol input from market watch
def grab_market_watch_stock_html(stock_symbol):
    request_result = request('https://www.marketwatch.com/investing/stock/' + stock_symbol)
    html = request_result.read()
    request_result.close()
    return html

# check if it is a validate stock symbol
def grab_and_validate_symbol(stock_symbol):
    nasdaq_html = grab_nasdaq_stock_html(stock_symbol)
    market_watch_html = grab_market_watch_stock_html(stock_symbol)

    if not parser.validate_symbol(nasdaq_html, market_watch_html):
        return False
    return True
