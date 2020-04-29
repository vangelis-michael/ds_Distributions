class Distribution:

    """ Gaussian distribution class for calculating and visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats extracted from the data file

    """

    # Init magic method allows you change how python instantiates an object
    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, filename):
        """Function to read in data from a txt file. The tt file should have one number (float) per line.
        The numbers are stored in the data attribute. After reading in the file, the mean and standard deviation are
        calculated.
        Args:
            filename (string): name of a file to read from

        Returns:
            None
        """
        with open(filename) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
