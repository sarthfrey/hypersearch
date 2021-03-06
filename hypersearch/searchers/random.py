import numpy as np
from ..searchers.base import Searcher


class RandomSearcher(Searcher):

	def __init__(self, obj_func, n_iter, param_file, arg_dict={}):
		Searcher.__init__(self, obj_func, n_iter, param_file, arg_dict)

	def search(self):
		for i in range(self.n_iter):
			params = self.sample_params()
			meta_dict = self.obj_func(params, self._arg_dict)
			self.results.append({'objective': meta_dict['objective'], 'meta_dict': meta_dict, 'hyperparams': params})

