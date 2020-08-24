# SQLAlchemy-Challenge

Bonus Challenges:
# 1:  I used the independent t-test as the test is comparing the tempurature variation across two different months or seasons (which you expect would be different), rather comparing variations within the same month across different years (which you would normally expect to be the same).  The resulting t-test had a very high t-score, indicating that the difference between the groups is much higher than within the group.  The p-score is effectively 0, indicating that the results are statistically significant, or unlikely to be due to chance.

# 2:   

Notes:
- Output for precipation do not match images, but the descriptive statistics total 2,000 + items, which doesn't make sense if the data is grouped by date to come up with an average daily rainfall
- Try eliminating the group by date and just have it plot the data by day
- Should data be for most active station for last year or all years in jupyter


Log
8/23:
- Inputing initial analysis into Flask API
- Precipitation analysis requires list of dates with dates as keys and prepcip as values.  Original query has multiple datapoints by station for each date.  Setting up Precip API as follows:
-> Jsonify and review query results -- expting 2,000+ dates over one year time period (output as expected)
-> Loop through results; create date list and append for each unique date; query was sorted in ascending order, so results should be sorted; jsonify and review
-> Nested loop through date list; for each date in date_list, loop through all rows of results; create date_temp dictionary; if results.date = date, append date_temp dictionary
- NOTE:  Before developing above, I discovered the defaultdict function, which greatly simplified the looping  

8/22:
- Solved base Precipitation and Station analyses
- Majority of time spent familiarizing myself with reflection and session commands of SQLAlchemy.  Relatively straightforward once overcoming the initial hurdle of database reflection.

