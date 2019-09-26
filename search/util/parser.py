from bs4 import BeautifulSoup as parser
import json
import unicodedata

# parse company information from marketwatch
def parse_basic_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    intraday_data = parsed_soup.find(class_="intraday__change")
    basic_info_dict = {"stockName": parsed_soup.find(class_="company__name").string,
                       "stockPrice": '$' + parsed_soup.find(class_="intraday__price").find("bg-quote").string,
                       "priceChange": '$' + intraday_data.find(class_="change--point--q").find("bg-quote").string,
                       "percentChange": intraday_data.find(class_="change--percent--q").find("bg-quote").string}
    return basic_info_dict

# Checks if stock symbol is validate
def validate_symbol(market_watch_html):
    # using Beautiful Soup to parse and get data.
    stock_name = parser(market_watch_html, "html.parser").find(class_="company__name")

    if stock_name is None:
        return False
    return True
