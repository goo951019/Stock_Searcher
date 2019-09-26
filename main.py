from flask_api import FlaskAPI
from flask_api import status
from search.util.dataGrabber import grab_and_validate_symbol
from search.service.stockSearch import stock_API_Response

app = FlaskAPI(__name__)

@app.route('/')
def root():
    return ("Welcome to Stock Searcher!<br/>"
            "To search stock please browse:<br/>"
            "https://stock-searcher.appspot.com/Stock_Symbol<br/>"
            "Example: https://stock-searcher.appspot.com/AMZN<br/>"
            "<br/>"
            "To Check status<br/>"
            "https://stock-searcher.appspot.com/status")

@app.route('/<string:stock_symbol>')
def stock_api(stock_symbol):
    return stock_API_Response(stock_symbol)

@app.route('/status')
def status_check():
    if not grab_and_validate_symbol("AMZN"):
        return status.HTTP_404_NOT_FOUND
    return "Server Running"

# Test line
print(stock_API_Response('AMZN'))
print("Project works!")
