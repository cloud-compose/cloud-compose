# cloud-compose
Cloud Compose simplifies the process of running Docker images on cloud instances. To use Cloud Compose you need three files:

1. A docker-compose.yml that describes which images you want to run
1. A cloud_init template for provisioning an EC2 server
1. A cloud-compose.yml to configure the cloud-compose system. 

Cloud Compose uses a simple plugin system to add additional tools. The most commonly used plugin is the cluster plugin. This plugin will provision a new server cluster on your favorite cloud provider. 

To install Cloud Compose, use pip to install the cloud-compose package and any additional plugins.

```
pip install cloud-compose cloud-compose-cluster
pip freeze > requirements.txt
```

To see what commands are available for a particular plugin run the help option
```
cloud-compose cluster help
```

To create a new cluster, you would simply issue the up command for the cluster plugin:
```
cloud-compose cluster up
```

You can also install a chatbot that will run these same commands from Slack. An example chatbot command to provision a mongodb cluster might look like this
```
@cloud-compose alias github.com/cloud-compose/mongodb mongodb
@cloud-compose mongodb cluster up
```

## Contributing 
To work on the code locally, checkout both cloud-compose and cloud-compose-cluster to the same parent directory. Then use a virtualenv and pip install editable to start working on them locally.
```
mkvirtualenv cloud-compose
pip install --editable cloud-compose
pip install --editable cloud-compose-cluster
```

