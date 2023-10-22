#AbhishekDungraniRESTAPI for stock Market Simulation
from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

# Initial list of stocks
stocks = [
    {"name": "ABC Pvt Ltd", "symbol": "A", "price": 100.00},
    {"name": "XYZ LLC", "symbol": "B", "price": 150.00},
    {"name": "GHI Pvt Ltd", "symbol": "C", "price": 75.00},
]

# Simulate price and changes
def simulate_price_changes():
    while True:
        for stock in stocks:
            stock["price"] += random.uniform(-5, 5)
        time.sleep(5)

# Start the price simulation in a separate thread
import threading
price_simulation_thread = threading.Thread(target=simulate_price_changes)
price_simulation_thread.start()

# Define a stock class
class Stock:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price

# Route to add a new stock
@app.route('/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    name = data['name']
    symbol = data['symbol']
    price = data['price']
    new_stock = Stock(name, symbol, price)
    stocks.append({"name": name, "symbol": symbol, "price": price})
    return jsonify({'message': 'Stock added successfully'})

# Route to retrive all stocks
@app.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)
