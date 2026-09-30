# Learning Roadmap — Maximum Concepts, Minimum Time

Learn in this order. Each step has a DO task — don't just read.

## 1. Ontology & Guidelines (2h) → teaches: ambiguity is the job
DO: fill `annotation-guidelines.md` for 3 classes.
Learn: class definition, edge cases (occlusion, truncation, tiny boxes), box tightness rule.
Key insight: 80% of quality problems are guideline problems, not annotator problems.

## 2. COCO Format (1h) → teaches: the lingua franca
DO: open any `*.json` export, find `images`, `annotations`, `categories`. Write a script to count boxes per class.
Learn: `bbox=[x,y,w,h]`, `area`, `iscrowd`, `image_id` linkage.
File: `src/coco_utils.py`

## 3. CVAT UI (3h) → teaches: tooling
DO: `docker compose up` in `cvat/`, create project, annotate 20 images + 1 video with interpolation.
Learn: projects vs tasks vs jobs, interpolation for video tracks, attributes (occluded/truncated), review mode.
Shortcut cheat: `N` next, `Ctrl+S` save, `R` redraw.

## 4. Quality Metrics (3h) → teaches: how to trust data
DO: annotate same 20 images twice, run `src/metrics.py` to get IoU agreement.
Learn:
- Box IoU = intersection / union. >0.5 = match, >0.75 = good.
- mAP50 = model metric, IoU-agreement = human metric. Don't confuse them.
- Cohen's Kappa for class labels.
File: `notebooks/02_agreement.ipynb`

## 5. Local Model: YOLOv8-nano (4h) → teaches: model-in-the-loop
DO: train on Colab T4, download `best.pt`, run `src/predict.py` locally on CPU.
Learn: transfer learning from `yolov8n.pt` (COCO pre-trained), `data.yaml`, train/val split, overfitting on small data.
Why nano: 6M params, CPU inference ~50ms, perfect for learning loop.

## 6. Active Learning Loop (4h) → teaches: the money skill
DO: predict on 100 new images → import to CVAT → correct only → measure time saved + correction rate.
Learn: pre-label precision vs time saved tradeoff, when to retrain, sampling (uncertainty vs random).
Portfolio number: "Manual 90s/img → assisted 35s/img, 28% boxes corrected."

## 7. Video Tracking (2h) → teaches: temporal consistency
DO: annotate 2 videos with track IDs, export MOT format, check ID switches.
Learn: detection (per-frame boxes) vs tracking (same ID across frames), interpolation, ID switch metric.

Skip for now: segmentation masks, 3D, audio, LLM RLHF — same principles, different tools.
