# Exercise: Tracking Data Remotely with DVC

In this exercise, you will add a DVC remote, push a tracked file to it, and pull it back.

## Objective

You will:

1. Add a DVC remote.
2. Track a CSV file with DVC.
3. Push the tracked data to the remote.
4. Pull it back from the remote.

## 1. Create a Remote

A DVC remote can be cloud storage (Amazon S3, Google Cloud Storage, Azure Blob Storage) or a folder outside your project. In the workspace, use a folder, so you don't need a cloud account:

```shell
dvc remote add -d localremote /tmp/dvcstore
```

## 2. Track and Push Files

Track the CSV file of identifiers from the previous demo and push it to the remote:

```shell
dvc add <file.csv>
git add <file.csv>.dvc .gitignore .dvc/config
git commit -m "Track data file with DVC"
dvc push
```

## 3. Pull Files Back

Delete your copy of the file and DVC's cache, then restore the file from the remote:

```shell
rm <file.csv>
rm -rf .dvc/cache
dvc pull
```

## What to Observe

- Git tracks the `.dvc` file (metadata).
- DVC pushes the actual data to the remote.
- `dvc pull` restores the file from the remote.

## Using Cloud Storage

On your own projects, the commands are the same for a cloud remote; only the URL changes, for example `s3://<bucket>/<path>` for Amazon S3. Google Drive (`gdrive://<folder-id>`) also needs the `dvc-gdrive` package and a Google Cloud project of your own, because Google blocks DVC's built-in Google Drive app. See [DVC's Google Drive guide](https://doc.dvc.org/user-guide/data-management/remote-storage/google-drive).

# Solution Reference

## Add the Remote

```shell
dvc remote add -d localremote /tmp/dvcstore
```

## Push to a Specific Remote

With more than one remote, name the one to use:

```shell
dvc push --remote localremote
```

## Or Set It as Default

```shell
dvc remote default localremote
dvc push
```

## Key Concept

- Git tracks metadata
- DVC tracks large data files
- Remote storage holds the actual dataset
