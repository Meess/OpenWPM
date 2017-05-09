// https://www.w3schools.com/xml/dom_httprequest.asp
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Action to be performed when the document is read;
    }
};
xhttp.open("GET", "filename", true);
xhttp.send();