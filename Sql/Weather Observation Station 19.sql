# Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-19/problem
# ------------------------------------------------------------------------------------------


SELECT ROUND(SQRT(((MAX(LONG_W) - MIN(LONG_W)) * (MAX(LONG_W) - MIN(LONG_W))) + ((MAX(LAT_N) - MIN(LAT_N)) * (MAX(LAT_N) - MIN(LAT_N)))), 4) FROM STATION;