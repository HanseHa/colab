
from click.testing import CliRunner
from wikibot import cli
from mylib.bot import scrape


def test_scrape():
    
    assert "Microsoft" in scrape("Microsoft")

def test_wikibot():

    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Python (programming language)', '--length', '2'])
    assert result.exit_code == 0
    assert "Python" in result.output