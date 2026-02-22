"""
Data Slicing Template

This script loads the Iris dataset and calculates
descriptive statistics for each species.

Students must implement the slice_iris function.
"""

import pandas as pd
from pathlib import Path


# Load dataset from ../data directory
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "iris.csv"


def slice_iris(df, feature):
    """
    Calculate and print the mean and standard deviation
    of a numeric feature grouped by class.

    Parameters
    ----------
    df : pandas.DataFrame
        The Iris dataset containing numeric feature columns
        and a 'class' column.

    feature : str
        The feature column to analyze.
        Expected values:
        - 'sepal_length'
        - 'sepal_width'
        - 'petal_length'
        - 'petal_width'

    TODO
    ----
    1. Loop through each unique value in the 'class' column.
    2. Filter the dataframe for each class.
    3. Compute the mean of the selected feature.
    4. Compute the standard deviation of the selected feature.
    5. Print results formatted to 4 decimal places:
       Example:

       Class: Iris-setosa
       sepal_length mean: 5.0060
       sepal_length stddev: 0.3525

    """

    # TODO: Implement this function
    raise NotImplementedError("slice_iris function not implemented yet.")


if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)

    slice_iris(df, "sepal_length")
    slice_iris(df, "sepal_width")
    slice_iris(df, "petal_length")
    slice_iris(df, "petal_width")