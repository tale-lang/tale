"""Command line interface module for hot reloading."""

import os
import sys
import subprocess
import traceback
from importlib import reload
from time import sleep

import click


def build_grammar_if_changed():
    def build(grammar: str):
        antlr4_path = '/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH'
        subprocess.call(f'java -Xmx500M -cp "{antlr4_path}" ' +
                        f'org.antlr.v4.Tool {grammar} -Dlanguage=Python3',
                        shell=True)

    this = build_grammar_if_changed
    grammar = 'tale/syntax/grammar/Tale.g4'
    change_time = os.stat(grammar)

    if hasattr(this, 'change_time') and this.change_time != change_time:
        print('[System] Rebuilding grammar')
        build(grammar)

    this.change_time = change_time


def clear_console():
    subprocess.call('clear', shell=True)


def reload_modules():
    modules = list(sys.modules.values())
    for module in modules:
        if module.__name__.startswith('tale'):
            reload(module)


@click.command()
@click.option('--interval', default=0.2, help='Interval between executions.')
@click.argument('program', type=click.File())
def cli(program, interval):
    """This script executes Tale CLI on a PROGRAM file with some interval."""

    # `program` file will be reopened each hot reloading cycle.
    program.close()

    while True:
        try:
            build_grammar_if_changed()
            clear_console()

            with open(program.name) as program:
                code = program.read()

                import tale.core

                reload_modules()
                reload(tale.core)

                tale.core.execute(code)

        except Exception:
            traceback.print_exc()

        sleep(interval)


if __name__ == '__main__':
    cli()
