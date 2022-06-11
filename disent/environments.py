from . import settings

ENVS = {
  "local": "http://localhost:8000",
  "dev":   "https://api-dev.disent.com",
  "prod":  "https://snpricer-dev.disent.com",
}

def set_env(env):
	keys = ENVS.keys()
	if env in keys:
		settings.ENV = env
	else:
		raise Exception('Error',f'Environment must be one of {keys}')

def get_uri_left():
	return ENVS[settings.ENV]
