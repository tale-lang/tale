"""Command line interface module for the Tale Python interpreter."""

import click

from tale.core import execute


@click.command()
@click.argument('program', type=click.File())
def cli(program):
    """This script interprets a PROGRAM file as a Tale program."""

    code = program.read()
    execute(code)


if __name__ == '__main__':
    cli()
