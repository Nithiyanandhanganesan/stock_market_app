from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest , LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('PKJZG4HU09SX27MF14E3', '09wNdAU9zDZKbEuthtGzsqOCuIxqjkx6AYXZnFzs')

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))


# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)


# search for AAPL and check whether we can trade this in alpaca
aapl_asset = trading_client.get_asset('AAPL')

if aapl_asset.tradable:
    print('We can trade AAPL.')


#####ORDERS##########

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# preparing limit order
limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# # Limit order
# limit_order = trading_client.submit_order(
#                 order_data=limit_order_data
#               )

#Short orders can also be placed for securities which you do not hold an open long position in.

# preparing orders
# market_order_data = MarketOrderRequest(
#                     symbol="SPY",
#                     qty=1,
#                     side=OrderSide.SELL,
#                     time_in_force=TimeInForce.GTC
#                     )
#
# # Market order
# market_order = trading_client.submit_order(
#                 order_data=market_order_data
#                )