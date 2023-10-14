"""
Data Visualizaiton Module

(Not Final)
"""
import matplotlib.pyplot as plt

class DataVis:

    def __init__(self, x_data, y_data, title, x_label, y_label, plot_type='line', color=None):
    # Create a new figure and axis
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.plot_type = plot_type
        self.color = color

    def plot(self):
        fig, ax = plt.subplots()

        # Plot the data based on the chosen plot type
        if self.plot_type == 'line':
            ax.plot(self.x_data, self.y_data, label='Data', color=self.color)
        elif self.plot_type == 'scatter':
            ax.scatter(self.x_data, self.y_data, label='Data', color=self.color)
        elif self.plot_type == 'bar':
            ax.bar(self.x_data, self.y_data, label='Data', color=self.color)

        # Set plot titles and labels
        ax.set_title(self.title)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)

        # Add a legend if needed
        ax.legend()

        # Add a header if provided
        if self.header:
            plt.figtext(0.5, 0.92, fontsize=12, ha='center')

        # Show the plot
        fig.tight_layout()
        plt.show()