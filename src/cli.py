import click

from tale.core import execute


@click.command()
@click.argument('program', type=click.File())
def cli(program):
    code = program.read()
    execute(code)


if __name__ == '__main__':
    cli()
