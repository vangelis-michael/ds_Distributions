import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution


class Binomial(Distribution):
    """Binomial distribution class for calculating and visualizing a binomial distribution
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, prob=0.5, size=20):
        # Distribution.__init__(self, mu, sigma)
        self.proba = prob
        self.tries = size

    def calculate_mean(self):
        avg = self.tries*self.proba
        self.mean = avg
        return self.mean

    def calculate_stdev(self):

        # if sample:
        #     n = len(self.data) - 1
        # else:
        #     n = len(self.data)

        mean = self.mean
        sigma = 0

        # for d in self.data:
        #     sigma += (d - mean) ** 2

        sigma = math.sqrt(self.tries * self.proba * (1-self.proba))
        self.stdev = sigma
        return self.stdev

    def read_data_file(self, filename, sample=True):
        with open(filename) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    # def plot_histogram(self):
    #     plt.hist(self.data)
    #     plt.title('Histogram of Data')
    #     plt.xlabel('data')
    #     plt.ylabel('count')

    # def pdf(self, x):
    #     return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)

    # def plot_histogram_pdf(self, n_spaces=50):
    #     mu = self.mean
    #     sigma = self.stdev

    #     min_range = min(self.data)
    #     max_range = max(self.data)

    #     # Calculate the interval between x values
    #     interval = 1.0 * (max_range - min_range) / n_spaces

    #     x = []
    #     y = []

    #     # Calculate the x values to visualize
    #     for i in range(n_spaces):
    #         tmp = min_range + interval * i
    #         x.append(tmp)
    #         y.append(self.pdf(tmp))

    #     # make the plots
    #     fig, axes = plt.subplots(2, sharex=True)
    #     fig.subplots_adjust(hspace=.5)
    #     axes[0].hist(self.data, density=True)
    #     axes[0].set_title('Binomial Histogram of Data')
    #     axes[0].set_ylabel('Density')

    #     axes[1].plot(x, y)
    #     axes[1].set_title('Binomial Distribution for \n Sample Mean and Sample Standard Deviation')
    #     axes[0].set_ylabel("Density")
    #     plt.show()

    #     return x, y

    # Magic method: helps you override and customize default python behavior
    # For instance adding two gaussians together
    def __add__(self, other):
        """Function to add together two gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """
        result = Binomial()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)

        return result

    # Prints a standard representation
    def __repr__(self):
        """Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian
        """
        return 'mean {}, standard deviation {}, number of tries {}, probability {}'.format(self.mean, self.stdev, self.tries, self.proba)
