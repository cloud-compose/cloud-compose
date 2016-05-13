from cloudcompose.exceptions import CloudComposeException
from os import environ

def require_env_var(key):
    if key not in environ:
        raise CloudComposeException('Missing %s environment variable' % key)
    return environ[key]

