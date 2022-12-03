import nox

@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "sample/hello_world.py")