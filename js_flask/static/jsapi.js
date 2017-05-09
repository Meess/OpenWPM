//https://developer.mozilla.org/en-US/docs/Web/API/navigator

// NAVIGATOR:
    // PropertiesFirefox:
    navigator.activeVRDisplays
    navigator.appCodeName
    navigator.appName
    navigator.appVersion
    navigator.getBattery
    navigator.connection
    navigator.geolocation
    navigator.hardwareConcurrency
    navigator.javaEnabled
    navigator.language
    navigator.languages
    navigator.mimeTypes
    navigator.onLine
    navigator.oscpu
    navigator.permissions
    navigator.platform
    navigator.plugins
    navigator.product
    navigator.serviceWorker
    navigator.storage
    navigator.userAgent
    // found in paper
    navigator.maxTouchPoints

    // Non-standard:
    navigator.buildID
    navigator.cookieEnabled
    navigator.credentials
    navigator.doNotTrack
    navigator.id
    navigator.mediaDevices
    navigator.mozNotification
    navigator.webkitNotification
    navigator.mozSocial
    navigator.presentation
    navigator.productSub
    navigator.securitypolicy
    navigator.standalone
    navigator.storageQuota
    navigator.vendor
    navigator.vendorSub
    navigator.webkitPointer

    // Methods:
    // getVRDisplays()
    // navigator.getVRDisplays().then(function(displays) {
    //   // Do something with the available VR displays
    // });

    // navigator.getUserMedia() 
    navigator.getUserMedia = navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia;

    // navigator.registerContentHandler()
    try{navigator.registerContentHandler(
        "application/vnd.mozilla.maybe.feed",
        "http://www.example.tld/?foo=%s",
        "My Feed Reader");
    } catch(err) {};
    // navigator.registerProtocolHandler()
    try{navigator.registerProtocolHandler(
        "web+burger",
        "https://www.google.co.uk/?uri=%s",
        "Burger handler");
    } catch(err) {};
    try{navigator.sendBeacon('http://www.google.nl', 'foo')} 
    catch(err) {};
    navigator.taintEnabled()
    navigator.vibrate(1)

// AudioContext
var audioCtx = new AudioContext();

// RTCPeerConnection
var testRTC = new RTCPeerConnection()
testRTC.onicecandidate
// onicegatheringstatechange

// WebVR API  - NOT

//  Screen
screen.availHeight
screen.availLeft
screen.availTop
screen.availWidth
screen.colorDepth
screen.height
screen.orientation
screen.pixelDepth
screen.width


CanvasRenderingContext2D.getImageData
CanvasRenderingContext2D.fillText
CanvasRenderingContext2D.strokeText
WebGLRenderingContext.getImageData
WebGLRenderingContext.fillText
WebGLRenderingContext.strokeText
HTMLCanvasElement.toDataURL
window.TouchEvent

// https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement
// HTMLelements
var elmnt = document.getElementById("demo")
elmnt.offsetHeight
elmnt.offsetWidth
elmnt.offsetTop
elmnt.offsetParent
elmnt.style
elmnt.tabIndex
elmnt.dataset
elmnt.getBoundingClientRect
elmnt.lang
elmnt.draggable
elmnt.hidden
elmnt.itemType
elmnt.itemValue
