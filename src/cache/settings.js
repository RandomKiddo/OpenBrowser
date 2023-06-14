/**
This program is protected by the MIT License © 2023 RandomKiddo
*/

var fs = require("fs");
var JSONString = fs.readFileSync("./SETTINGS.json", "utf8");
var json = JSON.parse(JSONString);

function loadDefaultSettings() {
    var incognitoSwitch = document.getElementById("incognitoSwitch");
    incognitoSwitch.checked = json.incognito;
    var forceHTTPSSwitch = document.getElementById("forceHTTPSSwitch");
    forceHTTPSSwitch.checked = json.force_https;
}

function switchChangeState(element) {
    element.checked = !element.checked;
    if (element.id.toString() === "incognitoSwitch") {
        json.incognito = !json.incognito;
        var newJSONString = JSON.stringify(json, null, 2);
        fs.writeFileSync("./SETTINGS.json", newJSONString);
    }
    JSONString = fs.readFileSync("./SETTINGS.json", "utf8");
    json = JSON.parse(JSONString);
}