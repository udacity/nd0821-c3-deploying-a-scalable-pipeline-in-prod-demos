import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "iris.csv"

df = pd.read_csv(DATA_PATH)


def slice_iris(df, feature):
    """
    Calculate and print the mean and standard deviation of a given
    feature in the Iris dataset, grouped by class.

    Parameters
    ----------
    df : pandas.DataFrame
        The Iris dataset containing numeric feature columns and
        a 'class' column.

    feature : str
        The name of the numeric feature column to analyze.

    Returns
    -------
    None
    """

    for cls in df["class"].unique():
        df_temp = df[df["class"] == cls]

        mean = df_temp[feature].mean()
        stddev = df_temp[feature].std()

        print(f"Class: {cls}")
        print(f"{feature} mean: {mean:.4f}")
        print(f"{feature} stddev: {stddev:.4f}")

    print()


if __name__ == "__main__":
    slice_iris(df, "sepal_length")
    slice_iris(df, "sepal_width")
    slice_iris(df, "petal_length")
    slice_iris(df, "petal_width")