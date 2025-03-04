from voorbeeld.visual_class import PlotSettings
import matplotlib.pyplot as plt

def create_visual2():
    fig, ax = plt.subplots()
    settings = PlotSettings(title="Week 2 Bar Plot", xlabel="Categories", ylabel="Values", axis_on=True, grid_on=True, legend_on=False)
    settings.apply_settings(ax)
    
    # Example bar plot data
    categories = ['A', 'B', 'C']
    values = [10, 20, 15]
    ax.bar(categories, values, label="Week 2 Data")
    
    plt.savefig(settings.output_folder / "week2_bar_plot")

if __name__ == "__main__":
    create_visual2()