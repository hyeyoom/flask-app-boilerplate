# flask-app-boilerplate
Flask application boilerplate for me ._.

## run

execute flask app for dev

```bash
$ python manage.py dev
```

execute flask app for production

```bash
$ python manage.py prod
```

## features

## project structure

```GAP
flask-app-boilerplate
├── application
│   ├── __init__.py
│   ├── config.py   # application configurations
│   ├── index.py    # application instances
│   ├── models      # database models
│   │   ├── __init__.py
│   │   └── test.py # mock model
│   └── web         # main controller
│       ├── __init__.py
│       └── web_controller.py
├── front           # it's okay with react! ._.
│   ├── static
│   └── templates   
│       ├── base.html
│       ├── index.html
│       └── nav.html
├── manage.py       # flask scripts
└── requirements.txt
```