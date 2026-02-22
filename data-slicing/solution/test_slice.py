import pandas as pd
from pathlib import Path
from slice import slice_iris


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "iris.csv"


def test_slice_iris_runs_without_error():
    """
    Ensure slice_iris runs without raising exceptions.
    """
    df = pd.read_csv(DATA_PATH)

    slice_iris(df, "sepal_length")
    slice_iris(df, "sepal_width")
    slice_iris(df, "petal_length")
    slice_iris(df, "petal_width")


def test_required_columns_exist():
    """
    Verify required columns exist in dataset.
    """
    df = pd.read_csv(DATA_PATH)

    expected_columns = {
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "class",
    }

    assert expected_columns.issubset(set(df.columns))


def test_class_values_exist():
    """
    Confirm exactly three species exist.
    """
    df = pd.read_csv(DATA_PATH)

    classes = df["class"].unique()

    assert len(classes) == 3