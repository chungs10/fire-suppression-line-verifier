document.addEventListener('DOMContentLoaded', function () {
    var loader = document.getElementById('canvas');
    loader.style.display = "none";

    // Create an overlay to block user interaction
    var overlay = document.createElement('div');
    overlay.id = 'overlay';
    overlay.style.position = 'fixed';
    overlay.style.top = 0;
    overlay.style.left = 0;
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    overlay.style.zIndex = 9999; // Ensure the overlay is on top of all other elements
    overlay.style.display = 'none'; // Hide the overlay initially
    document.body.appendChild(overlay);

    // load loader animations to buttons
    var analyzeButton = document.getElementById('analyze');
    var captureTemplateButton = document.getElementById('captureImage');
    var liveAnalysisButton = document.getElementById('liveAnalysis');

    function showLoaderForTime(seconds) {
        return function() {
            console.log("Runs");
            var loader = document.getElementById('canvas');
            loader.style.display = "block";
            overlay.style.display = 'block';
            setTimeout(function() {
                loader.style.display = "none";
                overlay.style.display = 'none';
            }, seconds * 1000);
        }
    }

    analyzeButton.addEventListener('click', showLoaderForTime(0.5));
    captureTemplateButton.addEventListener('click', showLoaderForTime(8));
    liveAnalysisButton.addEventListener('click', showLoaderForTime(10));
});

var canvasLoader = function () {

    var self = this;
    window.requestAnimFrame = function () { return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function (a) { window.setTimeout(a, 1E3 / 60) } }();

    self.init = function () {
        self.canvas = document.getElementById('canvas');
        self.ctx = self.canvas.getContext('2d');
        self.ctx.lineWidth = .5;
        self.ctx.strokeStyle = 'rgba(0,0,0,.75)';
        self.count = 75;
        self.rotation = 270 * (Math.PI / 180);
        self.speed = 6;
        self.canvasLoop();
    };

    self.updateLoader = function () {
        self.rotation += self.speed / 100;
    };

    self.renderLoader = function () {
        self.ctx.save();
        self.ctx.globalCompositeOperation = 'source-over';
        self.ctx.translate(125, 125);
        self.ctx.rotate(self.rotation);
        var i = self.count;
        while (i--) {
            self.ctx.beginPath();
            self.ctx.arc(0, 0, i + (Math.random() * 35), Math.random(), Math.PI / 3 + (Math.random() / 12), false);
            self.ctx.stroke();
        }
        self.ctx.restore();
    };

    self.canvasLoop = function () {
        requestAnimFrame(self.canvasLoop, self.canvas);
        self.ctx.globalCompositeOperation = 'destination-out';
        self.ctx.fillStyle = 'rgba(0,0,0,.03)';
        self.ctx.fillRect(0, 0, 250, 250);
        self.updateLoader();
        self.renderLoader();
    };

};

var loader = new canvasLoader();
loader.init();