import yfinance as yf
import matplotlib.pyplot as plt

companies = {
    "AAPL": "Apple",
    "GOOG": "Google",
    "AMZN": "Amazon",
    "MSFT": "Microsoft"
}

plt.figure(figsize=(12, 7))

for ticker, name in companies.items():

    data = yf.Ticker(ticker).history(period="max")

    data["Year"] = data.index.year

    yearly_avg = data.groupby("Year")["Close"].mean()

    plt.plot(yearly_avg.loc[2021:2025], label=name, marker='o')


plt.title("Big Tech: Average Stock Price (2021-2025)")
plt.xlabel("Year")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()