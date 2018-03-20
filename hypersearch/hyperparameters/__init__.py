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

	def __init__(self, name, categories, type='qualitative'):
		assert type == 'qualitative'
		CategoricalParameter.__init__(self, name, categories)
		self.ids = range(self.num_categories)
                self.category_id_map = dict((categories[id], id) for id in self.ids)
                self.id_category_map = dict((id, categories[id]) for id in self.ids)

	def sample(self, num_samples=None):
		return CategoricalParameter.sample(self, self.categories, num_samples)


class RealParameter(NumericalParameter):

	def __init__(self, name, lower_bound, upper_bound, type='real'):
		assert type == 'real'
		NumericalParameter.__init__(self, name, lower_bound, upper_bound)

	def sample(self, num_samples=None):
		return np.random.uniform(self.lower_bound, self.upper_bound, num_samples)


class DiscreteParameter(NumericalParameter, CategoricalParameter):

        def __init__(self, name, lower_bound, upper_bound, step=1, type='discrete'):
		assert type == 'discrete'
		NumericalParameter.__init__(self, name, lower_bound, upper_bound)
		CategoricalParameter.__init__(self, name, categories=np.arange(lower_bound, upper_bound, step))

        def sample(self, num_samples=None):
                return CategoricalParameter.sample(self, self.categories, num_samples)


class ParameterSet(object):

	def __init__(self, parameters):
		self.parameter_dict = {}
		for name, parameter in parameters.items():
			parameter['name'] = name
			if parameter['type'] == 'real':
				self.parameter_dict[name] = RealParameter(**parameter)
			elif parameter['type'] == 'discrete':
				self.parameter_dict[name] = DiscreteParameter(**parameter)
			elif parameter['type'] == 'qualitative':
				self.parameter_dict[name] = QualitativeParameter(**parameter)
			else:
				raise ValueError('parameter type is unsupported')

	def sample(self):
		return {name: parameter.sample() for name, parameter in self.parameter_dict.items()}

