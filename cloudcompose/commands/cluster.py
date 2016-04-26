import click

@click.group()
def cli():
    pass

@cli.command()
def up():
    """
    creates a new cluster
    """
    print "in cluster up command"

@cli.command()
def down():
    """
    destroys an existing cluster
    """
    print "in cluster down command"
