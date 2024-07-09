import click
from scripts.Maze import Maze

@click.command()
@click.option('-w', '--width', default=100, help='Width of the mazes')
@click.option('-h', '--height', default=100, help='Height of the mazes')
@click.option('--count', default=1, help='Number of files to generate')
def main(width, height, count):
    maze = Maze()
    for _ in range(count):
        maze.generate(width, height)

if __name__ == "__main__":
    main()
