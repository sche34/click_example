from voorbeeld.visual_class import CreateVisual
import matplotlib.pyplot as plt


class Visual2(CreateVisual):
    def create_visual(self):
        fig, ax = plt.subplots()
        self.apply_settings(ax)

        # Example bar plot data
        categories = ["A", "B", "C"]
        values = [10, 20, 15]
        ax.bar(categories, values)
        plt.savefig(self.settings.output_folder / "week2_bar_plot.png")
