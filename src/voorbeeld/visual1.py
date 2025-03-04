
from voorbeeld.visual_class import PlotSettings
import matplotlib.pyplot as plt

def create_visual1():
    fig, ax = plt.subplots()
    settings = PlotSettings(title="Visual 1", xlabel="X Axis", ylabel="Y Axis", axis_on=True, grid_on=True, legend_on=False)
    settings.apply_settings(ax)
    
    # Example plot data
    ax.plot([1, 2, 3], [4, 7, 6], label="Line 1")
    
    plt.savefig(settings.output_folder / "week1_bar_plot")

if __name__ == "__main__":
    create_visual1()