RunSpots
========

Booking.com Hackathon


## Requirements

- Django 1.8+ (to pull the template)
- Docker
- Docker Compose


## Quickstart common

## Quickstart for non-docker

Copy the `keys.json.sample` file and change the values accordingly:

```
cp app/settings/keys.json.sample app/settings/keys.json
```

Create a python3 venv

```
python3 -m venv runspot
```

Install the requirements

```
sudo source requirements/build.sh
pip install -r requirements/base.txt
pip install -r requirements/dev.txt
```

Create your own copy of `app/settings/dev.py` and change the settings variables
accordingly.

```
cp app/settings/dev.py app/settings/dev_<name>.py
```

Runserver with your settings

```
python3 manage.py runserver_plus --settings=app.settings.dev_<name>
```

All app go under the `app` package.

``
app
 |
 - subapp1
 - subapp2
```

So in the installed apps they should be included as:

```
LOCAL_APPS = [
    'app.subapp1',
    'app.subapp2',
]
```



## Quickstart for Docker

Copy or rename the `vars.env.sample` file:

```
cp vars.env.sample vars.env
```

Copy the `keys.json.sample` file and change the values accordingly:

```
cp app/settings/keys.json.sample app/settings/keys.json
```

Add runspots.dev to you /etc/hosts file:

```
echo "0.0.0.0       runspots.dev" | sudo tee -a /etc/hosts
```

Generate dev ssl keys:

```
source scripts/generate_ssl.sh var/ssl runspots.dev
```

Run compose:

```
docker-compose -f compose/dev.yml run --service-ports nginx
```

Then you should be able to ssh to the web container:

```
ssh happy@0.0.0.0 -p 2767
```

Open your browser to:

```
https://runspots.dev:8017
```

