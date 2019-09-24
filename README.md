Python Stock Searcher
The app searches Nasdaq and MarketWatch websites to obtain Stock Data.
It grabs data with urlopen, parses with Beautifil Soup, and creates an endpoint with Flask_API.

how to run:
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
    "keyInfo": {
        "bestBid": "$1,791", 
        "bestAsk": "$1,796", 
        "oneYearTarget": "2250", 
        "todaysHigh": "$1,798.93", 
        "todaysLow": "$1,757", 
        "shareVolume": "4,526,884", 
        "fiftyDayAverageDailyVolume": "3,679,981", 
        "previousClose": "$1,787.83", 
        "fiftyTwoWeekHigh": "$1,307", 
        "marketCap": "887,116,097,301", 
        "PERatio": "74.41", 
        "forwardPEOneYear": "72.91", 
        "earningsPerShare": "$24.10", 
        "annualizedDividend": "N/A", 
        "exDividendDate": "N/A", 
        "dividendPaymentDate": "N/A", 
        "currentYield": "0%", 
        "beta": "1.42"
    }
}