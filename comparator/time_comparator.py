from common.utils import log
import matplotlib.pyplot as plt


class TimeComparator(object):
    def __init__(self, algorithms):
        """
        :type algorithms: list[algorithm.abstract_algorithm.AbstractAlgorithm]
        """
        self.algorithms = algorithms
        self.algs_to_stats = {}

    def run(self):
        for algorithm in self.algorithms:
            log("Running {}...".format(algorithm))
            algorithm.run()
            log("{} ended!".format(algorithm))
            self.algs_to_stats[algorithm] = algorithm.get_stats()

    def _gather_results(self):
        alg_to_time_and_values = {}
        for algorithm, stats in self.algs_to_stats.iteritems():
            time_values, min_values = zip(
                *[(stat_dict.get("time"), stat_dict.get("min")) for stat_dict in stats.values()])
            alg_to_time_and_values[algorithm] = (time_values, min_values)
        return alg_to_time_and_values

    def show_stats(self):
        colors = ["b", "g", "r", "c", "m", "k"]
        alg_to_time_and_values = self._gather_results()
        plt.xlabel("Time (s)")
        plt.ylabel("min found distance")
        c = 0
        legends = []
        for algorithm, (time_series, value_series) in alg_to_time_and_values.iteritems():
            label = str(algorithm)
            line,  = plt.plot(time_series, value_series, "{}--".format(colors[c]), label=label)
            legends.append(line)
            c += 1
        plt.legend(handles=legends)
        plt.show()
