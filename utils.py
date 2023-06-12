import numpy as np


# Async function to get real time prices from Binance API
async def get_price(session, url):
    async with session.get(url) as response:
        return await response.json()


# Extract the last 60 prices and calculate the correlation between the two sets of prices
def calculate_correlation(eth_prices, btc_prices):
    eth_prices_array = np.array(eth_prices[-60:])
    btc_prices_array = np.array(btc_prices[-60:])
    return np.corrcoef(eth_prices_array, btc_prices_array)[0, 1]
