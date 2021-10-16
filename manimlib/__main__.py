#!/usr/bin/env python
from .config import parse_cli, get_configuration
from .extract_scene import main
from .utils.init_config import init_customization


def main():
    args = parse_cli()

    if args.config:
        init_customization()
    else:
        config = get_configuration(args)
        scenes = main(config)

        for scene in scenes:
            scene.run()


if __name__ == '__main__':
    main()
