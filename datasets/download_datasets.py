"""Kaggle Dataset Downloader"""

import os
import kaggle
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kaggle datasets to download
DATASETS = [
    "trainingdatapro/hair-detection-and-segmentation-dataset",
    "amitvkulkarni/hair-health",
    "kavyasreeb/hair-type-dataset",
    "ninaflirp/hair-salon-dataset",
    "sundarannamalai/hair-diseases",
    "tapakah68/face-segmentation",
    "niten19/face-shape-dataset",
    "asher213/images-transformations-and-cv2-and-dlib-features",
    "brijlaldhankour/hair-loss-dataset",
    "riotulab/skin-cancer-hair-removal",
    "pranavchandane/scut-fbp5500-v2-facial-beauty-scores",
    "kutayahin/glass-match-ai-faces"
]


def download_datasets():
    """
    Download all datasets from Kaggle
    """
    # Create directories
    Path("datasets/raw").mkdir(exist_ok=True, parents=True)
    
    # Check Kaggle credentials
    if not os.path.exists(os.path.expanduser("~/.kaggle/kaggle.json")):
        logger.error("❌ Kaggle credentials not found!")
        logger.error("Please setup Kaggle API credentials:")
        logger.error("1. Go to https://www.kaggle.com/settings/account")
        logger.error("2. Click 'Create New API Token'")
        logger.error("3. Move kaggle.json to ~/.kaggle/")
        return
    
    # Download datasets
    for dataset in DATASETS:
        try:
            logger.info(f"📥 Downloading {dataset}...")
            kaggle.api.dataset_download_files(
                dataset,
                path="datasets/raw",
                unzip=True
            )
            logger.info(f"✅ Downloaded {dataset}")
        except Exception as e:
            logger.warning(f"⚠️  Failed to download {dataset}: {e}")
    
    logger.info("\n🎉 Dataset download completed!")
    logger.info("📂 Datasets saved in: datasets/raw/")


if __name__ == "__main__":
    download_datasets()
