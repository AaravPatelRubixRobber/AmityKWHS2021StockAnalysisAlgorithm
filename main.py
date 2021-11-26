import yfinance as yf
import GrowthEstimateScraper
import SentimentAnalysis
import pandas as pd

basicMaterials = ['APD', 'ACH', 'ASH', '500027', 'BHP', 'BRKM5', 'CHNR', 'CLW', 'CSNA3', 'EMN', 'FMC', 'FCX', 'FFHL', 'GGBR4', 'GLEN', '500440', 'IOSP', 'JMAT', 'KALU', 'KL', 'KLBN11', 'MMAT', 'NP', 'NTIC', 'PKX', 'KWR', 'ROLL', 'RIO', 'RGLD', 'SUZB3', '500470', 'X', 'VALE3', '500295']
consumerDiscretionary = ['ANF', 'ATVI', 'AC', 'BABA', 'ATD.B', 'AMZN', 'AMC', 'AAL', 'AEO', 'APTV', 'AZO', 'AVP', '532977', 'BNED', '500043', 'BBBY', 'BBY', 'BWA', '500530', 'BYD', 'BBW', 'BURL', 'CZR', 'GOOS', 'KMX', 'CCL', 'CAKE', 'CAAS', 'CEA', 'ZNH', '601888', 'CMG', 'CPG', 'COST', 'DJCO', 'DAL', 'DG', 'DLTR', 'DOL', 'DOM', 'DPZ', 'EZJ', 'EDR', 'ETSY', 'FL', 'F', 'GPS', 'GM', 'HRB', 'HOG', 'HAS', '500182', 'HIBB', 'HD', 'HMC', 'HSW', 'H', 'IMAX', 'IHG', 'JBLU', '533155', 'LE', 'LVS', 'LCII', 'RENT3', 'LAME4', 'LREN3', 'LOOK', 'LULU', 'LYFT', 'M', 'MGLU3', '500520', 'MAR', '532500', 'MAT', 'MCD', '000333', 'MOV', 'NTES', 'NFLX', 'EDU', 'NXT', 'NKE', 'NCLH', 'OTB', 'ORLY', 'PZZA', 'PSON', 'PTON', 'PLNT', 'QSR', 'REV', 'RBA', 'SIRI', 'SKYW', 'SWBI', 'SONY', 'LUV', 'SAVE', 'SPOT', 'SBUX', 'SFIX', 'TAL', 'TGT', '500570', 'TSLA', 'TXRH', 'TCS', 'EL', 'DIS', 'WEN', 'NCTY', '500114', 'TJX', 'TM', 'UBER', 'ULTA', 'UAA', 'URBN', 'VRA', 'VFC', 'WMT', 'WTB', 'WSM', 'WH', 'YUM', 'ZNGA']
consumerStaples = ['ABEV3', 'CRFB3', 'BRFS3', 'CPB', 'CASY', 'KO', 'CL', 'CORE', 'CTVA', 'CVS', 'DEO', 'GIS', '540743', '532424', '500696', '500875', 'JJSF', 'SBRY', 'JBSS3', 'K', 'KDP', '600519', 'MDIA3', 'MKC', 'MCK', 'TAP', 'MNST', 'FIZZ', '500790', 'PEP', 'PG', 'RADL3', 'RKT', 'RAD', 'SFM', 'SYY', 'HSY', 'TR', 'THS', 'TSN', 'UL', 'ULVR', 'UNFI', 'WBA', 'WDFC', '000858', 'WYN']
energy = ['AMTX', 'BP', 'CCJ', 'CNQ', 'CVX', 'SNP', '00386', '533278', 'CLR', 'CSAN3', 'ET', 'XOM', '532155', 'HES', 'LAM', 'NGS', 'NOV', '500312', 'OKE', 'BRDT3', 'PTR', '00857', 'PETR3', 'PETR4', 'PSX', '500325', 'RDSA', 'SU', 'SUN', 'TLW', 'UGPA3']
financials = ['AFL', 'ALL', 'APAM', 'AV.', '532215', 'B3SA3', '532978', 'BBDC3', 'BBDC4', 'BPAC11', 'BBAS3', 'SANB11', 'BAC', '002142', 'BNS', 'OZK', 'BCS', 'BBSE3', 'BLK', 'BX', 'BPFH', 'CWB', '00939', 'JRJC', 'C', 'CLIG', 'CS', 'DB', 'DFS', 'FFH', 'BEN', 'GBCI', 'GS', 'GEG', 'GWO', '500180', '500010', 'HSBA', '532174', 'ICE', 'IRBR3', 'ITUB4', 'ITSA4', 'JPM', 'KEY', 'KKR', '500247', 'LAZ', 'LLOY', 'L', 'MTB', '500271', 'MET', 'MCO', 'MS', 'NWG', 'ONB', 'OPY', '02318', 'PNC', 'PSSA3', 'PRU', '532955', 'RF', 'RY', 'SDR', 'SEIC', 'STAN', '500112', 'SULA11', 'TROW', 'UBS', 'WFC', 'WBK', '532648']
healthCare = ['ABT', 'ABBV', 'ACHC', 'AMGN', 'AZN', '524804', 'ACB', 'BAX', 'BMY', 'CSII', 'CPRX', 'CNC', '500087', '500124', 'ENDP', 'GMAB', 'GILD', 'GSK', 'GMED', '532482', 'HBIO', 'HYPE3', 'ILMN', 'IQV', '600276', 'JNJ', 'MDC', 'MRK', 'MYGN', 'GNDI3', 'NVS', 'PFE', '500302', 'PBH', 'REGN', '300760', 'SN.', '524715', 'TEVA', 'TVTY', 'UNH', 'VEEV', 'VYNT', 'ZGNX']
industrials = ['AXP', 'AMN', '600585', '00914', 'ARCB', 'ASGN', '500820', 'BECN', '509480', '500103', 'BILL', 'BA', 'BBD.B', 'BNZL', 'CAR', 'CJT', 'CAT', 'CCRO3', '03311', 'CYD', 'CIEL3', '00267', 'DE', 'PLOW', 'EMBR3', 'EXPN', 'FICO', 'FERG', 'FCN', 'GE', 'ROCK', 'GAPB', 'HTLD', 'KSU', '500510', 'LMT', 'MA', 'MNDI', '500304', 'PCAR', 'PYPL', 'RTX', 'RR.', 'RAIL3', '600009', 'SMIN', 'SNA', 'MIDD', 'TWI', 'TREX', '532538', 'VRSK', 'V', 'WNC', 'WEGE3', 'ZTO']
realEstate = ['BRML3', '000002', '02202', '600007', 'DLR', 'EXR', 'IRM', 'MULT3', 'DOC', 'PSA', 'RMV', 'GEO']
technology = ['ADBE', 'GOOG', 'AAPL', 'BIDU', 'BNFT', 'CTSH', 'CSU', 'DSCV', 'DXC', '532927', 'ENGH', 'FB', 'FTNT', 'GRPN', '002415', '532281', '500209', '535648', 'MANH', 'MTCH', '03690', 'MCRO', 'MSFT', '532819', 'NVDA', 'NXPI', 'ORCL', 'QCOM', 'SGE', 'CRM', 'SAP', 'SHOP', 'SOHU', '532540', '532755', '00700', 'TWTR', '507685', 'XRX']
telecommunications = ['ANET', '532493', 'T', 'BCE', '532454', 'BT.A', '00941', 'CMCSA', '601138', 'GOGO', 'VIVT3', 'UTSI', 'VEON', 'VZ', 'VOD']
utilities = ['AEP', 'AWK', 'CU', 'ELET3', 'ELET6', '00384', '600900', 'SBSP3', 'CMIG4', 'CPFE3', 'D', 'ENGI11', 'EGIE3', 'EQTL3', 'FE', '517300', 'HNP', 'MSEX', 'NFG', '532555', 'PCG', '532898', 'SRE', 'SVT', '533206', 'SJW', 'SO', 'SSE', '500400', 'YORW', 'UGI', 'UU.']

