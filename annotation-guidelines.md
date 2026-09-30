# Annotation Guidelines — PPE Safety v1 (FILL THIS IN LESSON 0001)

## Ontology
- `person` — any visible human torso+head, height >=30px
- `helmet` — hard hat WORN on head only (not in hand, not on ground)
- `safety-vest` — high-vis vest worn, >50% visible

Attributes: `occluded=[yes/no]`, `truncated=[yes/no]`

## Box rules
- Tight: touch outermost visible pixels, 0 margin. Loose boxes drop IoU ~0.15.
- Occluded: still label if >50% visible, set occluded=yes.
- Truncated (edge of image): label, set truncated=yes.
- Tiny (<30px person height): SKIP.
- Reflections, posters, screens: NEVER label.

## Edge cases (add screenshot links as you go)
1. Helmet in hand → skip helmet, label person. ex: [link]
2. Vest under jacket → skip vest if <50% visible. ex: [link]
3. Back view, helmet visible → label both. ex: [link]
4. Two overlapping workers → two person boxes, may overlap. ex: [link]
5. Blur / night → label if confident, else skip + flag for review.

## Quality bar
- Mean pairwise IoU >=0.70 on 10% double-labeled sample, else revise this doc (v2).
- Every image: Ctrl+S, no unlabeled instances of the 3 classes.

Changelog: v1 2026-09-25 initial — fill decisions from lesson 0001.
