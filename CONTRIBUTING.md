## Development
To work on the code locally, checkout both cloud-compose and cloud-compose-cluster to the same parent directory. Then use a virtualenv and pip install editable to start working on them locally.
```
mkvirtualenv cloud-compose
pip install --editable cloud-compose
pip install --editable cloud-compose-cluster
```

Run the tests using this command:
```
python setup.py test
```

## Release
To release the changes create an account on [PyPi](https://pypi.python.org/pypi) and then get someone to add you to the project so you can push updates.

Update the version information in setup.py. Then create a release that corresponds to the version on Github and document the high level features in the release.

Then use deploy the change to PyPi with this command:
```
python setup.py sdist upload -r pypi
```
