# Preparing Django app

1. `python3 manage.py migrate`
2. `python3 manage.py collectstatic`
3. `python3 manage.py createsuperuser`

# Running with HyperDX

- Create a virtual environment and activate it

```
python3 -m venv .venv
source .venv/bin/activate
```

- Install requirements

```
pip install -r requirements.txt
```

- Install instrumentation packages

```
opentelemetry-bootstrap --action=install
```

## To run with gunicorn you need to add post_fork hook

1. Add a file `gunicorn.config.py` as given in this repo
2. Specify that config file when running gunicorn as in below run command

```
DJANGO_SETTINGS_MODULE=mysite.settings OTEL_SERVICE_NAME=mysite HYPERDX_API_KEY=<YOUR_KEY> opentelemetry-instrument gunicorn mysite.wsgi -c gunicorn.config.py --workers 2 --threads 2
```
*specifying **DJANGO_SETTINGS_MODULE** is necessary for opentelemetry instrumentation to work*

# Browsing the app and checking at HyperDX

1. Visit `http://localhost:8000/admin` and create a question for poll
2. Then visit the list of polls at `http://localhost:8000/polls/` and explore the polls
3. The data should be visible now in HyperDX at `https://hyperdx.io/search`

