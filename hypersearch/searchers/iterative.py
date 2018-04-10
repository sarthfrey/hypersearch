from ..searchers.base import Searcher
from ..searchers.random import RandomSearcher

class IterativeSearcher(Searcher):

        def __init__(self, obj_func, n_iter, n_sample, param_file, decision_func):
                Searcher.__init__(self, obj_func, n_iter, param_file)
                self.decision_func = decision_func
                self.n_sample = n_sample
                self.random_searcher = RandomSearcher(obj_func=obj_func, n_iter=n_sample, param_file=param_file)

        def search():
                self.random_searcher.search()
                self.results = self.random_searcher.results
                if self.n_iter > self.n_sample:
                        for i in xrange(self.n_iter - self.n_sample):
                                params = decision_func(self.results)
                                meta_dict = self.obj_func(params)
                                self.results.append({'objective': meta_dict['objective'], 'meta_dict': meta_dict, 'hyperparams': params})

