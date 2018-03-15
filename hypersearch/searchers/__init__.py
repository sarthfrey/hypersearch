import numpy as np
from ..config import ConfigFile
from ..hyperparameters import ParameterSet

class Searcher(object):

	def __init__(self, obj_func, n_iter, param_file):
		self._obj_func = obj_func
		self._n_iter = n_iter
		self._param_def = ConfigFile(param_file).load()
		self._param_set = ParameterSet(self.param_def)
		self._results = []

	def sample_params(self):
		return self.param_set.sample()

	def best_result(self):
		return max(self.results, key=lambda result_dict: result_dict['result'])

        @property
        def obj_func(self):
                return self._obj_func

	@property
        def n_iter(self):
                return self._n_iter

	@property
        def param_def(self):
                return self._param_def

	@property
        def param_set(self):
                return self._param_set

	@property
	def results(self):
		return self._results