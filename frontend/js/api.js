const API_BASE = window.API_BASE || 'http://localhost:8000/api/v1';

async function getRecommendations(faceShape) {
  const response = await fetch(`${API_BASE}/hairstyles/recommend?face_shape=${encodeURIComponent(faceShape)}`);
  return response.json();
}
