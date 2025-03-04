import click

from voorbeeld.visual1 import create_visual1
from voorbeeld.visual2 import create_visual2

@click.command()
@click.option("--week", default="1", help="Choose the visual number (1, 2 or 3)")
@click.option("--all", default=False)
def visual(week, all):
    possible_options = ['1', '2', '3']
    if week not in possible_options:
        raise ValueError('Must be 1, 2 or 3')
    
    if week == "1" or all:
        create_visual1()
    if week == '2' or all:
        create_visual2()
    
if __name__ == '__main__':
    visual()