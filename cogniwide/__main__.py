import argparse
from cogniwide.train import call_train, call_parse, call_predict
import logging
logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)


def create_argument_parser():
    """Parse all the command line arguments for the training script."""

    parser = argparse.ArgumentParser(
        prog="cognidiscovery",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="NO DESCRIPTION ADDED",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Print installed cognidiscovery version",
    )
    parser.add_argument('-c', '--config',default="config.yml", help='<Required> config file path')

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parsers = [parent_parser]

    subparsers = parser.add_subparsers(help="CogniDiscovery commands")


    scaffold_parser = subparsers.add_parser(
        "init",
        parents=parent_parsers,
        help="Creates a new project, with example training data, actions, and config files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    scaffold_parser.set_defaults(func=run)

    train_parser = subparsers.add_parser(
        "train",
        help="Trains a model",
        parents=parent_parsers,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    train_parser.add_argument('-a', '--annotations', default="annotations.json", type=str, help='annotation json')
    train_parser.add_argument('-m', '--model_directory', default="models/", type=str, help='Model output directory')

    train_parser.set_defaults(func=call_train)


    doc_parser = subparsers.add_parser(
        "parse",
        help="Trains a model",
        parents=parent_parsers,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    doc_parser.add_argument('-m', '--model_directory', default="models/", type=str, help='Model output directory')

    doc_parser.set_defaults(func=call_parse)

    doc_parser = subparsers.add_parser(
        "predict",
        help="predicts query model",
        parents=parent_parsers,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    doc_parser.add_argument('-q', '--query', default="hi", type=str, help='Enter Query')
    doc_parser.add_argument('-m', '--model_directory', default="models/", type=str, help='Model output directory')
    doc_parser.set_defaults(func=call_predict)

    return parser


def main():
    # Running as standalone python application
    import os
    import sys

    arg_parser = create_argument_parser()
    cmdline_arguments = arg_parser.parse_args()

    # insert current path in syspath so custom modules are found
    sys.path.insert(1, os.getcwd())

    if hasattr(cmdline_arguments, "func"):
        cmdline_arguments.func(cmdline_arguments)
    else:
        # user has not provided a subcommand, let's print the help
        logger.error("No command specified.")
        arg_parser.print_help()
        exit(1)


if __name__ == "__main__":
    main()
