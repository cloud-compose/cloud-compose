#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from importlib import import_module

#TODO read the list of plugins from the docker-compose.yml
plugins = ['cluster']

class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        return plugins

    def get_command(self, ctx, name):
        module_name = "cloudcompose.%s.commands.cli" % name
        print "Importing %s" % module_name
        imported_module = import_module(module_name)
        return imported_module.cli

cli = CLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')

if __name__ == '__main__':
    cli()
