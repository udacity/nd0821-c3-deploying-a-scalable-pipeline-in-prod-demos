# Exercise: Pipelines with DVC

In this exercise, you will create a simple two-stage ML pipeline using
DVC.

You are given:

- fake_data.csv
- prepare.py
- train.py

Your goal is to:

1. Create two DVC stages (prepare, train)
2. Specify dependencies and outputs correctly
3. Refactor the logistic regression hyperparameter to be read from **params.yaml**
4. Include the parameter in the DVC stage configuration

------------------------------------------------------------------------

## Objective

You will:

- Build a reproducible ML pipeline
- Track data and intermediate artifacts
- Connect hyperparameters via params.yaml
- Understand how DVC tracks params, dependencies, and outputs

------------------------------------------------------------------------

## Project Structure

Expected structure after completing the exercise:

. ├── fake_data.csv ├── prepare.py ├── train.py ├── params.yaml ├──
dvc.yaml ├── dvc.lock

------------------------------------------------------------------------

## Step 1 --- Initialize DVC

If not already initialized:

```shell
git init
dvc init
```

------------------------------------------------------------------------

## Step 2 --- Create the Prepare Stage

The prepare.py script should:

- Take fake_data.csv
- Output processed data (e.g., X.csv and y.csv)

Create the stage:

```shell
dvc stage add -n prepare \
    -d prepare.py \
    -d fake_data.csv \
    -o X.csv \
    -o y.csv \
    python prepare.py
```

------------------------------------------------------------------------

## Step 3 --- Refactor train.py to Use params.yaml

Currently, the logistic regression hyperparameter (C value) is
hard-coded.

Modify train.py so it:

- Reads `C` from params.yaml
- Uses that value in `LogisticRegression`

Example params.yaml:

```yaml
train:
    C: 1.0
```

Inside train.py:

```python
import yaml

with open("params.yaml") as f:
    params = yaml.safe_load(f)

C = params["train"]["C"]
```

Use it:

```python
LogisticRegression(C=C)
```

------------------------------------------------------------------------

## Step 4 --- Create the Train Stage

The train.py script should:

-  Take X.csv and y.csv
-  Read hyperparameter from params.yaml
-  Output a trained model (e.g., model.pkl)

Create the stage:

```shell
dvc stage add -n train \
    -d train.py \
    -d X.csv \
    -d y.csv \
    -p train.C \
    -o model.pkl \
    python train.py
```

------------------------------------------------------------------------

## Step 5 --- Run the Pipeline
```shell
dvc repro
```

You should see:

1. prepare stage runs
2. train stage runs
3. Outputs created
4. dvc.lock updated

------------------------------------------------------------------------

## Key Concepts

- -d : Dependency (code or data)
- -o : Output artifact
- -p : Parameter tracked from params.yaml
- dvc.yaml : Pipeline definition
- dvc.lock : Frozen reproducible state

------------------------------------------------------------------------

## Try This

Change the hyperparameter:

```yaml
train:
    C: 0.5
```

Then run:
```shell
dvc repro
```

Only the train stage should re-run.

------------------------------------------------------------------------

## What You Should Observe

- Changing fake_data.csv → both stages re-run
- Changing prepare.py → both stages re-run
- Changing train.py → only train re-runs
- Changing train.C in params.yaml → only train re-runs

------------------------------------------------------------------------

## Summary

You have now built:

- A two-stage ML pipeline
- Parameterized training
- A reproducible workflow
- A dependency-aware pipeline using DVC

This is the foundation of production-grade ML pipelines.

