
const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const capturedImage = document.getElementById('captured-image');
const resultContainer = document.getElementById('result-container');


async function initCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
  } catch (error) {
    console.error('Error accessing the camera: ', error);
  }
}


function captureImage() {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
  const imageUrl = canvas.toDataURL('image/jpeg');
  capturedImage.src = imageUrl;
  resultContainer.style.display = 'block';
}


function goBack() {
  window.history.back();
}


captureButton.addEventListener('click', captureImage);


initCamera();
