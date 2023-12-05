import logging
import sys

import click

logger = logging.getLogger(__name__)

try:
    logger.info(sys.ps1)
except AttributeError:
    logger.warning("No sys.ps1")


@click.command()
def run():
    result = 1 + 1
    logger.info(result)
