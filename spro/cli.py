# -*- coding: utf-8 -*-
import os

import click

import spro.create
import spro.optimize


@click.group()
@click.pass_context
def cli(ctx):
    """Console script for spro"""
    SIGOPT_API_TOKEN = os.environ.get("SIGOPT_API_TOKEN", None)
    if SIGOPT_API_TOKEN is None:
        raise click.UsageError(
            "Must supply SIGOPT_API_TOKEN environment variable"
        )
    ctx.obj = SIGOPT_API_TOKEN


@cli.command()
@click.pass_obj
@click.argument('name')
def create(SIGOPT_API_TOKEN, name):
    """
    Create a new experiment; eg when you get a new bag
    """
    spro.create(SIGOPT_API_TOKEN, name)


@cli.command()
@click.pass_obj
@click.argument('experiment-id', type=int)
def optimize(SIGOPT_API_TOKEN, experiment_id):
    """
    Asks user to try various parameter settings and report back
    """
    spro.optimize(SIGOPT_API_TOKEN, experiment_id)


if __name__ == "__main__":
    cli()
