from ga import funcs

if __name__ == "__main__":
    
    ga_config = {
                 # Basic controls for the genetic algo
                 'num strats': 30, # Number of strategies to try on each evolution
                 'num tickers': 15, # Number of tickers to optimise over
                 'num evolutions': 30, # Number of evolutions to perform
                 'min trades': 40, # Minimum trades the strategy performs per ticker
                 
                 # What to optimise, can be 'win rate', 'avg profit', 'median profit'
                 'fitness': 'avg profit',
                 
                 # Constrain to the maximum number of holding days
                 'max hold': 40,
                 
                 # Algorithm params, all 'percentages' must be less than 1
                 'keep perc': 0.4, # Percentage of top models to keep on each evolution
                 
                 # Out of sample testing and saving name
                 'out of sample test': False, # Test the optimised params on additional tickers
                 'num tickers test': 100, # Number of tickers to perform the out of sample testing
                 'save name': 'simple', # Save name for the optimised params
                 }
    
    # Run the algorithm
    strat = funcs.main(ga_config)
    
    # Perform the out of sample test
    funcs.out_sample_test(strat, ga_config)