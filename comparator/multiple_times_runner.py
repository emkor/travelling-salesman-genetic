from common.utils import log
import matplotlib.pyplot as plt


class MultipleTimesRunner(object):
    def __init__(self, algorithm):
        """
        :type algorithm: algorithm.genetic.GeneticSalesman
        """
        self.algorithm = algorithm
        self.run_to_stats = {}

    def run(self, times=10):
        for run in xrange(0, times):
            log("Starting algorithm {}, run #{}".format(self.algorithm, self.run))
            self.algorithm.run()
            alg_run_stats = self.algorithm.get_stats()
            self.run_to_stats[run] = alg_run_stats

    def average_stats(self):
        generation_to_min_values = self._initialize_empty(self.algorithm.max_generations)
        generation_to_avg_values = self._initialize_empty(self.algorithm.max_generations)
        generation_to_max_values = self._initialize_empty(self.algorithm.max_generations)
        for run_number, run_stats in self.run_to_stats.iteritems():
            for generation, stats in run_stats.iteritems():
                generation_to_min_values[generation-1].append(stats.get("min"))
                generation_to_avg_values[generation-1].append(stats.get("avg"))
                generation_to_max_values[generation-1].append(stats.get("max"))
        gen_to_min_avg = {gen: self._average(min_values) for gen, min_values in generation_to_min_values.iteritems()}
        gen_to_avg_avg = {gen: self._average(avg_values) for gen, avg_values in generation_to_avg_values.iteritems()}
        gen_to_max_avg = {gen: self._average(max_values) for gen, max_values in generation_to_max_values.iteritems()}

        gen_to_avg_stats = {}
        for gen, min_avg in gen_to_min_avg.iteritems():
            avg_avg = gen_to_avg_avg.get(gen)
            max_avg = gen_to_max_avg.get(gen)
            gen_to_avg_stats.update({gen: (min_avg, avg_avg, max_avg)})

        return gen_to_avg_stats

    def _initialize_empty(self, run_count):
        return {run: [] for run in xrange(0, run_count)}

    def _average(self, values):
        """
        :type values: list
        :rtype: float
        """
        return float(sum(values)) / float(len(values))

    def show_stats(self, gen_to_stats):
        generations = gen_to_stats.keys()
        mins = [stats[0] for _, stats in gen_to_stats.iteritems()]
        avgs = [stats[1] for _, stats in gen_to_stats.iteritems()]
        maxs = [stats[2] for _, stats in gen_to_stats.iteritems()]
        plt.plot(generations, mins, 'r--', generations, avgs, 'b--', generations, maxs, 'g--')
        plt.xlabel("Generation")
        plt.ylabel("min / avg / max distance of whole population")
        plt.show()
