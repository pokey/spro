import click
from sigopt import Connection


def evaluate_model(assignments):
    """
    Asks the user to brew a shot and report how it was
    """
    click.echo("Brew a shot with the following parameters:")
    click.echo(assignments)
    quality = click.prompt('How was it [0.0-10.0]?', type=float)
    return quality


def optimize(SIGOPT_API_TOKEN, experiment_id):
    """
    The main optimization loop.
    """
    click.echo("Running optimization loop.  Ctrl-C to exit")

    conn = Connection(client_token=SIGOPT_API_TOKEN)

    # Run the Optimization Loop between 10x - 20x the number of parameters
    while True:
        # See if there are any pending suggestions from a previous run and use
        # them if so
        suggestions = conn.experiments(experiment_id).suggestions().fetch(
            state="open"
        )
        if suggestions.count > 0:
            suggestion = suggestions.data[0]
        else:
            # Otherwise request a new suggestion
            suggestion = conn.experiments(experiment_id).suggestions().create()

        value = evaluate_model(suggestion.assignments)

        conn.experiments(experiment_id).observations().create(
            suggestion=suggestion.id,
            value=value,
        )
