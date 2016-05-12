from cloudcompose.cluster.template import Template
from cloudcompose.cluster.dockercompose import DockerCompose
from os.path import join, split
from pprint import pprint

class CloudInit():
    def __init__(self, plugin_name, base_dir='.'):
        self.base_dir = base_dir
        self.template_file = '%s.sh' % plugin_name

    def search_path(self, config_data):
        raw_search_path = config_data['search_path']
        raw_search_path.insert(0, '.')
        return [join(self.base_dir, path) for path in raw_search_path]

    def build(self, config_data, **kwargs):
        for key, value in kwargs.iteritems():
            config_data['_' + key] = value
        self.build_pre_hook(config_data, **kwargs)
        return self._render_template(config_data)

    def build_pre_hook(self, config_data, **kwargs):
        pass

    def _render_template(self, config_data):
        template = Template(self.search_path(config_data))
        return template.render(self.template_file, config_data)
