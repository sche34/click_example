import click

from voorbeeld.visual1 import Visual1
from voorbeeld.visual2 import Visual2


@click.command()
@click.option("--week", default="1", help="Choose the visual number (1 or 2)")
@click.option("--all", default=False, flag_value=True)
def visual(week, all):
    possible_options = ["1", "2"]
    if week not in possible_options:
        raise ValueError("Must be 1 or 2")

    # Read the configuration from the 'config.ini' file
    if week == "1" or all:
        V1 = Visual1("visual1")
        V1.create_visual()
    if week == "2" or all:
        V2 = Visual2("visual2")
        V2.create_visual()


if __name__ == "__main__":
    visual()
