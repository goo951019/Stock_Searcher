from bs4 import BeautifulSoup as parser
import json
from search.util.keyDictionary import key_dict as dict
import unicodedata

# parse company information from nasdaq
def parse_basic_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    intraday_data = parsed_soup.find(class_="intraday__change")
    basic_info_dict = {"stockName": parsed_soup.find(class_="company__name").string,
                       "stockPrice": '$' + parsed_soup.find(class_="intraday__price").find("bg-quote").string,
                       "priceChange": '$' + intraday_data.find(class_="change--point--q").find("bg-quote").string,
                       "percentChange": intraday_data.find(class_="change--percent--q").find("bg-quote").string}
    return basic_info_dict

# parse stock information from market watch
def parse_key_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    key_stock_data = parsed_soup.find(class_="row overview-results relativeP")
    key_stock_rows = key_stock_data.find_all(class_="table-row")
    return handle_each_stock_row(key_stock_rows)

# insert key and value into dict
def insert_to_dict(dict, key, value):
    value = unicodedata.normalize("NFKD", value)
    separator = " / "

    # split string that contains '/' and insert into dict separately.
    if separator in key and separator in value:
        keys = key.split(separator, 1)
        values = value.split(separator, 1)
        dict[keys[0]] = "".join(values[0].split())
        dict[keys[1]] = "".join(values[1].split())
    else:
        dict[key] = "".join(value.split())

# put table rows into keyDictionary
def handle_each_stock_row(key_stock_rows):
    stock_data_dict = {}
    # read a single table cell
    for row in key_stock_rows:
        table_cells = row.find_all(class_="table-cell")

        # If the table cell is in the key Dictionary, insert it into dict.
        for data in table_cells[0].contents:
            if data.string in dict:
                # insert_to_dict(stock_data_dict, key, value)
                insert_to_dict(stock_data_dict, dict[data.string], table_cells[1].string.strip())
    return stock_data_dict

# Checks if stock symbol is validate
def validate_symbol(nasdaq_html, market_watch_html):
    # using Beautiful Soup to parse and get data.
    data = parser(nasdaq_html, "html.parser").find(class_="row overview-results relativeP")
    stock_name = parser(market_watch_html, "html.parser").find(class_="company__name")

    if stock_name is None or data is None:
        return False
    return True
