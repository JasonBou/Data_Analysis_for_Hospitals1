import pandas as pd

def create_series(capitals):
    capital_series = pd.Series(capitals, name='Capitals of the world')
    return capital_series
    #pass
#capitals = {'Czech Republic': 'Prague',
#            'Russia': 'Moscow',
#            'Australia': 'Canberra'}
#capital_series = pd.Series(capitals, name ='Capital of the world')