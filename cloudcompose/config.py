from os.path import join, isfile
import yaml
from cloudcompose.exceptions import CloudComposeException

class CloudConfig:
    def __init__(self, sub_dir='.'):
        self.config_dirs = ['cloud-compose']
        self.config_dirs.append(sub_dir)
        self.config_files = ['cloud-compose.yml', 'cloud-compose.yaml']

    def config_data(self, plugin_name):
        config_dir, config_file = self.find_config()
        config_data = None
        with open(join(config_dir, config_file), 'r') as yaml_file:
            config_data = yaml.load(yaml_file)
        return config_data[plugin_name]

    def find_config(self):
        # start at the working directory and look first in the current folder
        for config_dir in self.config_dirs:
            for config_file in self.config_files:
                if isfile(join(config_dir, config_file)):
                    return config_dir, config_file
        raise CloudComposeException("Unable to find cloud-compose.yml in the current directory or directory called cloud-compose.")

