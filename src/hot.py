"""Command line interface module for hot reloading."""

import sys
import subprocess
import traceback
from importlib import reload
from time import sleep

import click


def clear_console():
    subprocess.call('clear', shell=True)


def reload_modules():
    for module in sys.modules.values():
        if module.__name__.startswith('prototype'):
            reload(module)


@click.command()
@click.option('--interval', default=0.2, help='Interval between executions.')
@click.argument('program', type=click.File())
def cli(program, interval):
    """This script executes Tale CLI on a PROGRAM file with some interval."""

    # It will be reopened each hot reloading cycle.
    program.close()

    while True:
        try:
            clear_console()

            with open(program.name) as program:
                # Need to reopen file each time.
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
