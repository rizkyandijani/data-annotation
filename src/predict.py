"""Local YOLO predict (CPU). After Colab training, download best.pt here."""
from pathlib import Path

def main(weights="runs/detect/train/weights/best.pt", source="data/raw", out="data/processed/pred"):
    from ultralytics import YOLO
    m = YOLO(weights)
    m.predict(source=source, save=True, project="data/processed", name="pred", exist_ok=True)
    print(f"done. check {out}. Import these to CVAT as pre-labels, then correct.")

if __name__ == "__main__":
    main()
