import click
from mylib.bot import scrape
# This script uses the Wikipedia API to scrape summaries of given topics.
# It uses the Click library to create a command-line interface for the script.
# The script defines a command `main` that takes two arguments: `name` and `length`.

@click.command()
@click.option("--name", 
              help='The topic to search for on Wikipedia.')
@click.option("--length", 
              help='The length of the wikipedia output.')

def cli(name, length):
    """
    Scrape a summary from Wikipedia for the given topic.
    """
    result = scrape(name, length)
    click.echo(click.style(f"{result}", fg="green"))


if __name__ == "__main__":
    cli(name="Microsoft", length=2)