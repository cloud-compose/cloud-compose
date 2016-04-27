import jinja2
from pprint import pprint
from os.path import join

class Template:
    def render(self, plugin_name, cloud_config):
        config_dir, config_data = cloud_config.config_data(plugin_name)
        pprint(config_data)
        template_file = join(config_dir, config_data['template'])
        template_obj = jinja2.Template(open(template_file).read())
        return template_obj.render(config_data)

