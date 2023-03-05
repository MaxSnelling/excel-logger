import yaml
from utils import cell

CONFIG_PATH = 'config.yaml'


def get_file_path() -> str:
    """
    Import spreadsheet file path from config file.

    :return: path to spreadsheet file.
    """
    with open(CONFIG_PATH, 'r') as file:
        config = yaml.safe_load(file)
        return config['source']['file']


def get_cells() -> list:
    """
    Import cell information from config file.

    :return: List of cells in config file.
    """
    with open(CONFIG_PATH, 'r') as file:
        config = yaml.safe_load(file)
        cells_input = config['source']['cells']
        return [cell(i['descriptor'], i['row'], i['col']) for i in cells_input]
