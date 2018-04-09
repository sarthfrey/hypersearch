import docopt
from hypersearch.searchers import RandomSearcher


def f(params, arg_dict):
	objective = 9 - params['x'] ** 2
	print arg_dict['test']
	return {'objective': objective}

if __name__ == '__main__':
	searcher = RandomSearcher(n_iter=5, param_file='test.yaml', obj_func=f, arg_dict={'test':'helloworld'})
	searcher.search()
	print searcher.best_result()

