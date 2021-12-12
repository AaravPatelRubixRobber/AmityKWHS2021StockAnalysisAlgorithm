# AmityKWHS2021StockAnalysisAlgorithm
A stock analysis algorithm which can identify leading stocks based on fundamental and technical indicators. This was made for the Wharton High School Investing Competition by the Amity Spartans

The program comprises of 3 files
  - main.py - calculates stock scores using a variety of fundamental and technical indicators
  - growthEstimateScraper.py - uses analyst growth estimates to get a genaric growth estimate for the company
  - sentimentAnalysis.py - uses an NLP machine learning algorithm to calculate a company's sentiment based on news

The algorithm goes through all investable stocks on the Wharton Investing Competiton spreadsheet. The algorithm then calculates 3 scores: a value score, a growth score, and a technical score. 

The value score asseses a company's fundamental situation and uses metrics to see if the stock is fundamentally undervalued. Some of these metrics include:
  - forward price to earnings
  - price to book
  - dividend yeild
  - current ratio

The growth score asseses a company's ability to grow revenues over the long-term. Some of these metrics include:
  - PEG ratio
  - forcasted growth
  - return on equity
  - current ratio

Finally, the technical score asseses a company's mid-term situation. It uses trading indicators and company news to predict a stock's short-term movements. Some metrics used to calculate this are:
  - MACD (200 MA long-term, 500 MA short-term)
  - NLP news sentiment surrounding a company

These scores are used to identify leading stocks in various industries, and they are used in conjuction with discretionary analysis to select our investments.
