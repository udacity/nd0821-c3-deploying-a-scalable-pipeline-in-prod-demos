# Exercise: Tracking Data Remotely with Google Drive as a DVC Remote

In this exercise, you will track data remotely using **Google Drive** as a DVC remote storage backend.

## Objective

You will:

1. Create a Google Drive folder to use as a DVC remote.
2. Configure the remote in DVC.
3. Track a CSV file using DVC.
4. Push the tracked data to Google Drive.
5. (Optional) Set the Google Drive remote as default.

## 1. Create a Google Drive Remote

1. Create a new folder in Google Drive.
2. Copy the folder URL.

Example:

    https://drive.google.com/drive/u/0/folders/0AIac4JZqHhKmUk9PDA

The unique identifier is:

    0AIac4JZqHhKmUk9PDA

You will use this identifier in the DVC command.

## 2. Add Google Drive as a DVC Remote

Run:

```shell
dvc remote add -d gdrive_remote gdrive://<FOLDER_ID>
```

Example:

```shell
dvc remote add -d gdrive_remote gdrive://0AIac4JZqHhKmUk9PDA
```

This sets the Google Drive folder as your default DVC remote.

## Important Note on Authentication

Due to recent Google security restrictions, you may encounter:

- "App blocked" errors
- Authentication failures
- Third-party app restrictions

This happens because Google restricts unverified applications.

### Possible Workarounds

- Use a personal or test Google account.
- Use Google Cloud Storage (recommended for production).
- Use other DVC-supported remotes (AWS S3, Azure Blob Storage, etc.).

## 3. Track Files in DVC

If authentication succeeds, track your CSV file:

```shell
dvc add <file.csv>
git add <file.csv>.dvc .gitignore
git commit -m "Track data file with DVC"
dvc push
```

On first push, you will be prompted to authenticate via browser.

Complete the authentication process and paste the provided code into the terminal if required.

## What to Observe

- Git tracks the `.dvc` file (metadata).
- DVC pushes actual data to Google Drive.
- Remote storage now contains your versioned dataset.

# Solution Reference

## Add Remote

```shell
dvc remote add driveremote gdrive://UNIQUE_IDENTIFIER
```

## Push to Specific Remote

```shell
dvc push --remote driveremote
```

## Or Set as Default

```shell
dvc remote default driveremote
dvc push
```

## Key Concept

- Git tracks metadata
- DVC tracks large data files
- Remote storage holds the actual dataset
- Google Drive acts as a versioned data backend

## Summary

This exercise demonstrates the conceptual workflow of using Google Drive as a DVC remote.

For production environments, consider using:

-   Google Cloud Storage
-   AWS S3
-   Azure Blob Storage

