"""IoU + annotator agreement. Lesson 0003-0004 starter."""
def box_iou(a, b):
    """a,b = [x,y,w,h] in pixels. Returns 0..1."""
    x1 = max(a[0], b[0]); y1 = max(a[1], b[1])
    x2 = min(a[0]+a[2], b[0]+b[2]); y2 = min(a[1]+a[3], b[1]+b[3])
    inter = max(0, x2-x1) * max(0, y2-y1)
    ua = a[2]*a[3]; ub = b[2]*b[3]
    union = ua + ub - inter
    return inter/union if union else 0.0

def mean_matching_iou(boxes_a, boxes_b, thresh=0.5):
    """Greedy match: for each box in A, best IoU in B. Returns (mean_iou, match_rate)."""
    if not boxes_a or not boxes_b:
        return 0.0, 0.0
    ious = []
    matched = 0
    used = set()
    for a in boxes_a:
        best, bi = 0, -1
        for i, b in enumerate(boxes_b):
            if i in used: continue
            v = box_iou(a, b)
            if v > best: best, bi = v, i
        ious.append(best)
        if best >= thresh:
            matched += 1; used.add(bi)
    return sum(ious)/len(ious), matched/max(len(boxes_a), len(boxes_b))

if __name__ == "__main__":
    print(box_iou([0,0,10,10],[5,5,10,10]))  # ~0.14
    print(mean_matching_iou([[0,0,10,10]], [[1,1,10,10]]))  # high
