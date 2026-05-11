# Hair AI Recommendation System

AI-Powered Hairstyle Recommendation & Hair Health Assessment System - Full Stack Production

## 🎯 Features

### 1. Face Shape Detection & Hairstyle Recommendation
- Real-time face shape analysis from uploaded/camera photos
- Multi-category hairstyle recommendations (modern, futuristic, old, present, old_age)
- Compatibility scoring and style previews

### 2. Hair Health Assessment
- Multi-image analysis for comprehensive hair health evaluation
- Detection: hair thickness, diseases, scalp conditions
- AI-powered product recommendations
- Detailed health report generation

### 3. Appointment Booking
- Schedule appointments with hairstylists
- Track appointment status
- Integration with recommendation results

## 🛠️ Technology Stack

**Backend**: FastAPI + Python 3.10+
**Database**: PostgreSQL (Free Tier)
**ML Framework**: TensorFlow/Keras (Optimized)
**Frontend**: HTML5 + CSS3 + JavaScript + React
**Cloud**: Google Cloud Platform (Free Tier)
- Cloud Run: Serverless backend
- Cloud SQL: PostgreSQL database
- Cloud Storage: Model storage

## 📁 Project Structure

```
hair-ai-system/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── api/
│   │   ├── models/
│   │   ├── ml/
│   │   ├── services/
│   │   ├── middleware/
│   │   ├── utils/
│   │   └── database/
│   ├── training/
│   ├── notebooks/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   ├── components/
│   └── Dockerfile
├── datasets/
│   └── download_datasets.py
├── deployment/
│   ├── cloud/
│   ├── kubernetes/
│   └── scripts/
├── tests/
├── docs/
├── .github/workflows/
├── docker-compose.yml
└── setup.sh
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL
- Docker & Docker Compose
- Node.js (optional, for frontend enhancements)

### Local Development

1. **Clone repository**
```bash
git clone https://github.com/bhukyaakash/hair-ai-system.git
cd hair-ai-system
```

2. **Setup backend**
```bash
cd backend
pip install -r requirements.txt
```

3. **Setup database**
```bash
cd ../deployment/scripts
bash setup_db.sh
```

4. **Run locally with Docker Compose**
```bash
cd ../.. 
docker-compose up --build
```

5. **Access application**
- Frontend: http://localhost:3000
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📊 ML Models

### Face Shape Classifier
- Base: EfficientNetB0
- Input: Face image
- Output: Shape classification (round, oval, square, heart, oblong, diamond)
- Target Accuracy: >85%

### Hairstyle Recommender
- Input: Face shape + user preferences
- Output: Top 5 hairstyle recommendations with categories
- Categories: Modern, Futuristic, Old, Present, Old_Age
- Target Accuracy: >90%

### Hair Health Analyzer
- Input: Multiple hair/scalp images
- Detects: Hair thickness, health status, issues
- Output: Health report with scores
- Target Accuracy: >80%

### Disease Detector
- Detects: Alopecia, dandruff, psoriasis, seborrheic dermatitis, etc.
- Output: Condition identification + severity
- Target Accuracy: >85%

## 🏋️ Training Models on HPC

1. **Download datasets**
```bash
cd datasets
python download_datasets.py
```

2. **Run training scripts**
```bash
cd ../backend/training
python train_face_shape.py
python train_hairstyle.py
python train_hair_health.py
python train_disease_detector.py
```

3. **Models will be saved** in `backend/app/ml/saved_models/`

## ☁️ Deployment

### Google Cloud Run (Recommended - Free Tier)

1. **Install Google Cloud SDK**
```bash
curl https://sdk.cloud.google.com | bash
gcloud init
```

2. **Deploy**
```bash
bash deployment/scripts/deploy.sh
```

See [DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📚 Documentation

- [API Documentation](docs/API_DOCUMENTATION.md)
- [Architecture Guide](docs/ARCHITECTURE.md)
- [Setup Guide](docs/SETUP_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md)
- [Model Training Guide](docs/MODEL_TRAINING_GUIDE.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🧪 Testing

```bash
pytest tests/
```

## 📊 Performance Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Face Shape Accuracy | >85% | In Development |
| Hairstyle Accuracy | >90% | In Development |
| Hair Health Accuracy | >80% | In Development |
| Inference Time | <1s | In Development |
| API Response | <2s | In Development |
| Model Size | <100MB | In Development |
| Test Coverage | >80% | In Development |

## 🔄 CI/CD

GitHub Actions workflows for:
- Backend testing and linting
- Frontend building
- Automated deployment to Google Cloud Run
- Docker image building and pushing

## 📝 Datasets Used

- trainingdatapro/hair-detection-and-segmentation-dataset
- amitvkulkarni/hair-health
- kavyasreeb/hair-type-dataset
- ninaflirp/hair-salon-dataset
- sundarannamalai/hair-diseases
- tapakah68/face-segmentation
- niten19/face-shape-dataset
- asher213/images-transformations-and-cv2-and-dlib-features
- brijlaldhankour/hair-loss-dataset
- riotulab/skin-cancer-hair-removal
- pranavchandane/scut-fbp5500-v2-facial-beauty-scores
- kutayahin/glass-match-ai-faces

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 👨‍💻 Author

Bhukyaakash - AI/ML Developer

## 📧 Contact

For questions or support, please open an issue or contact the maintainers.

## 🙏 Acknowledgments

- TensorFlow/Keras team for ML frameworks
- FastAPI for backend framework
- Google Cloud for cloud infrastructure
- Kaggle for datasets
