document.addEventListener('DOMContentLoaded', function() {
    var captureButton = document.getElementById('capture');
    var analyzeButton = document.getElementById('analyze');
  
    captureButton.addEventListener('click', captureImage);
    analyzeButton.addEventListener('click', analyzeImage);
  });
  
  function captureImage() {
    var input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.click();
  
    input.onchange = function(event) {
      var file = event.target.files[0];
      var reader = new FileReader();
  
      reader.onload = function(e) {
        var image = new Image();
        image.src = e.target.result;
  
        var box1 = document.querySelector('.box-capture');
        box1.innerHTML = '';
        box1.appendChild(image);
      };
  
      reader.readAsDataURL(file);
    };
  }
  
  function analyzeImage() {
    var box1 = document.querySelector('.box-capture');
    var image = box1.querySelector('img');
    
    if (image) {
      console.log("Analyzing image:", image.src);
      // No Analysis Code yet
    } else {
      console.log("No image found to analyze.");
    }
  }
  