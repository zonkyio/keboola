from keboola import docker

cfg = docker.Config('/data/')
params = cfg.get_parameters()

print(params['object'])
