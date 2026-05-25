# Equity Research Assistant

An AI-powered tool that generates professional equity research summaries 
for any stock ticker using live market data with Yahoo Finance.

## What It Does
- Takes any stock ticker as input (e.g. AAPL, TD, SHOP)
- Pulls live financial data including revenue, P/E ratio, 52-week range, and analyst targets
- Uses Google Gemini AI to generate a professional analyst-style summary (Not paying for Claude)
- Covers business overview, profitability, valuation, key risks, and overall outlook

## Technologies Used
- Python
- Google Gemini AI API
- yFinance (Yahoo Finance)

## How to Run It
1. Clone the repository
2. Install dependencies:
   `pip install google-genai yfinance`
3. Add your Google Gemini API key to line 4
4. Run:
   `python main.py`