"""basicMaterials = []
consumerDiscretionary = []
consumerStaples = []
energy = []
financials = []
healthCare = []
industrials = []
realEstate = []
technology = ['GOOG', 'AAPL']
telecommunications = []
utilities = []"""

sectorIndices = {0: "basicMaterials",
             1: "consumerDiscretionary",
             2: "consumerStaples",
             3: "energy",
             4: "financials",
             5: "healthCare",
             6: "industrials",
             7: "realEstate",
             8: "technology",
             9: "telecommunications",
             10: "utilities"}

allStocks = [basicMaterials,
             consumerDiscretionary,
             consumerStaples,
             energy,
             financials,
             healthCare,
             industrials,
             realEstate,
             technology,
             telecommunications,
             utilities]

def calcScoreValue(ticker):
    print('Calculating value score...')

    score = 0
    passCriteria = True

    #GETS TICKER
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        print(stock.info)
        assert(len(info) > 10)
    except:
        print('error with retrieving ticker')
        return -1

    #CALCULATES SCORES FOR EACH METRIC
    try:
        forwardPE = 1000/info['forwardPE']
        if info['forwardPE'] > 30 or info['forwardPE'] < 0: passCriteria = False
        print('forwardPE', info['forwardPE'])
    except:
        print('error with forward p/e... will try supplementing with trailing p/e')
        try:
            forwardPE = 1000/info['trailingPE']
            if info['trailingPE'] > 30 or info['trailingPE'] < 0: passCriteria = False
            print('trailingPE', info['trailingPE'])
        except:
            print('error with trailing p/e')
            forwardPE = 0

    try:
        priceToBook = 25/info['priceToBook']
        print('p/b', info['priceToBook'])
    except:
        print('error with priceToBook')
        priceToBook = 0

    try:
        if info["trailingAnnualDividendYield"] == None or info["trailingAnnualDividendYield"] == 0.0:
            dividendYeild = 0
            print('dividend yeild', 0)
        else:
            dividendYeild = info["trailingAnnualDividendYield"]*1000
            print('dividend yeild', info['trailingAnnualDividendYield'])
    except:
        print('error with dividend yeild')
        dividendYeild = 0

    try:
        currentRatio = 7*info['currentRatio']
        if info['currentRatio'] < 0.7: passCriteria = False
        elif info['currentRatio'] < 1: currentRatio = -75
        print('current ratio', info['currentRatio'])
    except:
        print('error with current ratio')
        currentRatio = 0
    #fiveYearAveDividendYield = info['fiveYearAvgDividendYield']
    #need something to show years of consecutive dividend payments

    if not passCriteria:
        print('failed criteria')
        return -1

    #CALCULATES FINAL SCORE
    score = forwardPE + priceToBook + dividendYeild + currentRatio
    return score

