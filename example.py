import docopt
from hypersearch.searchers import RandomSearcher


def f(params):
	objective = 9 - params['x'] ** 2
	return {'objective': objective}

if __name__ == '__main__':
	searcher = RandomSearcher(n_iter=5, param_file='test.yaml', obj_func=f)
	searcher.search()
	print searcher.best_result()

