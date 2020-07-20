import argparse
from cognidiscovery.utils.config import Config
from cognidiscovery.model import Parser, Annotator, Indexer, Interpreter
from cognidiscovery.utils.data import DataLoader
from cognidiscovery.utils.response_creator import ResponseCreator

def train(config,model_directory,annotations):
    data_loader = DataLoader()
    data_loader.from_json(path=annotations)
    data_loader = annotate(config, model_directory, data_loader)
    interpreter = index(config, model_directory, data_loader)
    return data_loader, interpreter


def predict(query, config, model_directory):
    interpreter = Interpreter.load(model_directory)
    output = interpreter.parse(query)
    return ResponseCreator(data=interpreter.data).process(output.get('result'), output.get('distance'),
                                                          output.get('cosine_sim'))


def load_config(conf_path):
    return Config.load(conf_path)


def call_train(args: argparse.Namespace):
    train(config=load_config(args.config),model_directory=args.model_directory,annotations = args.annotations)


def call_parse(args: argparse.Namespace):
    parse(config=load_config(args.config),model_directory=args.model_directory)


def call_predict(args: argparse.Namespace):
    print(predict(query = args.query, config=load_config(args.config),model_directory=args.model_directory))
