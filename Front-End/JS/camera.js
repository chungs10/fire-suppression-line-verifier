const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const capturedImage = document.getElementById('captured-image');
const resultContainer = document.getElementById('result-container');

let cameraActive = false;

async function toggleCamera() {
    if (!cameraActive) {
        try {
            // Clear the captured image area
            capturedImage.src = '';
            capturedImage.style.display = 'none'; // Hide the captured image
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            cameraActive = true;
            captureButton.textContent = 'Capture Image';
            // Show the capture button when camera is active
            captureButton.classList.remove('hidden');
            // Clear the captured image area when the camera is activated
            capturedImage.src = '';
            capturedImage.style.display = 'none'; // Hide the captured image
        } catch (error) {
            console.error('Error accessing the camera: ', error);
        }
    } else {
      captureImage(); // Capture image when turning off the camera
      cameraActive = false;
      captureButton.textContent = 'Activate Camera';
      // Hide the capture button when camera is inactive
      captureButton.classList.add('hidden');
  }
}

captureButton.addEventListener('click', toggleCamera);

// Function to capture image from video
function captureImage() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageUrl = canvas.toDataURL('image/jpeg');
    capturedImage.src = imageUrl;

    var box1 = document.querySelector('.box-capture');
    box1.innerHTML = ''; // Clear previous content
    box1.appendChild(capturedImage);

    capturedImage.style.display = 'block'; // Show the captured image
    resultContainer.style.display = 'block';
}

// Event listener for when video has loaded metadata
video.addEventListener('loadedmetadata', function() {
    // Show the capture button when video metadata is loaded
    captureButton.classList.remove('hidden');
});
