# -*- coding: utf-8 -*-

import click

from spro import optimize


@click.command()
def main(args=None):
    """Console script for spro"""
    optimize()


if __name__ == "__main__":
    main()
