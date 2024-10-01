import click

@click.command()
@click.option("--week", default="1", help="Choose the visual number (1, 2 or 3)")
@click.option("--all", default=False)
def visual(week, all):
    possible_options = ['1', '2', '3']
    if week not in possible_options:
        raise ValueError('Must be 1, 2 or 3')
    
    if week == "1" or all:
        print('Now it runs the class of visual one')
    if week == '2' or all:
        print('Now it runs the class of visual two')
    if week == '3' or all:
        print('Now it runs the class of visual three')
    
if __name__ == '__main__':
    visual()