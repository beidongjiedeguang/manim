#!/usr/bin/env python
import manimlib
from manimlib import __version__
from .config import parse_cli, get_configuration
from . import extract_scene
from .utils.init_config import init_customization


def main():
    print(f"ManimGL \033[32mv{__version__}\033[0m")
    args = parse_cli()

    if args.version and args.file == None:
        return
    if args.log_level:
        manimlib.logger.log.setLevel(args.log_level)

    if args.config:
        init_customization()
    else:
        config = get_configuration(args)
        scenes = extract_scene.main(config)

        for scene in scenes:
            scene.run()


if __name__ == "__main__":
    main()
