import yaml
import math
import numpy as np
from ..config import ConfigFile
from ..hyperparameters import ParameterSet

class Searcher(object):

	def __init__(self, obj_func, n_iter, param_file, arg_dict={}):
		self._obj_func = obj_func
		self._n_iter = n_iter
		with open(param_file, 'r') as f:
			self._param_def = yaml.load(f)
		self._arg_dict = arg_dict
		self._param_set = ParameterSet(self.param_def)
		self._results = []

	def sample_params(self):
		return self.param_set.sample()

	def best_result(self):
		return max(filter(lambda result_dict: not math.isnan(result_dict['objective']), self.results), key=lambda result_dict: result_dict['objective'])

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
