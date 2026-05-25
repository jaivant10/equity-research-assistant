from google import genai
import yfinance as yf

# Your API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    data = f"""
    Company: {info.get('longName', 'N/A')}
    Sector: {info.get('sector', 'N/A')}
    Current Price: {info.get('currentPrice', 'N/A')}
    Market Cap: {info.get('marketCap', 'N/A')}
    Revenue: {info.get('totalRevenue', 'N/A')}
    Net Income: {info.get('netIncomeToCommon', 'N/A')}
    P/E Ratio: {info.get('trailingPE', 'N/A')}
    EPS: {info.get('trailingEps', 'N/A')}
    52 Week High: {info.get('fiftyTwoWeekHigh', 'N/A')}
    52 Week Low: {info.get('fiftyTwoWeekLow', 'N/A')}
    Analyst Target Price: {info.get('targetMeanPrice', 'N/A')}
    Business Summary: {info.get('longBusinessSummary', 'N/A')}
    """
    return data

def summarize(ticker):
    print(f"\nFetching data for {ticker}...")
    stock_data = get_stock_data(ticker)

    prompt = f"""
    You are a professional investment analyst. 
    Based on the following data, write a concise analyst-style summary covering:
    - What the company does
    - Revenue and profitability
    - Valuation (P/E, price vs 52-week range)
    - Key risks
    - Overall outlook

    Data:
    {stock_data}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    print("\n--- ANALYST SUMMARY ---\n")
    text = "".join(part.text for part in response.candidates[0].content.parts if hasattr(part, 'text'))
    print(text)

# Run it
ticker = input("Enter a stock ticker (e.g. AAPL, TD, SHOP): ").upper()
summarize(ticker)
