from ga import funcs

if __name__ == "__main__":
    
    ga_config = {
                 # Basic controls for the genetic algo
                 'num strats': 40, # Number of strategies to try on each evolution
                 'num tickers': 20, # Number of tickers to optimise over
                 'num evolutions': 100, # Number of evolutions to perform
                 'keep perc': 0.3, # Percentage of top models to keep on each evolution
                 
                 # What to optimise, can be 'win rate', 'avg profit', 'median profit'
                 'fitness': 'avg profit',
                 
                 # Constraints
                 'max hold': 25, # Maximum number of holding days
                 'min trades': 50, # Minimum trades the strategy performs per ticker
                 
                 # Out of sample testing and saving name
                 'num tickers test': 200, # Number of tickers to perform the out of sample testing
                 'save name': 'avg profit', # Save name for the optimised params
                 }

    # Run the algorithm
    strat = funcs.main(ga_config)

    # Perform the out of sample test
    funcs.out_sample_test(strat, ga_config)