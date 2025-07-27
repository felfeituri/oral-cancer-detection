# Oral Cancer Detection Using Deep Learning

This project explores the application of deep learning to support early detection of oral cancer using clinical oral cavity photographs. A custom convolutional neural network (CNN) was developed to distinguish between cancerous and non-cancerous lesions based on images and structured metadata, simulating the real-world diagnostic workflow.

> Course: HIDS-7006 — AI for Health Applications  
> Institution: Georgetown University | Biomedical Graduate Education  
> Author: Fadwa Elfeituri, BDS, M.S. Candidate in Heath Informatics and Data Science

---

## Background

Oral cancer is the sixth most common cancer globally. Although survival rates exceed 80% when caught early, diagnosis is often delayed due to subtle clinical presentations and limited access to specialists—especially in underserved settings. This project aims to develop an AI-driven, non-invasive screening tool to help frontline clinicians identify suspicious lesions using mobile-captured photographs.

---

## Objective

To design and evaluate a binary classification system that can distinguish between **cancerous** and **non-cancerous** lesions using:

- Raw clinical oral photographs
- Extracted metadata (e.g., image size, color mode, aspect ratio)

The project implemented two CNN-based models:
1. **Two-Branch Multimodal CNN**: Image + metadata
2. **Image-Only CNN**: Image input only

---

## Datasets

- **Oral Cancer Dataset (Kaggle)**  
  500 cancerous and 450 non-cancerous intraoral photographs  
  [🔗 Link](https://www.kaggle.com/datasets/zaidpy/oral-cancer-dataset)

- **Oral Cancer Lips and Tongue Dataset (Kaggle)**  
  87 cancerous and 44 benign images focused on subregions  
  [🔗 Link](https://www.kaggle.com/datasets/shivam17299/oral-cancer-lips-and-tongue-images)

---

## Methods

### Preprocessing

- Removed corrupted files
- Converted all images to RGB and resized to 128×128
- Extracted metadata: file size, dimensions, aspect ratio, color mode, format
- Standardized metadata using z-score normalization
- Created a manifest CSV linking image paths to labels and features

### Model Architecture

#### Two-Branch CNN
- **Image input**: Conv2D + BatchNorm + MaxPooling
- **Metadata input**: Dense layers
- **Fusion**: Concatenation → Dense → Sigmoid output

#### Image-Only CNN
- Conv2D layers → Flatten → Dense → Sigmoid

### Evaluation Metrics
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix
- Training & Validation Curves

---

## Results

| Model              | Test Accuracy | Precision (Cancer) | Recall (Cancer) | F1 (Cancer) |
|--------------------|---------------|--------------------|------------------|-------------|
| Two-Branch CNN     | 96.7%         | 0.96               | 0.99             | 0.97        |
| Image-Only CNN     | 80.6%         | 0.83               | 0.85             | 0.84        |

- The **Two-Branch CNN** significantly outperformed the image-only model, especially in minimizing false negatives.
- Visualization of predictions showed better handling of visually ambiguous cases with metadata.

---

## Repository Structure

```plaintext
oral-cancer-detection/
├── notebooks/
│   ├── KaggleModel_DataCleaning_Notebook.ipynb
│   └── KaggleModel_Development_Notebook.ipynb
├── manifests/
│   └── image_metadata_manifest.csv
├── models/
│   └── best_model.h5
├── outputs/
│   └── figures/            # e.g., confusion matrix
├── report/
│   └── Final_Project_Report.pdf
├── requirements.txt
├── .gitignore
└── README.md
```
--- 
## How to Reproduce

### Clone the Repository
```bash
git clone https://github.com/yourusername/oral-cancer-detection.git
cd oral-cancer-detection
```

### Create the Environment
```bash
conda env create -f environment.yml
conda activate oral-cancer-env
```

---

## Ongoing Development

This project represents the **first phase** of a larger multimodal diagnostic tool. Future plans include:

- Multiclass classification (Healthy, Benign, OPMD, Cancer)
- Integration of **histopathological slides**, **radiographs**, and **salivary biomarkers**
- Mobile deployment for real-time clinical decision support
- Interpretability using Grad-CAM or SHAP visualizations

> Work in progress – stay tuned for updates.

---

## Author

**Fadwa Elfeituri**  
M.S. in Health Informatics & Data Science – Georgetown University  
ffe7@georgetown.edu


