import aiohttp
import asyncio

from config import ETHUSDT_URL, BTCUSDT_URL, INTERVAL_DELAY, RETRY_DELAY
from utils import get_price, calculate_correlation


async def main():

    # Initialize the previous prices of both pairs to a high number
    last_eth_price = last_btc_price = 10000

    # Initialize empty lists to save the prices of both pairs
    eth_prices = []
    btc_prices = []

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                eth_response = await get_price(session, ETHUSDT_URL)
                print(eth_response)
                btc_response = await get_price(session, BTCUSDT_URL)
                print(btc_response)

            # Parse the price from the response and append it to the list.
            current_eth_price = float(eth_response['price'])
            eth_prices.append(current_eth_price)
            print(eth_prices)

            current_btc_price = float(btc_response['price'])
            btc_prices.append(current_btc_price)
            print(btc_prices)

            # If there are more than 60 prices in the list (we have more than 1 hour of data)
            if len(eth_prices) > 60 and len(btc_prices) > 60:

                # Calculate the percentage change in price over the last hour
                eth_price_change = (current_eth_price - last_eth_price) / last_eth_price
                btc_price_change = (current_btc_price - last_btc_price) / last_btc_price

                # Calculate the correlation between the two sets of prices
                correlation = calculate_correlation(eth_prices, btc_prices)
                print(correlation)

                # the ETH price change by the correlation with the BTC price change.
                no_btc_eth_change = eth_price_change - correlation * btc_price_change
                print(no_btc_eth_change)

                # if the total price change is more than 1%, print a message.
                if no_btc_eth_change > 0.01:
                    print(
                        f"The price of ETHUSDT has increased by 1% in the last hour. Current price:: {current_eth_price}")
                elif no_btc_eth_change < -0.01:
                    print(
                        f"The price of ETHUSDT has decreased by 1% in the last hour. Current price: {current_eth_price}")

                last_eth_price = current_eth_price
                last_btc_price = current_btc_price

            await asyncio.sleep(INTERVAL_DELAY)

        except Exception as e:
            print(f"A '{e}' error has occurred")
            await asyncio.sleep(RETRY_DELAY)


if __name__ == "__main__":
    asyncio.run(main())
