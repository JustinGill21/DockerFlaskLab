# DockerFlaskLab - 'Hello World' Flask app

This repository is a simple flask app deployed from a docker container.

Environment configurations in the `docker-compose.yml` file specify that the Flask App is run in development
mode with Debug disabled.

# Launching the app

To launch the Flask app, navigate to the directory where you downloaded the repository and run the CLI command:

```bash
docker-compose up
```

By default, visit http://localhost:5555 in a browser to access the app locally on port 5555.

# Making requests to the API

To send custom requests to the API, run the `make-request.py` file with the CLI command:

```bash
python3 make-request.py
```
