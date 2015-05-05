# IVR with Django demo

## Local setup

```sh
$ conda create -n twilio-test python=3.4.1 
$ source activate twilio-test
$ pip install -r requirements.txt
```
(Note, I use conda to manage python, could just use a virtualenv)

Get your environment variables ready
```sh
$ cp example.env .env
```
Edit .env with all the correct variables, then run.

```sh
$ source .env
$ python manage.py migrate
$ foreman start
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

Install the [Heroku Toolbelt](https://toolbelt.heroku.com/).


```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```

Don't forget to set the heroku environment variables, either through
```sh
$ heroku config:set XXX=
```
or through the heroku dashboard (under settings)
