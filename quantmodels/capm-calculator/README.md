# CAPM Calculator

This project is a Capital Asset Pricing Model (CAPM) calculator that allows users to compute the expected return of multiple companies based on their stock data and market performance.

## Project Structure

```
capm-calculator
├── src
│   ├── main.py          # Entry point for the application
│   ├── capm.py          # Contains the CAPM calculation logic
│   ├── data
│   │   └── fetch.py     # Responsible for fetching stock and market data
│   └── utils
│       └── helpers.py   # Utility functions for data processing
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd capm-calculator
pip install -r requirements.txt
```

## Usage

1. Run the main application:

```bash
python src/main.py
```

2. Input the stock tickers for which you want to calculate the CAPM when prompted. You can enter multiple tickers separated by commas.

3. The application will fetch the necessary data, calculate the CAPM values (alpha and beta), and display the expected annual returns for each ticker.

## Example

```plaintext
Enter stock tickers (comma-separated): AAPL, MSFT, GOOG
```

The application will output the CAPM results for Apple, Microsoft, and Google.

## Dependencies

This project requires the following Python libraries:

- `yfinance`: For downloading stock data
- `pandas`: For data manipulation and analysis
- `statsmodels`: For statistical modeling and regression analysis

Make sure to install these libraries using the `requirements.txt` file provided.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.