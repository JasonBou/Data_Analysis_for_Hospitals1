import pandas as pd

def add_records(olympics):
    new_countries = pd.Series({2021: 'Tokyo', 2024: 'Paris', 2028: 'Los Angeles'})
    return pd.concat([olympics, new_countries])

