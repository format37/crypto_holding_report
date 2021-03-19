## Hodler index
1. Get a table with periodic date and price of currency.   
2. Calculate column last_long_lost, how many days that date hodler has wait until last lost.   
3. Get maximum of last_long_lost - that is Hodler index positive.   
4. Calculate negative (short) index the same. maximum of last_short_lost is Hodler index negative.   
   
### Example: 
2013.11.01 you bought btc at 213.4 then price goes up and down several times, while 2015.08.24 reached 211.4, less than 213.4 for the last time.   
Next day 2015.08.24 price growth 220.5 and after that never been less than 213.4   
In this case hodler has lost 661 days, or 1.8 years. But how many maximum lost period of any btc hodler. This value is finite: 3.3863013698630136 so many years has wait the most unfortunate btc hodler bought 2013.11.29 at 1206.9 After 3.4 years he get a profit. And no one wait longer.   
3.38 is hodler-index-positive of btc

### Also
Having hodler index we can calculate:
1. Median profit of 3.4 years hodling
2. Clustering of last_long_lost to obtain most frequent lost_long periods
3. Ratio: hodler-index-positive / hodler-index-negative   
   
And then compare goods on the stock to evaluate investment attractive
