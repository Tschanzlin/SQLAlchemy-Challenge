# SQLAlchemy-Challenge

Homework notes:
For the precipitation analysis chart and panda output, I am generating different output than the image files.  It was unclear whether the assignment was calling for total or average rainfall across each station for each day, so I chose to go with total rainfall and used the func.sum(Measurement.prcp) function.  I would note that the image file for the stored dataframe notes a count of 2021 vs. my 365 count.  I used a groupby function on the Measurement.date to create 365 days of data as requested, so my results make sense to me logically even though they do not match.

Originally for bonus challenge #1, I created two separate SQLAlchemy queries, formatted the data for dataframes, and joined the dataframes.  After reviewing, I wanted to re-run with a simpler, joined SQLAlchemy query.  I realized the first attempt (separate queries) was pulling station info from stations with no precip data.  The second attempt with the joined query solved this and I think the resulting code is cleaner as well.  I left the original effort as Part I(B) for reference.

For bonus challenge #2, I used the independent t-test as the test is comparing the tempurature variation across two different months or seasons (which you expect to be different), rather comparing variations within the same month across different years (which you expect to be similar).  The resulting t-test had a very high t-score, indicating that the difference between the groups is much higher than within the group.  The p-score is effectively 0, indicating that the results are statistically significant, or unlikely to be due to chance.

The Flask assignment in python was relative straightforward, with the exception of the Precipitation route, which created a list of precip values for each date.  I wanted to format the file with each data as a Key and the various measurements as a list of vales.  I used the "defaultdict" function to do this rather than creating a loop.  It would be interesting to explore other ways of storing the data by adding an additional key for the station.
 
Log
8/25:
- Clean-up code; check output

8/24:
- Completed all analysis

8/23:
- Inputing initial analysis into Flask API
- Precipitation analysis requires list of dates with dates as keys and prepcip as values.  - Original query has multiple datapoints by station for each date.  Setting up Precip API as follows:
-> Jsonify and review query results -- expting 2,000+ dates over one year time period (output as expected)
-> Loop through results; create date list and append for each unique date; query was sorted in ascending order, so results should be sorted; jsonify and review
-> Nested loop through date list; for each date in date_list, loop through all rows of results; create date_temp dictionary; if results.date = date, append date_temp dictionary
- NOTE:  Before developing above, I discovered the defaultdict function, which greatly simplified the looping  

8/22:
- Solved base Precipitation and Station analyses
- Majority of time spent reviewing reflection and session commands of SQLAlchemy.  Relatively straightforward once overcoming the initial hurdle of database reflection.

