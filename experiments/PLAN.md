# Experiment Plan (LLM Preference Alignment)

## Objective
Build a reproducible baseline for predicting human preference signals from paired conversational responses.

## Baseline (Week 1)
- Simple classifier scaffold with consistent metrics logging
- Error slicing plan (length, topic buckets if available, confidence calibration)

## Evaluation
- Accuracy / F1
- Calibration check (basic confidence vs correctness)
- Qualitative error review: where labels look ambiguous

## Reporting
- Local `runs/<name>/metrics.json` (not committed)
- Commit `experiments/results.md` + `experiments/error_analysis.md`