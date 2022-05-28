import click
from {{ cookiecutter.project_slug }} import __version__


def print_version(ctx, _, value):  # pragma: no cover
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()


@click.command()
@click.option('--version', help='Show version information.', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():
    """{{ cookiecutter.project_description }}"""

if __name__ == '__main__':
    cli()
