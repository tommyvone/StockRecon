
# 🚀 Global Stock Picker

A Flask web application that helps users discover trending stocks from global markets with direct trading platform access.

## Features

- **Random Stock Selection**: Get 5 randomly selected stocks from a curated list of global opportunities
- **Interactive Dropdown**: Select any stock to view detailed information
- **Direct Trading Links**: One-click access to Yahoo Finance for each stock
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Refresh**: Get new stock picks instantly with the refresh button

## Stock Coverage

The app features carefully selected stocks across various sectors and regions:

- **Technology**: NVIDIA (NVDA), TSMC (TSM), ASML (ASML), Alphabet (GOOGL)
- **Clean Energy**: NextEra Energy (NEE)
- **E-commerce**: Shopify (SHOP), MercadoLibre (MELI)
- **International**: Reliance Industries (India), Airbus (Europe)
- **Cybersecurity**: CrowdStrike (CRWD)

## Installation & Setup

1. **Clone or fork this repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```
4. **Access the app**: Open your browser to `http://localhost:5000`

## Usage

1. **View Random Picks**: The homepage displays 5 randomly selected stocks
2. **Analyze Stocks**: Use the dropdown to select any stock for detailed analysis
3. **Start Trading**: Click the "Start Trading" button to access Yahoo Finance
4. **Refresh Picks**: Click the refresh button to get new random selections

## File Structure

```
├── main.py              # Flask application and stock data
├── templates/
│   └── index.html       # Frontend HTML with CSS and JavaScript
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Deployment

This app is configured for deployment on Replit with:
- **Build Command**: `pip install --no-cache-dir -r requirements.txt`
- **Run Command**: `python3 main.py`
- **Port Configuration**: Automatically uses the PORT environment variable

## Customization

### Adding New Stocks

Edit the `STOCKS` list in `main.py`:

```python
STOCKS = [
    {
        "title": "Stock Name (SYMBOL)",
        "description": "Brief description of the company",
        "why_trade": "Reason why it's a good trading opportunity",
        "trade_url": "https://finance.yahoo.com/quote/SYMBOL"
    },
    # Add more stocks here
]
```

### Changing the Number of Random Picks

Modify the `get_random_stocks()` function call in the routes:

```python
random_stocks = get_random_stocks(7)  # Change from 5 to any number
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: CSS Grid, Flexbox, Gradients
- **API**: RESTful endpoints for stock refresh

## API Endpoints

- `GET /` - Homepage with random stock selection
- `GET /refresh` - JSON API endpoint for new random stocks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This application is for educational and informational purposes only. It does not provide financial advice. Always do your own research and consult with financial professionals before making investment decisions.
