import numpy as np


class Parameter(object):

	def __init__(self, name):
		self.name = name


class CategoricalParameter(Parameter):

	def __init__(self, name, categories):
		Parameter.__init__(self, name)
		self.categories = categories
		self.num_categories = len(categories)

	def sample(self, categories, num_samples=None):
		return np.random.choice(categories, num_samples)


class NumericalParameter(Parameter):

        def __init__(self, name, lower_bound, upper_bound):
                Parameter.__init__(self, name)
                self.lower_bound = lower_bound
                self.upper_bound = upper_bound


class QualitativeParameter(CategoricalParameter):

	def __init__(self, name, categories):
		CategoricalParameter.__init__(self, name, categories)
		self.ids = range(self.num_categories)
                self.category_id_map = dict((categories[id], id) for id in self.ids)
                self.id_category_map = dict((id, categories[id]) for id in self.ids)

	def sample(self, num_samples=None):
		return CategoricalParameter.sample(self, self.categories, num_samples)


class ContinuousParameter(NumericalParameter):

	def __init__(self, name, lower_bound, upper_bound):
		NumericalParameter.__init__(self, name, lower_bound, upper_bound)

	def sample(self, num_samples=None):
		return np.random.uniform(self.lower_bound, self.upper_bound, num_samples)


class DiscreteParameter(NumericalParameter, CategoricalParameter):

        def __init__(self, name, lower_bound, upper_bound, step):
                NumericalParameter.__init__(self, name, lower_bound, upper_bound)
                CategoricalParameter.__init__(self, name, categories=np.arange(lower_bound, upper_bound, step))

        def sample(self, num_samples=None):
                return CategoricalParameter.sample(self, self.categories, num_samples)


class ParameterSet(object):

	def __init__(self, parameters):
		self.parameters = parameters
		self.parameter_dict = dict((parameter.name, parameter) for parameter in parameters)

	def get_random(self):
		return dict((parameter.name, parameter.sample()) for parameter in self.parameters)
