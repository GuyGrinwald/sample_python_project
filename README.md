Sample Python Project
========================

This is a sample Python project for quick bootstrapping new projects.

## TODO:
1. Create a `.env` file in the root folder with this content:
```
PYTHONPATH=.;${PYTHONPATH}
```
2. Update this README
3. Update `setup.py`
4. Do your awesome stuff

## Setup

1. If not already present, install Python 3.11 and [virtualeenvwrapper](https://pypi.org/project/virtualenvwrapper/)
2. Create a local virtualenv
```
$ mkvirtualenv {your-env-name}
```
3. Install project dependencies using
```bash
$ pip install -r requirements.txt
```

## Running Tests

We use [nox](https://nox.thea.codes/en/stable/tutorial.html#running-nox-for-the-first-time) as our testing framework. To run the tests do the following:
1. Install `nox`
```bash
$ pip install nox
```
2. Run `nox` tests
```bash
$ nox --session unit_test -f noxfile.py
```