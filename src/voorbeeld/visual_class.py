from pathlib import Path

class PlotSettings:
    output_folder = Path("output")

    def __init__(self, title="", xlabel="", ylabel="", axis_on=True, grid_on=False, legend_on=False):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.axis_on = axis_on
        self.grid_on = grid_on
        self.legend_on = legend_on

    def apply_settings(self, ax):
        ax.set_title(self.title)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        if not self.axis_on:
            ax.axis('off')
        if self.grid_on:
            ax.grid(True)
        if self.legend_on:
            ax.legend()