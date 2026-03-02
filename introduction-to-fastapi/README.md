# FastAPI Hello World Exercise

This directory contains a pre-built FastAPI application (`main.py`) for
the Hello World exercise.

Your task is to run the application and understand how FastAPI works in
both a local environment and the provided Workspace.

## Project Structure

    .
    ├── main.py
    └── README.md

`main.py` already contains a minimal FastAPI application with a simple
`GET /` endpoint.

## Running the Application

### Running Locally

If you are running this project locally, start the server with:

``` bash
uvicorn main:app --reload
```

Then open your browser and navigate to:

    http://127.0.0.1:8000

You should see the JSON response:

``` json
{"greeting": "Hello World!"}
```

The `--reload` flag enables automatic reload when code changes.

## Running in the Workspace Environment

Inside the provided Workspace, applications are accessed through a proxy
URL rather than `127.0.0.1`.

Start the server with:

``` bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

After starting the server:

1.  Click the **"Open Browser"** button in the bottom-right corner.
2.  The application will open at a proxy URL similar to:

```{=html}
<!-- -->
```
    https://<workspace-domain>/proxy/8000/

## Accessing the API Documentation

FastAPI automatically generates interactive API documentation.

### Local Environment

    http://127.0.0.1:8000/docs

### Workspace Environment (Important)

When running inside the Workspace, you must specify the `root_path` for
the documentation to work correctly.

Start the server with:

``` bash
uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --root-path /proxy/8000 \
  --reload
```

Then open:

    https://<workspace-domain>/proxy/8000/docs

Without setting `--root-path`, the documentation may fail to load or may
not retrieve the OpenAPI schema correctly.

## What You Should Observe

-   FastAPI automatically converts Python return values into JSON.
-   Interactive API documentation is generated without additional
    configuration.
-   Workspace environments require proxy-aware configuration
    (`--root-path`).

You are now ready to modify `main.py` and build additional endpoints.

