
from flask import Flask, render_template, request

app = Flask('app')

# Stock data with trading platform links
STOCKS = [
    {
        'title': 'NVIDIA (NVDA)',
        'description': 'GPU leader powering AI, gaming, and data centers',
        'why_trade': 'AI demand is surging globally; NVIDIA dominates the space',
        'trade_url': 'https://www.fidelity.com/trading/the-fidelity-account'
    },
    {
        'title': 'TSMC (TSM)',
        'description': 'World\'s largest semiconductor foundry',
        'why_trade': 'Global chip shortages and rising demand make TSMC essential',
        'trade_url': 'https://www.schwab.com/investing'
    },
    {
        'title': 'NextEra Energy (NEE)',
        'description': 'U.S. clean energy giant in wind and solar',
        'why_trade': 'Governments worldwide are investing in renewable infrastructure',
        'trade_url': 'https://www.etrade.com/investing/stocks'
    },
    {
        'title': 'ASML Holding (ASML)',
        'description': 'Dutch firm producing advanced chip-making machines',
        'why_trade': 'Critical supplier for next-gen semiconductors amid global tech race',
        'trade_url': 'https://www.degiro.com'
    },
    {
        'title': 'Alphabet (GOOGL)',
        'description': 'Parent of Google, strong in cloud, ads, and AI',
        'why_trade': 'Digital ad recovery and AI integration are boosting global revenue',
        'trade_url': 'https://www.webull.com'
    },
    {
        'title': 'Shopify (SHOP)',
        'description': 'E-commerce platform for global merchants',
        'why_trade': 'Online retail continues to grow, especially in emerging markets',
        'trade_url': 'https://www.td.com/ca/en/investing/direct-investing'
    },
    {
        'title': 'Reliance Industries (RELIANCE.NS)',
        'description': 'Indian conglomerate in telecom, retail, and energy',
        'why_trade': 'India\'s digital and economic expansion makes it a strategic play',
        'trade_url': 'https://zerodha.com'
    },
    {
        'title': 'MercadoLibre (MELI)',
        'description': 'Latin America\'s top e-commerce and fintech platform',
        'why_trade': 'Rising internet access and digital payments adoption in the region',
        'trade_url': 'https://www.interactivebrokers.com'
    },
    {
        'title': 'Airbus (AIR.PA)',
        'description': 'European aerospace leader',
        'why_trade': 'Post-COVID travel rebound and airline fleet upgrades drive demand',
        'trade_url': 'https://www.trading212.com'
    },
    {
        'title': 'CrowdStrike (CRWD)',
        'description': 'Cybersecurity firm protecting global enterprises',
        'why_trade': 'Cyber threats are rising; companies are increasing security budgets',
        'trade_url': 'https://robinhood.com'
    }
]

@app.route('/')
def stock_picker():
    return render_template('index.html', stocks=STOCKS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
