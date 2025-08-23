
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Stock data
STOCKS = [
    {
        "title": "NVIDIA (NVDA)",
        "description": "GPU leader powering AI, gaming, and data centers",
        "why_trade": "AI demand is surging globally; NVIDIA dominates the space",
        "trade_url": "https://finance.yahoo.com/quote/NVDA"
    },
    {
        "title": "TSMC (TSM)",
        "description": "World's largest semiconductor foundry",
        "why_trade": "Global chip shortages and rising demand make TSMC essential",
        "trade_url": "https://finance.yahoo.com/quote/TSM"
    },
    {
        "title": "NextEra Energy (NEE)",
        "description": "U.S. clean energy giant in wind and solar",
        "why_trade": "Governments worldwide are investing in renewable infrastructure",
        "trade_url": "https://finance.yahoo.com/quote/NEE"
    },
    {
        "title": "ASML Holding (ASML)",
        "description": "Dutch firm producing advanced chip-making machines",
        "why_trade": "Critical supplier for next-gen semiconductors amid global tech race",
        "trade_url": "https://finance.yahoo.com/quote/ASML"
    },
    {
        "title": "Alphabet (GOOGL)",
        "description": "Parent of Google, strong in cloud, ads, and AI",
        "why_trade": "Digital ad recovery and AI integration are boosting global revenue",
        "trade_url": "https://finance.yahoo.com/quote/GOOGL"
    },
    {
        "title": "Shopify (SHOP)",
        "description": "E-commerce platform for global merchants",
        "why_trade": "Online retail continues to grow, especially in emerging markets",
        "trade_url": "https://finance.yahoo.com/quote/SHOP"
    },
    {
        "title": "Reliance Industries (RELIANCE.NS)",
        "description": "Indian conglomerate in telecom, retail, and energy",
        "why_trade": "India's digital and economic expansion makes it a strategic play",
        "trade_url": "https://finance.yahoo.com/quote/RELIANCE.NS"
    },
    {
        "title": "MercadoLibre (MELI)",
        "description": "Latin America's top e-commerce and fintech platform",
        "why_trade": "Rising internet access and digital payments adoption in the region",
        "trade_url": "https://finance.yahoo.com/quote/MELI"
    },
    {
        "title": "Airbus (AIR.PA)",
        "description": "European aerospace leader",
        "why_trade": "Post-COVID travel rebound and airline fleet upgrades drive demand",
        "trade_url": "https://finance.yahoo.com/quote/AIR.PA"
    },
    {
        "title": "CrowdStrike (CRWD)",
        "description": "Cybersecurity firm protecting global enterprises",
        "why_trade": "Cyber threats are rising; companies are increasing security budgets",
        "trade_url": "https://finance.yahoo.com/quote/CRWD"
    }
]

def get_random_stocks(count=5):
    """Get a random selection of stocks"""
    return random.sample(STOCKS, min(count, len(STOCKS)))

@app.route('/')
def home():
    random_stocks = get_random_stocks(5)
    return render_template('index.html', stocks=random_stocks)

@app.route('/refresh')
def refresh_stocks():
    """API endpoint to get new random stocks"""
    random_stocks = get_random_stocks(5)
    return jsonify(random_stocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
