# Mission: Vision Data Annotation

## Why
Software developer learning image + video annotation to build a portfolio project that proves end-to-end understanding: from guidelines to quality metrics to model-in-the-loop.

## Success looks like
- Write annotation guidelines with ontology + edge cases for a 3-class PPE domain
- Annotate 300-500 images + 2-3 videos in CVAT and export COCO + MOT
- Compute annotator agreement (IoU) and build a QA dashboard
- Fine-tune local YOLOv8-nano and demo pre-label time saved with numbers
- Publish GitHub repo with guidelines, metrics, screenshots, lessons learned

## Constraints
- ~1 month, learn as much as possible as fast as possible, granular lessons preferred
- No GPU locally (no nvidia-smi, no torch) — use Colab T4 for training, CPU locally for inference
- Everything scaffolded under `./data-annotation` only
- Prefers hands-on, software-engineering angle (Docker, APIs, scripts, formats)

## Out of scope
- Segmentation masks / 3D / audio / LLM RLHF for now — same principles, deferred
- CVAT Nuclio serverless auto-annotation — use offline pre-label script instead
