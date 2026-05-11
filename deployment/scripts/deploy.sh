#!/bin/bash

# Hair AI System Deployment Script

set -e

echo "🚀 Deploying Hair AI System to Google Cloud Run..."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check prerequisites
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ Google Cloud SDK not found. Please install it first.${NC}"
    exit 1
fi

if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker not found. Please install it first.${NC}"
    exit 1
fi

# Configuration
PROJECT_ID=$(gcloud config get-value project)
SERVICE_NAME="hair-ai-backend"
REGION="us-central1"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

echo -e "${YELLOW}Configuration:${NC}"
echo "Project ID: $PROJECT_ID"
echo "Service Name: $SERVICE_NAME"
echo "Region: $REGION"
echo "Image: $IMAGE_NAME"
echo ""

# Build Docker image
echo -e "${YELLOW}Building Docker image...${NC}"
cd backend
docker build -t ${IMAGE_NAME}:latest -t ${IMAGE_NAME}:$(date +%Y%m%d_%H%M%S) .
cd ..
echo -e "${GREEN}✓ Docker image built${NC}"

# Configure Docker for GCP
echo -e "${YELLOW}Configuring Docker authentication...${NC}"
gcloud auth configure-docker
echo -e "${GREEN}✓ Docker configured${NC}"

# Push image to GCR
echo -e "${YELLOW}Pushing image to Google Container Registry...${NC}"
docker push ${IMAGE_NAME}:latest
echo -e "${GREEN}✓ Image pushed${NC}"

# Deploy to Cloud Run
echo -e "${YELLOW}Deploying to Cloud Run...${NC}"
gcloud run deploy ${SERVICE_NAME} \
    --image ${IMAGE_NAME}:latest \
    --region ${REGION} \
    --platform managed \
    --memory 1Gi \
    --cpu 1 \
    --allow-unauthenticated \
    --set-env-vars ENVIRONMENT=production,DEBUG=False \
    --timeout 300s \
    --concurrency 80

echo -e "${GREEN}✓ Deployment completed${NC}"

# Get service URL
SERVICE_URL=$(gcloud run services describe ${SERVICE_NAME} --region ${REGION} --format='value(status.url)')
echo ""
echo -e "${GREEN}✅ Deployment successful!${NC}"
echo ""
echo -e "${YELLOW}Service URL:${NC} ${SERVICE_URL}"
echo -e "${YELLOW}API Docs:${NC} ${SERVICE_URL}/docs"
echo ""
