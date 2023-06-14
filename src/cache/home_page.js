/**
This program is protected by the MIT License © 2023 RandomKiddo
*/

var emptySearch = document.getElementById("emptySearch");
emptySearch.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        //todo talk to Python to search
    }
});