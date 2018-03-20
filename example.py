import docopt
from hypersearch.searchers.random import RandomSearcher


def f(params):
	return 9 - params['x'] ** 2

if __name__ == '__main__':
	searcher = RandomSearcher(n_iter=3, param_file='test.yaml', obj_func=f)
	searcher.search()
	print searcher.best_result()
	print searcher.results

