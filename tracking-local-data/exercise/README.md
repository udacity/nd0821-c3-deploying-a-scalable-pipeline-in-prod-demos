# Exercise: Tracking Local Data with DVC

In this exercise, you will track data using DVC with a local remote
storage.

## Objective

You will:

1.  Initialize Git and DVC.
2.  Configure a local remote directory outside the current working
    directory.
3.  Generate a CSV file using the provided script.
4.  Track the CSV file with DVC.
5.  Push the tracked data to the local remote.
6.  Modify the CSV file and track the updated version.

------------------------------------------------------------------------

## Step 1 --- Initialize the Repository

From inside the `exercise` directory:

``` bash
git init
dvc init
```

------------------------------------------------------------------------

## Step 2 --- Configure Local Remote

Create a folder outside the current directory and set it as the default
remote:

``` bash
mkdir ../local_remote
dvc remote add -d localremote ../local_remote
```

Verify:

``` bash
dvc remote list
```

------------------------------------------------------------------------

## Step 3 --- Generate the CSV

Run:

``` bash
python exercise_func.py 10
```

This creates `id.csv`.

------------------------------------------------------------------------

## Step 4 --- Track with DVC

``` bash
dvc add id.csv
git add .gitignore id.csv.dvc
git commit -m "Track initial id.csv"
dvc push
```

------------------------------------------------------------------------

## Step 5 --- Update the Data

Double the identifiers:

``` bash
python exercise_func.py 20
```

Then:

``` bash
dvc add id.csv
git add id.csv.dvc
git commit -m "Update id.csv to 20 identifiers"
dvc push
```

------------------------------------------------------------------------

## What to Observe

-   The `.dvc` file changes after updating the CSV.
-   Git tracks metadata.
-   DVC stores the actual data in the local remote.
