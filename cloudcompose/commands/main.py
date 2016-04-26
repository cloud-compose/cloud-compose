#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.version_option()
@click.argument('plugin')
@click.argument('action')
def main(plugin, action):
    print "Running %s %s" % (plugin, action)

if __name__ == '__main__':
    main()
