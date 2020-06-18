"""Command line interface module for the Tale Python interpreter."""

import os
import subprocess

from mints import Arg, Flag, cli


class File:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> str:
        with open(self.path, 'r') as f:
            return f.read()


def rebuild_grammar():
    def build(grammar: str):
        antlr4_path = '/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH'
        subprocess.call(f'java -Xmx500M -cp "{antlr4_path}" ' +
                        f'org.antlr.v4.Tool {grammar} -Dlanguage=Python3',
                        shell=True)

    grammar = 'tale/syntax/grammar/Tale.g4'
    change_time = os.stat(grammar)
    build(grammar)


@cli
def interpret(program: Arg[File], rebuild: Flag):
    """Interprets a program file as a Tale program."""

    if rebuild:
        rebuild_grammar()

    from tale.core import execute

    code = program.read()
    execute(code)


cli.add_parser(File)


if __name__ == '__main__':
    cli()
