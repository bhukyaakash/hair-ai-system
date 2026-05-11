#!/bin/bash

echo "🚀 Setting up Hair AI Recommendation System..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "${YELLOW}Checking Python version...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "${RED}Python 3 is not installed. Please install Python 3.10+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "${GREEN}✓ Python $PYTHON_VERSION found${NC}"

# Create virtual environment
echo "${YELLOW}Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate
echo "${GREEN}✓ Virtual environment created${NC}"

# Install backend dependencies
echo "${YELLOW}Installing backend dependencies...${NC}"
cd backend
pip install --upgrade pip
pip install -r requirements.txt
echo "${GREEN}✓ Backend dependencies installed${NC}"
cd ..

# Create necessary directories
echo "${YELLOW}Creating necessary directories...${NC}"
mkdir -p datasets/raw
mkdir -p datasets/processed
mkdir -p backend/app/ml/saved_models
mkdir -p uploads
echo "${GREEN}✓ Directories created${NC}"

# Create .env file
echo "${YELLOW}Creating .env file...${NC}"
if [ ! -f .env ]; then
    cp .env.example .env
    echo "${GREEN}✓ .env file created (edit with your configuration)${NC}"
else
    echo "${YELLOW}⚠ .env file already exists${NC}"
fi

echo ""
echo "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "${YELLOW}Next steps:${NC}"
echo "1. Edit .env file with your configuration"
echo "2. Download datasets: python datasets/download_datasets.py"
echo "3. Train models: cd backend/training && python train_face_shape.py"
echo "4. Run locally: docker-compose up --build"
echo ""
echo "${YELLOW}For more information, see docs/SETUP_GUIDE.md${NC}"
