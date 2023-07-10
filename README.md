# HVACMapperReducer
Mapper and Reducer programs using Google Cloud Platform and
Hadoop to aggregate and identify HVAC data. 
#
The first mapper and reducer find the 3 worst HVAC systems, based on all available data (,the greatest
difference between desired temperature and actual temperature).
The second mapper and reducer find the 3 hottest buildings, based on all available data, during normal business hours.
The third mapper and redcuer find the average temperature in each of the 3 hottest buildings as a function of time-of-day.
