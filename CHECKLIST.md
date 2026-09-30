# Fast-Track Checklist (tick as you finish lessons)

- [ ] 0001 ontology: fill `annotation-guidelines.md` (20 min)
- [ ] 0002 CVAT: docker up, 10 images annotated, COCO exported to `data/processed/`
- [ ] 0003 COCO+IoU: run `src/metrics.py`, count boxes per class
- [ ] 0004 quality: double-label 20 images, mean IoU >=0.70 or revise guidelines v2
- [ ] Scale: 300-500 images + 1 video with tracks (interpolation)
- [ ] 0005 Colab T4: `yolo train model=yolov8n.pt data=data.yaml epochs=50`, save `best.pt`, record mAP50
- [ ] 0006 pre-label: `python src/predict.py`, import to CVAT, correct 100 images, measure s/img + correction %
- [ ] 0007 video: 2-3 clips, track IDs, count ID switches
- [ ] QA app: `streamlit run app/qa.py` to review tiny/low-IoU boxes
- [ ] README: metrics, screenshots, GIF, lessons learned → portfolio ready

Course map: `lessons/0001-ontology.html` → `0002-first-10-boxes-cvat.html` → `0003-coco-iou.html` → (0004-0007 generated next on demand).
