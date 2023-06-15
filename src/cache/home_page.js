/**
This program is protected by the MIT License © 2023 RandomKiddo
*/

function navigate() {
    var value = document.forms["searchPlaceholder"]["gsearch"].value;
    if (value.toString().startsWith("www") || value.toString().startsWith("http")) {
        window.location = value.toString()
    } else {
        window.location = "https://duckduckgo.com/?q=" + value.toString();
    }
}