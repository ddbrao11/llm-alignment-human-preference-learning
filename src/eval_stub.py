import argparse
import json
import os
from typing import Dict, List, Tuple

Example = Tuple[str, str, str, int]  # (prompt, response_a, response_b, label)


def load_data() -> List[Example]:
    # Placeholder examples. Replace with real dataset loader later.
    return [
        ("q1", "a1", "b1", 1),
        ("q2", "a2", "b2", 0),
        ("q3", "a3", "b3", 1),
        ("q4", "a4", "b4", 0),
    ]


def evaluate(data: List[Example]) -> Dict:
    # Dummy predictor: always predicts label=1
    y_true = [x[3] for x in data]
    y_pred = [1 for _ in data]

    correct = sum(int(t == p) for t, p in zip(y_true, y_pred))
    acc = correct / max(1, len(y_true))

    metrics = {
        "accuracy": acc,
        "n": len(y_true),
        "note": "baseline scaffold (always-predict-1) to validate evaluation + logging",
    }
    return metrics


def main(out_dir: str) -> Dict:
    os.makedirs(out_dir, exist_ok=True)
    data = load_data()
    metrics = evaluate(data)

    out_path = os.path.join(out_dir, "metrics.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return metrics


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out_dir", default="runs/eval_baseline")
    args = p.parse_args()

    m = main(args.out_dir)
    print(m)