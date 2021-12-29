import sys

from src.GraphAlgo import GraphAlgo


def main():
    file_name = str(sys.argv[1])
    graph_algo = GraphAlgo()
    graph_algo.load_from_json(file_name)
    graph_algo.plot_graph()


if __name__ == '__main__':
    main()
