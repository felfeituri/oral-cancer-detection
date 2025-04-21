# Oral Cancer Detection using Clinical and Histopathological Images

This project explores the use of deep learning to support early detection of oral cancer by analyzing two complementary data types: clinical photographs of the oral cavity and histopathological slide images. The goal is to train machine learning models that can help distinguish between healthy, precancerous, and cancerous oral tissues to assist in early diagnosis, especially in low-resource settings.

# Datasets Used

## Clinical Images

* Annotated Oral Cavity Images: 3,000 mobile-captured images categorized into healthy, benign, potentially malignant, and cancerous.

* Kaggle – Oral Cancer Dataset: 500 oral cancer and 450 non-cancer images.

* Kaggle – Oral Cancer (Lips and Tongue): Focused images of oral subregions.

## Histopathological Images

* ORCHID Database: A curated dataset of oral cancer histology images:
** Zenodo Record 12636426 – training set
**Zenodo Record 12646943 – validation/test set

## Objective

Develop and evaluate convolutional neural networks (CNNs) to classify image data into diagnostic categories and explore model performance across datasets. The aim is to provide a reproducible ML workflow that can support early detection strategies and augment clinical decision-making.

How to Reproduce

# Clone the repo
```bash
git clone https://github.com/yourusername/oral-cancer-detection.git
cd oral-cancer-detection
```

# Create the environment
```bash
conda env create -f environment.yml conda activate oral-cancer-env
```

# Project Structure
```plaintext
notebooks/       # Development notebooks for training & evaluation
src/             # Preprocessing and training scripts
data/            # DO NOT upload large files; placeholders only
models/          # Trained model outputs (add to .gitignore)
```

# Contact

For questions, contact Fadwa Elfeituri – ffe7@georgetown.edu
