import yfinance as yf


# Get user input for ETF tickers
ticker = input("Enter your ticker: ").upper().split(",")
ticker = [t.strip() for t in ticker]

while True:

    # Simple prediction logic based on daily percentage change
    def prediction(change):
        if change > 1.5:
            return "📈 Bullish", "Strong upward momentum"
        elif change > -1:
            return "😐 Moderate", "Stable with low volatility"
        else:
            return "📉 Bearish", "Downward trend"

    # Fetch data and analyze
    for symbol in ticker:
        etf = yf.Ticker(symbol)
        data = etf.history(period="2d")
    if len(data) < 2:
        print(f"Not enough data for {symbol}. Skipping...")
        continue

    # Calculate daily percentage change
    current_price = data['Close'][-1]
    previous_price = data['Close'][-2]
    change_percent = ((current_price - previous_price)/previous_price) * 100

    trend, explanation = prediction(change_percent)

    print("\n-----------------------------")
    print(f"ETF: {symbol}")
    print(f"Current Price: ${current_price:.2f}")
    print(f"Previous Close: ${previous_price:.2f}")
    print(f"Daily Change: {change_percent:.2f}%")
    print(f"Prediction: {trend}")
    print(f"Reason: {explanation}")

    # choice to continue or exit
    cont = input("\nDo you want to check another ETF? (yes/no): ").lower()
    if cont == 'yes':
        ticker = input("Enter your ticker: ").upper().split(",")
        ticker = [t.strip() for t in ticker]
    elif cont != 'no' or cont != 'yes':
        print("Invalid input. Try again.")
        ticker = input("Enter your ticker: ").upper().split(",")
        ticker = [t.strip() for t in ticker]
    else:
        break


  