def calcScoreGrowth(ticker):
    print('Calculating growth score...')
    score = 0
    passCriteria = True
    # GETS TICKER
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        assert (len(info) > 10)
    except:
        print('error with retrieving ticker')
        return -1

    # CALCULATES SCORES FOR EACH METRIC
    try:
        pegRatio = 100 / info['pegRatio']
        if info['pegRatio'] > 4: passCriteria = False
        print('pegRatio', info['pegRatio'])
    except:
        print('error with pegRatio')
        pegRatio = 0
    try:
        CalcGrowth = float(GrowthEstimateScraper.getLTGrowthRate(ticker))
        if CalcGrowth < 15: passCriteria = False
        forcastedGrowth = 40*min(1+CalcGrowth/100, 1.7)**5
        print('forcastedGrowth', CalcGrowth)
        #print('forwardEPS', info["forwardEPS"])
        #print('trailingEPS', info["trailingEPS"])
    except:
        print('error with forcastedGrowth')
        forcastedGrowth = 0
    try:
        returnOnEquity = 100*min(info['returnOnEquity'], 1)
        print('returnOnEquity', info['returnOnEquity'])
    except:
        print('error with returnOnEquity')
        returnOnEquity = 0
    try:
        currentRatio = 5*info['currentRatio']
        if info['currentRatio'] < 0.7: passCriteria = False
        elif info['currentRatio'] < 1: currentRatio = -75
        print('current ratio', info['currentRatio'])
    except:
        print('error with current ratio')
        currentRatio = 0

    if not passCriteria:
        print('failed criteria')
        return -1

    score = pegRatio + forcastedGrowth + returnOnEquity + currentRatio
    return score

