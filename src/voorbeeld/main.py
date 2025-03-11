import click
from enum import Enum

from voorbeeld.visual1 import Visual1
from voorbeeld.visual2 import Visual2

class WeekOption(Enum):
    ONE = "1"
    TWO = "2"

@click.command()
@click.option("--week", default="1", help="Choose the visual number (1 or 2)")
@click.option("--all", default=False, flag_value=True)
def visual(week, all):
    possible_options = [option.value for option in WeekOption]
    if week not in possible_options:
        raise ValueError("Must be 1 or 2")

    # Read the configuration from the 'config.ini' file
    if week == WeekOption.ONE.value or all:
        V1 = Visual1("visual1")
        V1.create_visual()
    if week == WeekOption.TWO.value or all:
        V2 = Visual2("visual2")
        V2.create_visual()


if __name__ == "__main__":
    visual()
