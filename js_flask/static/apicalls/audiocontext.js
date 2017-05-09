// code derived from: https://www.cdn-net.com/cc.js
Array.prototype.extend = function (other_array) {
    other_array.forEach(function(v) {this.push(v)}, this);
}

var audioCtx = new AudioContext(),
    oscillator = audioCtx.createOscillator(),
    analyser = audioCtx.createAnalyser(),
    gain = audioCtx.createGain(),
    scriptProcessor = audioCtx.createScriptProcessor(4096, 1, 1),
    output = [];

gain.gain.value = 0; // Disable volume
oscillator.type = "triangle"; // Set oscillator to output triangle wave
oscillator.connect(analyser); // Connect oscillator output to analyser input
analyser.connect(scriptProcessor); // Connect analyser output to scriptProcessor input
scriptProcessor.connect(gain); // Connect scriptProcessor output to gain input
gain.connect(audioCtx.destination); // Connect gain output to audiocontext destination

scriptProcessor.onaudioprocess = function (a) {
    a = new Float32Array(analyser.frequencyBinCount);
    analyser.getFloatFrequencyData(a);
    output.extend(a);
    analyser.disconnect();
    scriptProcessor.disconnect();
    gain.disconnect();
    oscillator.stop();
    document.getElementById('result').innerHTML = output;
};

oscillator.start(0)