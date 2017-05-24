import click
from sigopt import Connection


def create(SIGOPT_API_TOKEN, name):
    """
    Create a new experiment
    """
    conn = Connection(client_token=SIGOPT_API_TOKEN)

    experiment = conn.experiments().create(
        name=name,
        parameters=[
            dict(name='x', type='double', bounds=dict(min=0.0, max=1.0)),
            dict(name='y', type='double', bounds=dict(min=0.0, max=1.0)),
        ],
    )

    click.echo("Created experiment {}".format(experiment.id))
    click.echo(
        "Track experiment at "
        "https://sigopt.com/experiment/{}".format(experiment.id)
    )
