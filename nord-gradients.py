from enum import Enum
from functools import partial
import json
import logging
from pathlib import Path
import subprocess
import sys

from tqdm import tqdm as base_tqdm


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
tqdm = partial(base_tqdm, bar_format='{desc} |{bar}| {n_fmt}/{total_fmt}')

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR.joinpath("images")
CONFIG_FILE_PATH = BASE_DIR.joinpath("config.json")


class NordColor(Enum):
    # polar night
    nord0 = "#2E3440"
    nord1 = "#3B4252"
    nord2 = "#434C5E"
    nord3 = "#4C566A"
    # snow storm
    nord4 = "#D8DEE9"
    nord5 = "#E5E9F0"
    nord6 = "#ECEFF4"
    # frost
    nord7 = "#8FBCBB"
    nord8 = "#88C0D0"
    nord9 = "#81A1C1"
    nord10 = "#5E81AC"
    # aurora
    nord11 = "#BF616A"
    nord12 = "#D08770"
    nord13 = "#EBCB8B"
    nord14 = "#A3BE8C"
    nord15 = "#B48EAD"


def load_config() -> dict:
    with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    logging.info("Starting execution")
    logging.info("Loading config file")
    config = load_config()
    logging.info("Generating gradients")
    with tqdm(config["dimensions"], desc="Dimensions") as pbar_0:
        for dimension in pbar_0:
            pbar_0.set_description(f"{dimension['width']}x{dimension['height']}")
            width = dimension["width"]
            height = dimension["height"]
            dimension_dir = IMAGES_DIR.joinpath(f"{width}x{height}")
            with tqdm(config["angles"], desc="Angles", leave=False) as pbar_1:
                for angle in pbar_1:
                    pbar_1.set_description(f"{angle} degrees")
                    angle_dir = dimension_dir.joinpath(f"{angle}-degrees")
                    with tqdm(config["gradients"], desc="Gradients", leave=False) as pbar_2:
                        for gradient in pbar_2:
                            pbar_2.set_description(f"{gradient['from']} to {gradient['to']}")
                            from_hex = NordColor[gradient["from"]].value
                            to_hex = NordColor[gradient["to"]].value
                            output_path = angle_dir.joinpath(f"{gradient['from']}-to-{gradient['to']}-{width}x{height}-{angle}°.png")
                            output_path.parent.mkdir(parents=True, exist_ok=True)
                            command = [
                                "magick",
                                "-size",
                                f"{width}x{height}",
                                "-define",
                                f"gradient:angle={angle}",
                                f"gradient:{from_hex}-{to_hex}",
                                f"{output_path.as_posix()}"
                            ]
                            subprocess.run(command)
    logging.info("Execution finished")
