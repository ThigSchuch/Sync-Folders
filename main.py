from argparser import valid_args
from config import ConfigArgs, ConfigFile
from sync import Sync

if __name__ == "__main__":

    valid, args = valid_args()

    if valid:
        config = ConfigArgs(
            source_folder=args["source"],
            replica_folder=args["replica"],
            interval_sync=args["interval"],
            log_file=args["log"],
        )

    else:
        config = ConfigFile()

    synchronization = Sync(configuration=config)
    synchronization.start()
