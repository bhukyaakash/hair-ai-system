async function startCamera(videoElement) {
  if (!navigator.mediaDevices) return null;
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  videoElement.srcObject = stream;
  return stream;
}
