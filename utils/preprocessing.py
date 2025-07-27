# utils/preprocessing.py

import os
import pandas as pd
from PIL import Image
from pathlib import Path

def extract_image_metadata(image_dir, label_map={'Cancer': 1, 'Non-Cancer': 0}):
    records = []
    image_dir = Path(image_dir)

    for label_name in label_map.keys():
        for img_path in (image_dir / label_name).glob("*"):
            try:
                with Image.open(img_path) as img:
                    width, height = img.size
                    records.append({
                        "path": str(img_path),
                        "label": label_map[label_name],
                        "width": width,
                        "height": height,
                        "mode": img.mode,
                        "format": img.format,
                        "file_size_kb": round(os.path.getsize(img_path) / 1024, 2)
                    })
            except Exception as e:
                print(f"Skipping {img_path}: {e}")

    return pd.DataFrame(records)

def engineer_features(df):
    # Aspect ratios
    df["aspect_ratio"] = df["width"] / df["height"]
    
    # Scale factor (assuming standard resized dimensions 128x128)
    df["scale_factor"] = (df["width"] * df["height"]) / (128 * 128)

    # One-hot encode image mode and format
    df = pd.get_dummies(df, columns=["mode", "format"], prefix=["mode", "format"])

    # Normalize numeric columns
    from sklearn.preprocessing import StandardScaler
    numeric_cols = ["width", "height", "file_size_kb", "aspect_ratio", "scale_factor"]
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df

def save_manifest(df, out_path="manifests/image_metadata_manifest.csv"):
    os.makedirs(Path(out_path).parent, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Manifest saved to {out_path}")
