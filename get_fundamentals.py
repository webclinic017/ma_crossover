import time

from utils import tickers
from alpha_vantage.fundamentaldata import FundamentalData

def fundamental_download_case(case: int,
                              ticker: str,
                              fd):
    '''
    Due to the API limit of 5 calls per minute, this function was desinged so
    that every 5th download can impose a sleep time of a minute.

    Parameters
    ----------
    case : int
        The download switch statement.
    ticker : str
        The ticker to download the data for
    fd : Fundamental Data Downloader
        The fundamental data downloader for AlphaVantage.

    Returns
    -------
    None
    '''
    
    if case == 0:
        annual_IS = fd.get_income_statement_annual(ticker)
        annual_IS[0].to_csv(f'data/{ticker}_annual_IS.csv', index = False)
        
    elif case == 1:
        annual_BS = fd.get_balance_sheet_annual(ticker)
        annual_BS[0].to_csv(f'data/{ticker}_annual_BS.csv', index = False)
        
    elif case == 2:
        annual_CF = fd.get_cash_flow_annual(ticker)
        annual_CF[0].to_csv(f'data/{ticker}_annual_CF.csv', index = False)
        
    if case == 3:
        quarterly_IS = fd.get_income_statement_quarterly(ticker)
        quarterly_IS[0].to_csv(f'data/{ticker}_quarterly_IS.csv', index = False)
        
    elif case == 4:
        quarterly_BS = fd.get_balance_sheet_quarterly(ticker)
        quarterly_BS[0].to_csv(f'data/{ticker}_quarterly_BS.csv', index = False)
        
    elif case == 5:
        quarterly_CF = fd.get_cash_flow_quarterly(ticker)
        quarterly_CF[0].to_csv(f'data/{ticker}_quarterly_CF.csv', index = False)
        
    return
        

def get_historical_fundamentals(ticker_list: list,
                                api_key: str):
    '''
    Using the AlphaVantage API, obtain the historical fundamental data for a
    set of tickers

    Parameters
    ----------
    ticker_list : list
        The list of tickers to download the fundamentals for
    api_key : str
        The AlphaVantage API key

    Returns
    -------
    None
    
    Notes
    -----
    On a free API key, only 500 calls per day are allowed. Given that this
    function downloads 6 different statements, a maximum of 83 tickers can be
    considered.
    '''
    
    fd = FundamentalData(api_key,
                         output_format = 'pandas',
                         )
    download = 0
    print('Downloading the fundamentals')
    
    for ticker in ticker_list:
        
        for case in range(0, 6):
            fundamental_download_case(case, ticker, fd)
            download += 1
            
            if download%5 == 0:
                time.sleep(60)
        
        print('Completed: ', ticker)

    return

api_key = 'MU3I3DR1WXM7WRV6'
ticker_list = tickers.get_tickers('spy')

get_historical_fundamentals(ticker_list[3:15], api_key)