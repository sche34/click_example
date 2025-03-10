from voorbeeld.visual_class import CreateVisual
import matplotlib.pyplot as plt


class Visual1(CreateVisual):
    def create_visual(self):
        fig, ax = plt.subplots()
        self.apply_settings(ax)

        # Example plot data
        ax.plot([1, 2, 3, 4], [9, 11, 8, 7], label="Line 1")

        plt.savefig(self.settings.output_folder / "week1_bar_plot")
