/*

Problem Link: https://www.hackerrank.com/challenges/js10-date/problem
---------------------------------------------------------------------

*/


// Solution: 
// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"

function getDayName(dateString) {
    let dayName;
    // Write your code here

    dateString = new Date(dateString);
    dayName = dateString.getDay();

    if (dayName == 0)
        dayName = "Sunday";
    else if (dayName == 1)
        dayName = "Monday";
    else if (dayName == 2)
        dayName = "Tuesday";
    else if (dayName == 3)
        dayName = "Wednesday";
    else if (dayName == 4)
        dayName = "Thursday";
    else if (dayName == 5)
        dayName = "Friday";
    else if (dayName == 6)
        dayName = "Saturday";

    return dayName;
}
