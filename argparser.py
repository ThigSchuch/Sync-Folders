import argparse

parser = argparse.ArgumentParser(description="Sync folders")
parser.add_argument(
    "--source",
    type=str,
    help="Source folder to sync",
)
parser.add_argument(
    "--replica",
    type=str,
    help="Replica folder to sync",
)
parser.add_argument(
    "--interval",
    type=int,
    help="Interval sync in seconds",
    default=60,
)
parser.add_argument(
    "--log",
    type=str,
    help="Log file",
    default="sync.log",
)

ARGS = parser.parse_args()


def valid_args() -> tuple[bool, dict]:
    """
    Check if the provided arguments are valid for syncing folders.

    Returns a tuple with a boolean indicating if the arguments are valid and a dictionary of the arguments.

    Returns:
        tuple[bool, dict]: A tuple containing a boolean indicating if the arguments are valid and a dictionary of the arguments.
    """
    if ARGS.source or ARGS.replica:
        if not ARGS.source or not ARGS.replica:
            parser.error("You must provide the source and replica folders")

        if ARGS.interval and ARGS.interval <= 0:
            parser.error("The interval sync must be greater than 0")

        return True, vars(ARGS)

    return False, vars(ARGS)
