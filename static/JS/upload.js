document.addEventListener('DOMContentLoaded', function () {
  var uploadButton = document.getElementById('upload');
  var analyzeButton = document.getElementById('analyze');
  var captureTemplateButton = document.getElementById('captureImage');
  var liveAnalysisButton = document.getElementById('liveAnalysis');

  uploadButton.addEventListener('click', uploadImage);
  if (analyzeButton.classList.contains('simple')) {
    analyzeButton.addEventListener('click', analyzeImageSimple);
  } else {
    analyzeButton.addEventListener('click', analyzeImage);
  }
  captureTemplateButton.addEventListener('click', captureTemplate);
  liveAnalysisButton.addEventListener('click', liveAnalysis)
});

function uploadImage() {
  var input = document.createElement('input');
  input.type = 'file';
  input.accept = 'image/*';
  input.click();

  input.onchange = function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
      var image = new Image();
      image.src = e.target.result;

      var box1 = document.querySelector('.box-capture');
      box1.innerHTML = ''; // Clear previous content
      box1.appendChild(image);
    };

    reader.readAsDataURL(file);
  };
}

function getCurrentDateTime() {
  var currentDate = new Date();

  // Get the date components
  var year = currentDate.getFullYear();
  var month = ('0' + (currentDate.getMonth() + 1)).slice(-2); // Months are zero-based
  var day = ('0' + currentDate.getDate()).slice(-2);

  // Get the time components
  var hours = ('0' + currentDate.getHours()).slice(-2);
  var minutes = ('0' + currentDate.getMinutes()).slice(-2);
  var seconds = ('0' + currentDate.getSeconds()).slice(-2);

  // Construct the date and time string in the desired format
  var dateTimeString = year + '-' + month + '-' + day + '_' + hours + '-' + minutes + '-' + seconds;

  return dateTimeString;
}

function captureTemplate() {
  fetch('/captureTemplate', {
    method: 'POST'
  });
}

function liveAnalysis() {
  fetch('/liveAnalysis', {
    method: 'POST'
  });
}

function analyzeImage() {
  var box1 = document.querySelector('.box-capture');
  var image = box1.querySelector('img');
  var filePath = `./static/database/unprocessed/${getCurrentDateTime()}.jpg`

  if (image) {
    //console.log("Analyzing image:", image.src);
    var formData = new FormData();
    formData.append('imagePath', filePath);
    formData.append('base64image', image.src);

    // Make a POST request to the Flask API
    fetch('/mlAnalysis', {
      method: 'POST',
      body: formData
    })
      .then(response => response.text())
      .then(result => {
        updateFireState(result);
        displayImage(result);
        // Record the result here
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } else {
    console.log("No image found to analyze.");
  }
}

function analyzeImageSimple() {
  var box1 = document.querySelector('.box-capture');
  var image = box1.querySelector('img');
  var filePath = `./static/database/unprocessed/${getCurrentDateTime()}.jpg`

  if (image) {
    //console.log("Analyzing image:", image.src);
    var formData = new FormData();
    formData.append('imagePath', filePath);
    formData.append('base64image', image.src);

    // Make a POST request to the Flask API
    fetch('/simpleAnalysis', {
      method: 'POST',
      body: formData
    })
      .then(response => response.text())
      .then(result => {
        displayImage(result);
        // Record the result here
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } else {
    console.log("No image found to analyze.");
  }
}

function displayImage(filePath) {
  const video = document.getElementById('video');
  var imageContainer = document.getElementsByClassName("box-result")[0];
  imageContainer.innerHTML = ''; // Clear previous content

  var img = new Image();
  img.src = filePath;
  img.style.width = "300px";
  imageContainer.appendChild(img);
}

function confirmFireAction() {
  // Set confirmation flag for fire action in localStorage
  localStorage.setItem('fireConfirmation', 'confirmed')
}

function confirmStrapAction() {
  // Set confirmation flag for strap action in localStorage
  localStorage.setItem('strapConfirmation', 'confirmed')
}

function confirmWeightAction() {
  // Set confirmation flag for weight action in localStorage
  localStorage.setItem('weightConfirmation', 'confirmed')
}

function updateFireState(filePath) {
  const parts = filePath.split('__');
  if (parts.length >= 2) {
      const state = parts[1].split('.');
      if(state[0] == "pass") {
        localStorage.setItem('fireConfirmation', 'confirmed');
      } else {
        localStorage.setItem('fireConfirmation', 'unconfirmed')
      }
  }
}