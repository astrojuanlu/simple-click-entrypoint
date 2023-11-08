import logging
import sys

import click

logger = logging.getLogger(__name__)

try:
    logger.info(sys.ps1)
except AttributeError:
    logger.warning("No sys.ps1")


@click.command()
def main():
    result = 1 + 1
    logger.info(result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()

    logger.info("End of direct module execution")
