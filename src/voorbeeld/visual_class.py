from abc import ABC, abstractmethod
import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    title: str
    xlabel: str
    ylabel: str
    axis_off: bool
    grid_on: bool
    legend_on: bool
    output_folder: Path


class CreateVisual(ABC):
    def __init__(self, section: str):
        self.settings = self.load_settings(section)

    def set_config(self):
        configfile = Path("config.toml").resolve()
        with configfile.open("rb") as f:
            self.config = tomllib.load(f)

    def load_settings(self, section: str) -> Settings:
        self.set_config()
        config_general = self.config["general"]
        config_visual = self.config[section]

        return Settings(
            title=config_visual["title"],
            xlabel=config_visual["xlabel"],
            ylabel=config_visual["ylabel"],
            axis_off=config_visual.get("axis_off", False),
            grid_on=config_visual.get("grid_on", False),
            legend_on=config_visual.get("legend_on", False),
            output_folder=Path(config_general["output_folder"]),
        )

    @abstractmethod
    def create_visual(self) -> None:
        pass

    def apply_settings(self, ax):
        ax.set_title(self.settings.title)
        ax.set_xlabel(self.settings.xlabel)
        ax.set_ylabel(self.settings.ylabel)
        if self.settings.axis_off:
            ax.set_axis_off()
        if self.settings.grid_on:
            ax.grid(True)
        if self.settings.legend_on:
            ax.legend()
