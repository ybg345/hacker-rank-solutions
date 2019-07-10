/*

Problem Link: https://www.hackerrank.com/challenges/js10-switch/problem
-----------------------------------------------------------------------

*/


// Solution: 
function getLetter(s) {
    let letter;
    switch (s[0]) { 
        case "a":
        case "e":
        case "i":
        case "o":
        case "u":
            letter = "A";
            return letter;
            break;

        case "b":
        case "c":
        case "d":
        case "f":
        case "g":
            letter = "B";
            return letter;
            break;

        case "h":
        case "j":
        case "k":
        case "l":
        case "m":
            letter = "C";
            return letter;
            break;

        default:
            letter = "D";
            return letter;
    };
    
    return letter;
}
