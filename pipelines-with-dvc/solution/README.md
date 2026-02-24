# Solution: Pipelines with DVC

This directory contains the complete solution for the Pipelines with DVC exercise.

The solution demonstrates:

- Two DVC stages (prepare, train)
- Explicit dependencies and outputs
- Parameterized training via params.yaml
- Reproducible ML pipeline execution

------------------------------------------------------------------------

## Project Structure

. ├── fake_data.csv ├── prepare.py ├── train.py ├── params.yaml ├──
dvc.yaml ├── dvc.lock ├── X.csv ├── y.csv └── model.pkl

------------------------------------------------------------------------

## Parameter Configuration

The logistic regression hyperparameter C is no longer hard-coded.

It is read from params.yaml:
```yaml
C: 1.0
```
Inside train.py, the parameter is loaded via:
```python
with open("./params.yaml", "rb") as f:
    params = yaml.load(f, Loader=Loader)

lr = LogisticRegression(C=params["C"])
```
This allows DVC to track hyperparameter changes and re-run only the
affected stage.

------------------------------------------------------------------------

## Stage 1 --- Prepare

Purpose: - Reads fake_data.csv - Outputs: - X.csv - y.csv

Stage Command:
```shell
dvc exp run -n prepare -d fake_data.csv -d prepare.py -o X.csv -o y.csv python ./prepare.py
```
------------------------------------------------------------------------

## Stage 2 --- Train

Purpose: - Reads: - X.csv - y.csv - params.yaml - Trains Logistic Regression - Outputs: - model.pkl

Stage Command:
```shell
dvc exp run -n train -d X.csv -d y.csv -d train.py -p C python ./train.py
```

------------------------------------------------------------------------

## Running the Full Pipeline
```shell
dvc repro
```
DVC will:

1. Execute prepare
2. Execute train
3. Update dvc.lock
4. Track parameter values

------------------------------------------------------------------------

## What This Demonstrates

- Modify fake_data.csv → prepare + train re-run
- Modify prepare.py → prepare + train re-run
- Modify train.py → train only re-runs
- Modify C in params.yaml → train only re-runs

------------------------------------------------------------------------

## Key Concepts Demonstrated

- Multi-stage DVC pipelines
- Explicit dependency tracking
- Parameter tracking with -p
- Experiment tracking via dvc exp run
- Reproducible ML workflow

------------------------------------------------------------------------

## Final Result

You now have a fully reproducible, parameterized ML pipeline managed by
DVC.

This structure mirrors production-grade ML pipelines where:

- Data preprocessing
- Model training
- Hyperparameter control
- Artifact versioning

are cleanly separated and tracked.

