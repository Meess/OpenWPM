// sample code derived from https://www.browserleaks.com/canvas#how-does-it-work

// Text with lowercase/uppercase/punctuation symbols
var txt = "BrowserLeaks,com <canvas> 1.0";

var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext("2d");
ctx.textBaseline = "top";
// The most common type
ctx.font = "14px 'Arial'";
ctx.textBaseline = "alphabetic";
ctx.fillStyle = "#f60";
ctx.fillRect(125,1,62,20);
// Some tricks for color mixing to increase the difference in rendering
ctx.fillStyle = "#069";
ctx.fillText(txt, 2, 15);
ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
ctx.fillText(txt, 4, 17);
var pre = document.getElementById("canvasDataURL");
pre.innerHTML = canvas.toDataURL();
