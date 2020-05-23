"""Command line interface module for the Tale Python interpreter."""

import os
import subprocess

import click


def rebuild_grammar():
    def build(grammar: str):
        antlr4_path = '/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH'
        subprocess.call(f'java -Xmx500M -cp "{antlr4_path}" ' +
                        f'org.antlr.v4.Tool {grammar} -Dlanguage=Python3',
                        shell=True)

    grammar = 'tale/syntax/grammar/Tale.g4'
    change_time = os.stat(grammar)
    build(grammar)


@click.command()
@click.argument('program', type=click.File())
@click.option('--rebuild', is_flag=True)
def cli(program, rebuild):
    """Interprets a PROGRAM file as a Tale program."""

    if rebuild:
        rebuild_grammar()

    from tale.core import execute

    code = program.read()
    execute(code)


if __name__ == '__main__':
    cli()
