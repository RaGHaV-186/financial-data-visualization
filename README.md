# Big Tech Stock Analysis 📈

### Overview
This project is a data visualization tool that tracks and compares the yearly stock performance of major tech giants (**Apple, Google, Amazon, Microsoft, Tesla**).
It automatically fetches historical market data using the Yahoo Finance API, processes the yearly averages to smooth out volatility, and plots the growth trends on a comparative line chart. This tool helps analysts visualize long-term performance trends across the tech sector.

### Features
* **Automated Data Extraction:** Uses the `yfinance` API to pull real-time historical market data.
* **Data Processing:** Calculates yearly averages using Pandas to smooth out daily price noise.
* **Multi-Stock Comparison:** Visualizes 5 different companies on a single comparative line chart.
* **Scalable Architecture:** Built with Python dictionaries and loops, making it effortless to add more companies in the future.

### Tech Stack
* **Python 3.x**
* **yfinance:** Financial Data API wrapper.
* **Pandas:** Data manipulation, cleaning, and aggregation.
* **Matplotlib:** Data visualization and plotting.

### How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/tech-stock-analysis.git](https://github.com/YOUR_USERNAME/tech-stock-analysis.git)
    cd tech-stock-analysis
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the analysis:**
    ```bash
    python main.py
    ```

### Sample Output

The script generates a dashboard window and saves an image file (`stock_analysis.png`) showing:
* **Multiple Colored Lines:** distinct trends for Apple, Google, Amazon, Microsoft, and Tesla.
* **X-Axis:** Timeframe from 2021 to 2025.
* **Y-Axis:** Average Stock Price in USD.
* **Legend:** Clearly labeled identifiers for each company.

---
*Created as part of a Data Science portfolio project.*
