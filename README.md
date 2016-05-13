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
Build code and configuration files into the same Docker image. Then use environment variables to change behavior as needed. Version the code and configuration in the same code repository and use Docker image tags to strongly version all infrastructure changes.

### Deploy infrastructure like code
Infrastructure deployments can be automated just like code deployments by using the cloud providers API to create new servers. Just like with code changes, each deployment does a complete refresh of all changes so that no state is preserved on the servers between deployments. To manage application state, like data files, use cloud provider volumes and snapshots or built-in cluster replication to quickly restore data on new servers.

### Unify deployment, scaling, and failure recovery
Instead of using different strategies for configuration changes, scaling, and failure recovery treat them the same. By replacing servers during deployment the failure recovery method is also getting tested. This simplifies operations and reduces complexity.

# Contributing
If you want to contribute to the project see the [contributing guide](CONTRIBUTING.md).
