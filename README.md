# Vision Data Annotation — Learn Fast by Building

Goal: learn image + video annotation end-to-end in ~1 month, with a portfolio artifact.

## The loop (this is the whole skill)
1. Define ontology + guidelines → 2. Annotate in CVAT → 3. Measure quality → 4. Train local YOLO → 5. Pre-label next batch → 6. Fix guidelines

If you can demo that loop with numbers, you understand data annotation.

## Stack (all local except one training step)
- UI: CVAT (docker, localhost:8080) — manual + correction
- Format: COCO JSON (export from CVAT, input to analysis + training)
- Model: YOLOv8-nano `yolov8n.pt` — fine-tuned, runs on CPU
- Train: Colab T4 free GPU once, inference local after
- QA: Python + Streamlit

## Start here (order matters for speed)
1. Read `LEARNING_ROADMAP.md` (15 min) — what to learn in what order
2. Read `annotation-guidelines.md` — fill it for your domain
3. Follow `CHECKLIST.md` week by week
4. Run `notebooks/` in order: EDA → agreement → train-eval

## Domain (recommended)
Construction PPE: `person, helmet, safety-vest`. 300-500 images + 2-3 videos (10-30s).
Why: public data exists, needs both detection + tracking, meaningful.
