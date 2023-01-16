/**
This program is protected by the MIT License © 2023 RandomKiddo
*/

var fs = require("fs");

function loadDefaultSettings() {
    fs.readFile("./SETTINGS.json", "utf8", (err, jsonString) => {
        if (err) {
            console.log("File read error: ", err);
            return;
        }
        try {
            var data = JSON.parse(jsonString);
        } catch (err) {
            console.log(err);
            return;
        }
        var incognitoSwitch = document.getElementById("incognitoSwitch");
        incognitoSwitch.checked = data.incognito;
    });
}

function switchChangeState(element) {
    element.checked = !element.checked;
    fs.readFile("./SETTINGS.json", "utf8", (err, jsonString) => {
        if (err) {
            console.log("File read error: ", err);
            return;
        }
        // write to file
    });
}