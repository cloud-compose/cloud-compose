# Cloud Compose
Cloud Compose is a family of tools that support immutable infrastructure on cloud environments. This project contains the code needed to connect various plugins to support common cloud management operations. See the [Cloud Compose cluster plugin](https://github.com/cloud-compose/cloud-compose-cluster) for a concrete example of how the plugin system works.

To install Cloud Compose, use pip to install the cloud-compose package and any additional plugins.

```
pip install cloud-compose cloud-compose-cluster
pip freeze > requirements.txt
```

Once a plugin is configured, you can see what commands are available by running the plugin command with no options
```
cloud-compose cluster 
```

## Immutable Infrastructure
Immutable infrastructure is built around the following three principles:

* consolidate code and configuration
* deploy infrastructure like code
* unify scaling, deployment, and failure recovery 

### Consolidate code and configuration
BUilde code and configuration files into the same Docker image. Use environment variables to change behavior as needed. Version the code and configuration in the same code repository and use Docker image tags to strongly version all infrastructure changes.

### Deploy infrastructure like code
Infrastructure deployments can be automated just like code deployments by using the cloud providers API to create new servers. Just like with code changes, each deployment does a complete refresh of all configuration files so that no state is preserved on the servers between deployments. To manage application state like database data files, use cloud provider volumes and snapshots or cluster replication to quickly restore state on new servers.

### Unify deployment, scaling, and failure recovery
Instead of having different methods for responding to configuration changes, scaling, and failure recovery treat them all as the same type of event and use the same process. By replacing servers during deployment the failure recovery method is also getting tested at the same time. This simplifies operations and reduces complexity.

## Contributing 
To work on the code locally, checkout both cloud-compose and cloud-compose-cluster to the same parent directory. Then use a virtualenv and pip install editable to start working on them locally.
```
mkvirtualenv cloud-compose
pip install --editable cloud-compose
pip install --editable cloud-compose-cluster
```

