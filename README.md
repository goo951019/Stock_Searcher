Python Stock Searcher
The app searches Nasdaq and MarketWatch websites to obtain Stock Data.
It grabs data with urlopen, parses with Beautifil Soup, and creates an endpoint with Flask_API.

how to run:
*** Be sure to download all the requirements (Flask-API, BeautifulSoup4) through using pip ***
python3 main.py --> runs the code. 
                    At the end of main.py, there is test line "print(stock_API_Response('AMZN'))" to see the result

how to deploy:
*** Be sure to be in project directory ***
gcloud init
 --> Then, login and choose project
gcloud app deploy
gcloud app browse

Example for https://stock-searcher.appspot.com/AMZN
{
    "stockName": "Amazon.com Inc.", 
    "stockPrice": "$1,792.00", 
    "priceChange": "$-1.40", 
    "percentChange": "-0.08%", 
}