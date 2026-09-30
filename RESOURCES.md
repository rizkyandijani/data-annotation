# Vision Annotation Resources

## Knowledge

- [CVAT Documentation — Projects, Tasks, Tracks, Export](https://opencv.github.io/cvat/docs/)
  Canonical source for CVAT concepts. Use for: anything about annotation UI, interpolation, COCO/MOT export.
- [COCO Dataset — Common Objects in Context](https://cocodataset.org/#home)
  Defines the COCO format and the 80-class dataset YOLOv8n is pre-trained on. Use for: format spec, category ideas.
- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
  Official train/val/predict API. Use for: `yolo train`, `data.yaml`, transfer learning from `yolov8n.pt`.
- [Roboflow Universe + Guides](https://universe.roboflow.com/)
  Public images/videos + practical annotation guides. Use for: sourcing PPE data, guideline examples.
- [Google Colab — GPU notebooks](https://colab.research.google.com/)
  Free T4 GPU runtime. Use for: the one training step your CPU can't do fast.

## Wisdom (Communities)

- [CVAT GitHub Discussions](https://github.com/cvat-ai/cvat/discussions)
  Practitioners troubleshooting export, SDK, tracking. Use for: real-world CVAT bugs and workflows.
- [Roboflow Forum / Universe comments](https://discuss.roboflow.com/)
  Dataset builders sharing ontologies and quality tips. Use for: guideline review, edge-case decisions.
- [r/computervision](https://www.reddit.com/r/computervision/)
  High-signal, moderated. Use for: portfolio critique, active-learning questions.

## Gaps

- Good free PPE video clips with tracking IDs are scarce — may need to cut your own 10-30s clips from public CCTV demos.
- No single good source on annotator agreement for boxes (IoU-based) — we compute it ourselves in `src/metrics.py`.
