Sample Python Project
========================

This is a sample Python project for quick bootstrapping new projects.

## TODO:
1. Create a `.env` file in the root folder with this content:
```
PYTHONPATH=.;${PYTHONPATH}
```
2. Follow [this guide](https://stackoverflow.com/a/47184788/4890123) to fix your virtualenv to include your project in the PYTHONPATH
3. Update this README
4. Update `setup.py`
5. Do your awesome stuff
    * Rename `sample/` and update its content
    * Do you need a web service - update `web/`
    * Do you need a Docker - update `Dockerfile`
    * Do you need `K8s` - update `k8s/`
6. Update `k8s/deployment.yaml` with your correct project name (i.e. replace `sample-python-project` prefix)

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

## Running Localy
1. Configure your environment's interpreter into your IDE
2. Make sure your `PATH` and `PYTHONPATH` env variables are configured properly
3. Open `web/app.py` and run the file via the IDE

## Running in Docker
1. Make sure you have `Docker` installed
2. `cd` to project root folder and build the image
```bash
$ docker build . -t sample-python-project
```
3. Run the image with exposed ports (make sure you're binded to the correct localhost - could also be `0.0.0.0`)
```bash
$ docker run -d -p 127.0.0.1:5000:5000 sample-python-project
```

## Running in K8s
1. Make sure Docker is installed
2. Make sure you have K8s installed either via Docker-Desktop or other service such as minikube
3. Install kubectl
4. Create the K8s deployment
```bash
$ kubectl create -f k8s\deployment.yaml
```
5. Run the K8s deployment
```bash
$ kubectl run sample-python-project-deployment --image sample-python-project --namespace sample-python-project-namespace
```
6. To kill the container and clean up resources run
```bash
kubectl delete namespace sample-python-project-namespace
```