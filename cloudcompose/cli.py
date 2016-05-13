#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from importlib import import_module
from cloudcompose.config import CloudConfig

class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        cloud_config = CloudConfig()
        plugins = cloud_config.list_plugins()
        return plugins

    def get_command(self, ctx, name):
        module_name = "cloudcompose.%s.commands.cli" % name
        imported_module = import_module(module_name)
        return imported_module.cli

cli = CLI(help='This tool\'s subcommands are loaded from the cloudcompose.<plugin>.commands.cli package '
          'where <plugin> is defined in the cloud-compose.yml file')

if __name__ == '__main__':
    cli()