def calcTechnicalScore(ticker):
    score = 0
    # GETS TICKER
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        assert (len(info) > 10)
    except:
        print('error with retrieving ticker')
        return -1

    try:
        twoHundredDayAverage = info["twoHundredDayAverage"]
        fiftyDayAverage = info["fiftyDayAverage"]
        print("two hundred day average: ", twoHundredDayAverage)
        print("fifty day average: ", fiftyDayAverage)
        momentum = 100 if twoHundredDayAverage < fiftyDayAverage else 0
    except:
        print('error with momentum')
        momentum = 0
        returnOnEquity = 0

    try:
        sentiment = SentimentAnalysis.getSentiment(ticker)
        print("sentiment -", sentiment)
        sentimentScore = sentiment*500
    except:
        print('error getting company sentiment')
        sentiment = 0
        sentimentScore = 0

    score = momentum + sentimentScore
    return score



#"C:\AaravWorld\code\Python\Python38\SentimentAnalysisStockScraper.py"
#https://towardsdatascience.com/sentiment-analysis-of-stocks-from-financial-news-using-python-82ebdcefb638

stockScores = {}

sectorIndex = 0
for sector in allStocks:
    stockScores[sectorIndices[sectorIndex]] = {}
    print('\n\n\n' + sectorIndices[sectorIndex].upper())
    for stock in sector:
        print(2 * '\n', '***' + stock + '***', '\n----------')
        stockScoreValue = calcScoreValue(stock)
        print()
        stockScoreGrowth = calcScoreGrowth(stock)
        print()
        stockScoreTechnical = calcTechnicalScore(stock)
        print(stock + ' scores: ', 'value-' + str(stockScoreValue) + ', growth-' + str(stockScoreGrowth) + ', technical-' + str(stockScoreTechnical))
        stockScores[sectorIndices[sectorIndex]][stock] = [stockScoreValue, stockScoreGrowth, stockScoreTechnical]
    sectorIndex += 1

print('stockScores', stockScores)

sectorIndex = 0
for sector in stockScores.values():

    print('\n' + sectorIndices[sectorIndex])
    sectorIndex += 1

    topValue = {}
    topGrowth = {}
    valueMinScore = 0
    valueItems = max(int(len(sector)/5), 7)
    growthMinScore = 0
    growthItems = max(int(len(sector)/5), 7)

    for s, scores in sector.items():
        if scores[0] > valueMinScore:
            topValue[s] = scores[0]
            if len(topValue) >= valueItems:
                minKey = min(topValue, key=topValue.get)
                del topValue[minKey]

        if scores[1] > growthMinScore:
            topGrowth[s] = scores[1]
            if len(topGrowth) >= growthItems:
                minKey = min(topGrowth, key=topGrowth.get)
                del topGrowth[minKey]

    topValueList = topValue.keys()
    dfValue = pd.DataFrame({'stock': topValueList,
               'value': [sector[stock][0] for stock in topValueList],
               'technical': [sector[stock][2] for stock in topValueList]})
    topGrowthList = topGrowth.keys()
    dfGrowth = pd.DataFrame({'stock': topGrowthList,
                            'growth': [sector[stock][1] for stock in topGrowthList],
                            'technical': [sector[stock][2] for stock in topGrowthList]})

    print("top Value:")
    print(dfValue)
    print("top Growth:")
    print(dfGrowth)
