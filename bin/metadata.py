import click
import sys
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

from arxiv_public_data.oai_metadata import all_of_arxiv

@click.command()
@click.option('--outfile', type=str, default=None)
@click.option('--oai_from', type=str, default=None)
@click.option('--oai_until', type=str, default=None)
@click.option('--oai_set', type=str, default=None)
def main(outfile=None, oai_from=None, oai_until=None, oai_set=None):
    
    oai_set_prefix = 'all' if oai_set is None else oai_set
    if outfile is None:
        outfile = Path(os.environ.get('ROOT_DB')) / 'oai_arxiv' / f'{oai_set_prefix}_dataset.json.gz'
    oai_kwargs = {}
    for key, val in zip(['from','until','set'], [oai_from, oai_until, oai_set]):
        if val is not None:
            oai_kwargs[key] = val

    all_of_arxiv(outfile=str(outfile), oai_kwargs=oai_kwargs)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main()
