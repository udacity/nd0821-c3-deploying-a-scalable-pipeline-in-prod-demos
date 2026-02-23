# Exercise: Exploring Heroku CLI 🚀

## Objective

In this exercise, you will:

- Create a Heroku app using the CLI
- Manually specify the official Python buildpack
- Connect the app to a local Git repository
- Deploy the repository to Heroku
- Access the Heroku runtime environment (VM) using `heroku run bash`

The goal is to become comfortable navigating Heroku entirely from the
command line.

------------------------------------------------------------------------

## Prerequisites

Before starting, ensure you have:

-  A Heroku account (logged in via CLI)

Log in if needed:

```bash
heroku login
```

------------------------------------------------------------------------

## Step 1 --- Explore the Heroku CLI

View the full list of available commands:

```bash
heroku
```

------------------------------------------------------------------------

## Step 2 --- Create a Heroku App with Python Buildpack

Create a new Heroku app with a custom name and manually specify the official Python buildpack:

```bash
heroku create name-of-the-app --buildpack heroku/python
```

Note: Manually specifying the Python buildpack is not strictly required.\

Heroku automatically detects Python if it finds:

- `requirements.txt`
- `setup.py`

We are specifying it explicitly for learning purposes.

------------------------------------------------------------------------

## Step 3 --- Verify the Buildpack

Confirm that the Python buildpack is attached:

```bash
heroku buildpacks --app name-of-the-app
```

------------------------------------------------------------------------

## Step 4 --- Initialize a Local Git Repository

Inside your project folder:

```bash
git init
git add *
git commit -m "Initial commit."
```

Even an empty repository is fine for this exercise.

------------------------------------------------------------------------

## Step 5 --- Connect the Local Repo to Heroku

Attach the Heroku remote:

```bash
heroku git:remote --app name-of-the-app
```

Verify:

```bash
git remote -v
```

------------------------------------------------------------------------

## Step 6 --- Deploy to Heroku

Push your repository to Heroku:

```bash
git push heroku main
```

If your default branch is `master`:

```bash
git push heroku master
```

------------------------------------------------------------------------

## Step 7 --- Enter the Heroku Runtime Environment

Access the Heroku VM (dyno) shell:

```bash
heroku run bash --app name-of-the-app
```

Try exploring with:

```bash
pwd
ls
ls ..
```

You will notice:

- Standard Unix directory structure
- Minimal environment
- Many tools are not installed (even `vi` is missing)

Exit the shell:

```bash
exit
```

------------------------------------------------------------------------

## Reflection Questions

- What does specifying a buildpack actually do?
- What happens if you do not specify one?
- Why is the Heroku runtime environment so minimal?
- How does Heroku connect Git deployment to application builds?

------------------------------------------------------------------------

## Cleanup (Optional)

To remove the app:

```bash
heroku apps:destroy --app name-of-the-app
```

------------------------------------------------------------------------

## What You Learned 🎯

- How to use the Heroku CLI
- How buildpacks work
- How Git integrates with Heroku
- How to access a running dyno
- What a minimal cloud runtime environment looks like

