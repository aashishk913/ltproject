from upstox_api.api import *
from datetime import datetime
import time
import pandas as pd
import numpy as np

u = Upstox ('KEY', 'PSWD')
u.get_master_contract('NSE_EQ')
stocklist = []
x = 0
myarray = []
mysig = []
for i in range(0,360):
    x = u.get_ohlc(u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'), OHLCInterval.Minute_1, datetime.strptime('05/09/2019', '%d/%m/%Y').date(), datetime.strptime('05/09/2019', '%d/%m/%Y').date())
    df = pd.DataFrame.from_dict(x)
    print(df['close'].tail(1))
    stocklist.append(df['close'].tail(1))
    data = pd.DataFrame(stocklist) 
    exp2 = data.ewm(span=26, adjust=False).mean()
    exp3 = data.ewm(span=9, adjust=False).mean()
    exp = data.ewm(span=12, adjust=False).mean()
    macd = exp-exp2
    sig = macd.ewm(span=9, adjust=False).mean()
    myarray = np.asarray(macd)
    mysig = np.asarray(sig)
    print(myarray)
    print("mysig")
    print(mysig)
    if i > 1:
        print("in if ")
        if myarray[-2] > mysig[-2] and myarray[-1] < mysig[-1] :  #previous candle average #instant candle average                                                      
            print("**selll signal**")
            print("old macd ",myarray[-2] , " old signa" ,mysig[-2])
            print("new macd ",myarray[-1] , " new signa" ,mysig[-1])  
            if x < 1 :
                print(u.place_order(TransactionType.Sell,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
                x = x  + 1
            else:
                print(u.place_order(TransactionType.Sell,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
                print("another trade")
                
                print(u.place_order(TransactionType.Sell,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
                
                
                          
        if myarray[-2] < mysig[-2] and myarray[-1] > mysig[-1]:                    #previous candle average                                                                       #instant candle average
            print("**buyyy signal**")
            print("old macd ",myarray[-2] , " old signa" ,mysig[-2])
            print("new macd ",myarray[-1] , " new signa" ,mysig[-1])
                    
            if x < 1 :
                print(u.place_order(TransactionType.Buy,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
                x = x  + 1
            else:
                print(u.place_order(TransactionType.Buy,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
                print("another trade")
                
                print(u.place_order(TransactionType.Buy,  #transaction_type
                        u.get_instrument_by_symbol('NSE_EQ', 'YESBANK'),  #instrument
                          1,  # quantity
                          OrderType.Market,  # order_type
                          ProductType.Intraday,  # product_type
                          0.0,  # price
                          None,  # trigger_price
                          0,  # disclosed_quantity
                          DurationType.DAY, # duration
                          None, # stop_loss
                          None, # square_off
                          None )# trailing_ticks
                      )
    time.sleep(60)
