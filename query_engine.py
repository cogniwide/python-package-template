from encoders.one_hot_encoder import OneHotTextEncoder
from encoders.bert_encoder import BertEncoder
from indexers.faiss_indexer import FaissIndexer
from rankers.basic_ranker import BasicRanker
import numpy as np
import time

class QueryEngine():
    def __init__(self,model_dir):
        self.model_dir = model_dir

        self.indexer = FaissIndexer()
        self.indexer.load(self.model_dir)

        self.encoder = BertEncoder()

        self.ranker = BasicRanker()
        self.ranker.load(self.model_dir)

    def process(self,query,k=1):
        """
            ranking(NL Query, NLP features(sentiment, intent), Image search ) =>
                connectors (Rest, gRPC, Rasa)

        :param doc_path:
        :param output_dir:
        :return:
        """

        st = time.time()
        encoded_query = self.encoder.encode(np.array([query])).astype(np.float32)


        result,distance = self.indexer.query(encoded_query,k)
        print(distance)

        result = self.ranker.process(result, distance)
        et = time.time()

        print(et - st, ' seconds')
        return result


if __name__ == "__main__":
    # import argparse
    #
    # parser = argparse.ArgumentParser(description="Cognidocs commandline tool")
    #
    # parser.add_argument("-o", "--model-folder", type=str, nargs=1,
    #                     metavar="model_folder_path", default="output/model",
    #                     help="choose  model folder")
    #
    # # parse the arguments from standard input
    # args = parser.parse_args()
    # model_dir = args.model_folder_path
    model_dir = "output/model"
    predictor = QueryEngine(model_dir)
    query = "Wrist placement"
    print(predictor.process(query))