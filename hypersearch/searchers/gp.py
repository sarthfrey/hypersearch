from ..searchers.iterative import IterativeSearcher

class GaussianSearcher(IterativeSearcher):

        def __init__(self, obj_func, n_iter, n_sample, param_file, kind='ucb', kappa=2.576, xi=0.0):
                IterativeSearcher.__init__(self, obj_func, n_iter, n_sample, param_file, decision_func=self.predict)
                self.iterative_searcher = IterativeSearcher(obj_func, n_iter, n_sample, param_file, decision_func=self.predict)
                self.utility_func = UtilityFunction(kind='ucb', kappa=2.576, xi=0.0)

        def search(self):
                self.iterative_searcher.search()
                self.results = self.iterative_searcher.results

        def predict(self):
                pass #TODO

