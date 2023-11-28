import csv
import os
import re
from pathlib import Path

from bio_dose_response import calculate_dilution_series
from chem_operators import ChemOperators
from excel_handler import get_source_layout

from extra_functions import unit_converter
import numpy as np

from info import unit_converter_dict, unit_converter_list
from csv_handler import CSVWriter
from database_handler import DataBaseFunctions


def testing(well_dict, vol_needed_pure):

    groups = set()
    for well_counter, wells in enumerate(well_dict):
        if well_counter == 250:
            print(well_dict[wells])
        group = well_dict[wells]["group"]
        groups.add(group)
    print(groups)


def get_data(config, file):
    dbf = DataBaseFunctions(config)
    all_compounds = {}
    with open(file, "r", newline="\n") as csv_file:
        all_lines = csv_file.readlines()

        for line in all_lines:
            line = line.strip()
            line = line.split(";")

            if line[-1] != "":
                compound_id = line[-1]
                row_data = dbf.find_data_single_lookup("compound_main", compound_id, "compound_id")
                if row_data:
                    smiles = row_data[0][2]
                    temp_mw = ChemOperators.mw_from_smiles(smiles)
                    all_compounds[compound_id] = {"well": line[0], "mw": temp_mw}

    new_file = Path(r"C:\Users\phch\Desktop\test\new.txt")
    new_file.touch()
    headlines = ["well", "mw", "compound_id"]
    with open(new_file, "w", newline="\n") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(headlines)

        for data in all_compounds:
            row_data = [all_compounds[data]["well"], all_compounds[data]["mw"], data]
            csv_writer.writerow(row_data)



def testing():



if __name__ == "__main__":
    source_layout = {"positive":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "negative":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "max":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "minimum":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "blank":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "empty":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "filler":
                         {"use": False,
                          "compound": "",
                          "source_wells": {0: {"well_id": "",
                                               "vol": 0,
                                               "plate": ""}},
                          "well_counter": 0,
                          "transfer_volume": ""},
                     "sample":
                         {}
                       }

    import configparser
    config = configparser.ConfigParser()
    config.read("config.ini")

    ex_file = Path(r"C:\Users\phch\Desktop\test\dose_response\dose_reposnse_layout.xlsx")
    source_layout = get_source_layout(ex_file, source_layout)

    well_dict = {1: {'group': 0, 'well_id': 'A1', 'state': 'empty', 'colour': '#1e0bc8'}, 2: {'group': 0, 'well_id': 'B1', 'state': 'empty', 'colour': '#1e0bc8'}, 3: {'group': 0, 'well_id': 'C1', 'state': 'empty', 'colour': '#1e0bc8'}, 4: {'group': 0, 'well_id': 'D1', 'state': 'empty', 'colour': '#1e0bc8'}, 5: {'group': 0, 'well_id': 'E1', 'state': 'empty', 'colour': '#1e0bc8'}, 6: {'group': 0, 'well_id': 'F1', 'state': 'empty', 'colour': '#1e0bc8'}, 7: {'group': 0, 'well_id': 'G1', 'state': 'empty', 'colour': '#1e0bc8'}, 8: {'group': 0, 'well_id': 'H1', 'state': 'empty', 'colour': '#1e0bc8'}, 9: {'group': 0, 'well_id': 'I1', 'state': 'empty', 'colour': '#1e0bc8'}, 10: {'group': 0, 'well_id': 'J1', 'state': 'empty', 'colour': '#1e0bc8'}, 11: {'group': 0, 'well_id': 'K1', 'state': 'empty', 'colour': '#1e0bc8'}, 12: {'group': 0, 'well_id': 'L1', 'state': 'empty', 'colour': '#1e0bc8'}, 13: {'group': 0, 'well_id': 'M1', 'state': 'empty', 'colour': '#1e0bc8'}, 14: {'group': 0, 'well_id': 'N1', 'state': 'empty', 'colour': '#1e0bc8'}, 15: {'group': 0, 'well_id': 'O1', 'state': 'empty', 'colour': '#1e0bc8'}, 16: {'group': 0, 'well_id': 'P1', 'state': 'empty', 'colour': '#1e0bc8'}, 17: {'group': 0, 'well_id': 'A2', 'state': 'empty', 'colour': '#1e0bc8'}, 18: {'group': 0, 'well_id': 'B2', 'state': 'minimum', 'colour': '#ff8000'}, 19: {'group': 0, 'well_id': 'C2', 'state': 'minimum', 'colour': '#ff8000'}, 20: {'group': 0, 'well_id': 'D2', 'state': 'minimum', 'colour': '#ff8000'}, 21: {'group': 0, 'well_id': 'E2', 'state': 'minimum', 'colour': '#ff8000'}, 22: {'group': 0, 'well_id': 'F2', 'state': 'minimum', 'colour': '#ff8000'}, 23: {'group': 0, 'well_id': 'G2', 'state': 'minimum', 'colour': '#ff8000'}, 24: {'group': 0, 'well_id': 'H2', 'state': 'minimum', 'colour': '#ff8000'}, 25: {'group': 0, 'well_id': 'I2', 'state': 'minimum', 'colour': '#ff8000'}, 26: {'group': 0, 'well_id': 'J2', 'state': 'minimum', 'colour': '#ff8000'}, 27: {'group': 0, 'well_id': 'K2', 'state': 'minimum', 'colour': '#ff8000'}, 28: {'group': 0, 'well_id': 'L2', 'state': 'minimum', 'colour': '#ff8000'}, 29: {'group': 0, 'well_id': 'M2', 'state': 'minimum', 'colour': '#ff8000'}, 30: {'group': 0, 'well_id': 'N2', 'state': 'minimum', 'colour': '#ff8000'}, 31: {'group': 0, 'well_id': 'O2', 'state': 'minimum', 'colour': '#ff8000'}, 32: {'group': 0, 'well_id': 'P2', 'state': 'empty', 'colour': '#1e0bc8'}, 33: {'group': 0, 'well_id': 'A3', 'state': 'empty', 'colour': '#1e0bc8'}, 34: {'group': 0, 'well_id': 'B3', 'state': 'max', 'colour': '#790dc1'}, 35: {'group': 0, 'well_id': 'C3', 'state': 'max', 'colour': '#790dc1'}, 36: {'group': 0, 'well_id': 'D3', 'state': 'max', 'colour': '#790dc1'}, 37: {'group': 0, 'well_id': 'E3', 'state': 'max', 'colour': '#790dc1'}, 38: {'group': 0, 'well_id': 'F3', 'state': 'max', 'colour': '#790dc1'}, 39: {'group': 0, 'well_id': 'G3', 'state': 'max', 'colour': '#790dc1'}, 40: {'group': 0, 'well_id': 'H3', 'state': 'max', 'colour': '#790dc1'}, 41: {'group': 0, 'well_id': 'I3', 'state': 'max', 'colour': '#790dc1'}, 42: {'group': 0, 'well_id': 'J3', 'state': 'max', 'colour': '#790dc1'}, 43: {'group': 0, 'well_id': 'K3', 'state': 'max', 'colour': '#790dc1'}, 44: {'group': 0, 'well_id': 'L3', 'state': 'max', 'colour': '#790dc1'}, 45: {'group': 0, 'well_id': 'M3', 'state': 'max', 'colour': '#790dc1'}, 46: {'group': 0, 'well_id': 'N3', 'state': 'max', 'colour': '#790dc1'}, 47: {'group': 0, 'well_id': 'O3', 'state': 'max', 'colour': '#790dc1'}, 48: {'group': 0, 'well_id': 'P3', 'state': 'empty', 'colour': '#1e0bc8'}, 49: {'group': 0, 'well_id': 'A4', 'state': 'empty', 'colour': '#1e0bc8'}, 50: {'group': 1, 'well_id': 'B4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 1}, 51: {'group': 1, 'well_id': 'C4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 1}, 52: {'group': 1, 'well_id': 'D4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 1}, 53: {'group': 2, 'well_id': 'E4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 1}, 54: {'group': 2, 'well_id': 'F4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 1}, 55: {'group': 2, 'well_id': 'G4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 1}, 56: {'group': 3, 'well_id': 'H4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 1}, 57: {'group': 3, 'well_id': 'I4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 1}, 58: {'group': 3, 'well_id': 'J4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 1}, 59: {'group': 4, 'well_id': 'K4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 1}, 60: {'group': 4, 'well_id': 'L4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 1}, 61: {'group': 4, 'well_id': 'M4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 1}, 62: {'group': 0, 'well_id': 'N4', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 63: {'group': 0, 'well_id': 'O4', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 64: {'group': 0, 'well_id': 'P4', 'state': 'empty', 'colour': '#1e0bc8'}, 65: {'group': 0, 'well_id': 'A5', 'state': 'empty', 'colour': '#1e0bc8'}, 66: {'group': 1, 'well_id': 'B5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 2}, 67: {'group': 1, 'well_id': 'C5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 2}, 68: {'group': 1, 'well_id': 'D5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 2}, 69: {'group': 2, 'well_id': 'E5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 2}, 70: {'group': 2, 'well_id': 'F5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 2}, 71: {'group': 2, 'well_id': 'G5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 2}, 72: {'group': 3, 'well_id': 'H5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 2}, 73: {'group': 3, 'well_id': 'I5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 2}, 74: {'group': 3, 'well_id': 'J5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 2}, 75: {'group': 4, 'well_id': 'K5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 2}, 76: {'group': 4, 'well_id': 'L5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 2}, 77: {'group': 4, 'well_id': 'M5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 2}, 78: {'group': 0, 'well_id': 'N5', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 79: {'group': 0, 'well_id': 'O5', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 80: {'group': 0, 'well_id': 'P5', 'state': 'empty', 'colour': '#1e0bc8'}, 81: {'group': 0, 'well_id': 'A6', 'state': 'empty', 'colour': '#1e0bc8'}, 82: {'group': 1, 'well_id': 'B6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 3}, 83: {'group': 1, 'well_id': 'C6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 3}, 84: {'group': 1, 'well_id': 'D6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 3}, 85: {'group': 2, 'well_id': 'E6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 3}, 86: {'group': 2, 'well_id': 'F6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 3}, 87: {'group': 2, 'well_id': 'G6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 3}, 88: {'group': 3, 'well_id': 'H6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 3}, 89: {'group': 3, 'well_id': 'I6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 3}, 90: {'group': 3, 'well_id': 'J6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 3}, 91: {'group': 4, 'well_id': 'K6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 3}, 92: {'group': 4, 'well_id': 'L6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 3}, 93: {'group': 4, 'well_id': 'M6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 3}, 94: {'group': 0, 'well_id': 'N6', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 95: {'group': 0, 'well_id': 'O6', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 96: {'group': 0, 'well_id': 'P6', 'state': 'empty', 'colour': '#1e0bc8'}, 97: {'group': 0, 'well_id': 'A7', 'state': 'empty', 'colour': '#1e0bc8'}, 98: {'group': 1, 'well_id': 'B7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 4}, 99: {'group': 1, 'well_id': 'C7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 4}, 100: {'group': 1, 'well_id': 'D7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 4}, 101: {'group': 2, 'well_id': 'E7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 4}, 102: {'group': 2, 'well_id': 'F7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 4}, 103: {'group': 2, 'well_id': 'G7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 4}, 104: {'group': 3, 'well_id': 'H7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 4}, 105: {'group': 3, 'well_id': 'I7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 4}, 106: {'group': 3, 'well_id': 'J7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 4}, 107: {'group': 4, 'well_id': 'K7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 4}, 108: {'group': 4, 'well_id': 'L7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 4}, 109: {'group': 4, 'well_id': 'M7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 4}, 110: {'group': 0, 'well_id': 'N7', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 111: {'group': 0, 'well_id': 'O7', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 112: {'group': 0, 'well_id': 'P7', 'state': 'empty', 'colour': '#1e0bc8'}, 113: {'group': 0, 'well_id': 'A8', 'state': 'empty', 'colour': '#1e0bc8'}, 114: {'group': 1, 'well_id': 'B8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 5}, 115: {'group': 1, 'well_id': 'C8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 5}, 116: {'group': 1, 'well_id': 'D8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 5}, 117: {'group': 2, 'well_id': 'E8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 5}, 118: {'group': 2, 'well_id': 'F8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 5}, 119: {'group': 2, 'well_id': 'G8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 5}, 120: {'group': 3, 'well_id': 'H8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 5}, 121: {'group': 3, 'well_id': 'I8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 5}, 122: {'group': 3, 'well_id': 'J8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 5}, 123: {'group': 4, 'well_id': 'K8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 5}, 124: {'group': 4, 'well_id': 'L8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 5}, 125: {'group': 4, 'well_id': 'M8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 5}, 126: {'group': 0, 'well_id': 'N8', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 127: {'group': 0, 'well_id': 'O8', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 128: {'group': 0, 'well_id': 'P8', 'state': 'empty', 'colour': '#1e0bc8'}, 129: {'group': 0, 'well_id': 'A9', 'state': 'empty', 'colour': '#1e0bc8'}, 130: {'group': 1, 'well_id': 'B9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 6}, 131: {'group': 1, 'well_id': 'C9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 6}, 132: {'group': 1, 'well_id': 'D9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 6}, 133: {'group': 2, 'well_id': 'E9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 6}, 134: {'group': 2, 'well_id': 'F9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 6}, 135: {'group': 2, 'well_id': 'G9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 6}, 136: {'group': 3, 'well_id': 'H9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 6}, 137: {'group': 3, 'well_id': 'I9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 6}, 138: {'group': 3, 'well_id': 'J9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 6}, 139: {'group': 4, 'well_id': 'K9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 6}, 140: {'group': 4, 'well_id': 'L9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 6}, 141: {'group': 4, 'well_id': 'M9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 6}, 142: {'group': 0, 'well_id': 'N9', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 143: {'group': 0, 'well_id': 'O9', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 144: {'group': 0, 'well_id': 'P9', 'state': 'empty', 'colour': '#1e0bc8'}, 145: {'group': 0, 'well_id': 'A10', 'state': 'empty', 'colour': '#1e0bc8'}, 146: {'group': 1, 'well_id': 'B10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 7}, 147: {'group': 1, 'well_id': 'C10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 7}, 148: {'group': 1, 'well_id': 'D10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 7}, 149: {'group': 2, 'well_id': 'E10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 7}, 150: {'group': 2, 'well_id': 'F10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 7}, 151: {'group': 2, 'well_id': 'G10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 7}, 152: {'group': 3, 'well_id': 'H10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 7}, 153: {'group': 3, 'well_id': 'I10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 7}, 154: {'group': 3, 'well_id': 'J10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 7}, 155: {'group': 4, 'well_id': 'K10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 7}, 156: {'group': 4, 'well_id': 'L10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 7}, 157: {'group': 4, 'well_id': 'M10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 7}, 158: {'group': 0, 'well_id': 'N10', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 159: {'group': 0, 'well_id': 'O10', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 160: {'group': 0, 'well_id': 'P10', 'state': 'empty', 'colour': '#1e0bc8'}, 161: {'group': 0, 'well_id': 'A11', 'state': 'empty', 'colour': '#1e0bc8'}, 162: {'group': 1, 'well_id': 'B11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 8}, 163: {'group': 1, 'well_id': 'C11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 8}, 164: {'group': 1, 'well_id': 'D11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 8}, 165: {'group': 2, 'well_id': 'E11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 8}, 166: {'group': 2, 'well_id': 'F11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 8}, 167: {'group': 2, 'well_id': 'G11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 8}, 168: {'group': 3, 'well_id': 'H11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 8}, 169: {'group': 3, 'well_id': 'I11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 8}, 170: {'group': 3, 'well_id': 'J11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 8}, 171: {'group': 4, 'well_id': 'K11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 8}, 172: {'group': 4, 'well_id': 'L11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 8}, 173: {'group': 4, 'well_id': 'M11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 8}, 174: {'group': 0, 'well_id': 'N11', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 175: {'group': 0, 'well_id': 'O11', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 176: {'group': 0, 'well_id': 'P11', 'state': 'empty', 'colour': '#1e0bc8'}, 177: {'group': 0, 'well_id': 'A12', 'state': 'empty', 'colour': '#1e0bc8'}, 178: {'group': 1, 'well_id': 'B12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 9}, 179: {'group': 1, 'well_id': 'C12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 9}, 180: {'group': 1, 'well_id': 'D12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 9}, 181: {'group': 2, 'well_id': 'E12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 9}, 182: {'group': 2, 'well_id': 'F12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 9}, 183: {'group': 2, 'well_id': 'G12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 9}, 184: {'group': 3, 'well_id': 'H12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 9}, 185: {'group': 3, 'well_id': 'I12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 9}, 186: {'group': 3, 'well_id': 'J12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 9}, 187: {'group': 4, 'well_id': 'K12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 9}, 188: {'group': 4, 'well_id': 'L12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 9}, 189: {'group': 4, 'well_id': 'M12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 9}, 190: {'group': 0, 'well_id': 'N12', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 191: {'group': 0, 'well_id': 'O12', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 192: {'group': 0, 'well_id': 'P12', 'state': 'empty', 'colour': '#1e0bc8'}, 193: {'group': 0, 'well_id': 'A13', 'state': 'empty', 'colour': '#1e0bc8'}, 194: {'group': 1, 'well_id': 'B13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 10}, 195: {'group': 1, 'well_id': 'C13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 10}, 196: {'group': 1, 'well_id': 'D13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 10}, 197: {'group': 2, 'well_id': 'E13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 10}, 198: {'group': 2, 'well_id': 'F13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 10}, 199: {'group': 2, 'well_id': 'G13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 10}, 200: {'group': 3, 'well_id': 'H13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 10}, 201: {'group': 3, 'well_id': 'I13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 10}, 202: {'group': 3, 'well_id': 'J13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 10}, 203: {'group': 4, 'well_id': 'K13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 10}, 204: {'group': 4, 'well_id': 'L13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 10}, 205: {'group': 4, 'well_id': 'M13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 10}, 206: {'group': 0, 'well_id': 'N13', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 207: {'group': 0, 'well_id': 'O13', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 208: {'group': 0, 'well_id': 'P13', 'state': 'empty', 'colour': '#1e0bc8'}, 209: {'group': 0, 'well_id': 'A14', 'state': 'empty', 'colour': '#1e0bc8'}, 210: {'group': 5, 'well_id': 'B14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 1}, 211: {'group': 5, 'well_id': 'C14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 1}, 212: {'group': 5, 'well_id': 'D14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 1}, 213: {'group': 6, 'well_id': 'E14', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 1}, 214: {'group': 6, 'well_id': 'F14', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 1}, 215: {'group': 6, 'well_id': 'G14', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 1}, 216: {'group': 7, 'well_id': 'H14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 1}, 217: {'group': 7, 'well_id': 'I14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 1}, 218: {'group': 7, 'well_id': 'J14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 1}, 219: {'group': 8, 'well_id': 'K14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 1}, 220: {'group': 8, 'well_id': 'L14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 1}, 221: {'group': 8, 'well_id': 'M14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 1}, 222: {'group': 0, 'well_id': 'N14', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 223: {'group': 0, 'well_id': 'O14', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 224: {'group': 0, 'well_id': 'P14', 'state': 'empty', 'colour': '#1e0bc8'}, 225: {'group': 0, 'well_id': 'A15', 'state': 'empty', 'colour': '#1e0bc8'}, 226: {'group': 5, 'well_id': 'B15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 2}, 227: {'group': 5, 'well_id': 'C15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 2}, 228: {'group': 5, 'well_id': 'D15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 2}, 229: {'group': 6, 'well_id': 'E15', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 2}, 230: {'group': 6, 'well_id': 'F15', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 2}, 231: {'group': 6, 'well_id': 'G15', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 2}, 232: {'group': 7, 'well_id': 'H15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 2}, 233: {'group': 7, 'well_id': 'I15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 2}, 234: {'group': 7, 'well_id': 'J15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 2}, 235: {'group': 8, 'well_id': 'K15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 2}, 236: {'group': 8, 'well_id': 'L15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 2}, 237: {'group': 8, 'well_id': 'M15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 2}, 238: {'group': 0, 'well_id': 'N15', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 239: {'group': 0, 'well_id': 'O15', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 240: {'group': 0, 'well_id': 'P15', 'state': 'empty', 'colour': '#1e0bc8'}, 241: {'group': 0, 'well_id': 'A16', 'state': 'empty', 'colour': '#1e0bc8'}, 242: {'group': 5, 'well_id': 'B16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 3}, 243: {'group': 5, 'well_id': 'C16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 3}, 244: {'group': 5, 'well_id': 'D16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 3}, 245: {'group': 6, 'well_id': 'E16', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 3}, 246: {'group': 6, 'well_id': 'F16', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 3}, 247: {'group': 6, 'well_id': 'G16', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 3}, 248: {'group': 7, 'well_id': 'H16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 3}, 249: {'group': 7, 'well_id': 'I16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 3}, 250: {'group': 7, 'well_id': 'J16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 3}, 251: {'group': 8, 'well_id': 'K16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 3}, 252: {'group': 8, 'well_id': 'L16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 3}, 253: {'group': 8, 'well_id': 'M16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 3}, 254: {'group': 0, 'well_id': 'N16', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 255: {'group': 0, 'well_id': 'O16', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 256: {'group': 0, 'well_id': 'P16', 'state': 'empty', 'colour': '#1e0bc8'}, 257: {'group': 0, 'well_id': 'A17', 'state': 'empty', 'colour': '#1e0bc8'}, 258: {'group': 5, 'well_id': 'B17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 4}, 259: {'group': 5, 'well_id': 'C17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 4}, 260: {'group': 5, 'well_id': 'D17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 4}, 261: {'group': 6, 'well_id': 'E17', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 4}, 262: {'group': 6, 'well_id': 'F17', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 4}, 263: {'group': 6, 'well_id': 'G17', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 4}, 264: {'group': 7, 'well_id': 'H17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 4}, 265: {'group': 7, 'well_id': 'I17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 4}, 266: {'group': 7, 'well_id': 'J17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 4}, 267: {'group': 8, 'well_id': 'K17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 4}, 268: {'group': 8, 'well_id': 'L17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 4}, 269: {'group': 8, 'well_id': 'M17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 4}, 270: {'group': 0, 'well_id': 'N17', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 271: {'group': 0, 'well_id': 'O17', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 272: {'group': 0, 'well_id': 'P17', 'state': 'empty', 'colour': '#1e0bc8'}, 273: {'group': 0, 'well_id': 'A18', 'state': 'empty', 'colour': '#1e0bc8'}, 274: {'group': 5, 'well_id': 'B18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 5}, 275: {'group': 5, 'well_id': 'C18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 5}, 276: {'group': 5, 'well_id': 'D18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 5}, 277: {'group': 6, 'well_id': 'E18', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 5}, 278: {'group': 6, 'well_id': 'F18', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 5}, 279: {'group': 6, 'well_id': 'G18', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 5}, 280: {'group': 7, 'well_id': 'H18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 5}, 281: {'group': 7, 'well_id': 'I18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 5}, 282: {'group': 7, 'well_id': 'J18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 5}, 283: {'group': 8, 'well_id': 'K18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 5}, 284: {'group': 8, 'well_id': 'L18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 5}, 285: {'group': 8, 'well_id': 'M18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 5}, 286: {'group': 0, 'well_id': 'N18', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 287: {'group': 0, 'well_id': 'O18', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 288: {'group': 0, 'well_id': 'P18', 'state': 'empty', 'colour': '#1e0bc8'}, 289: {'group': 0, 'well_id': 'A19', 'state': 'empty', 'colour': '#1e0bc8'}, 290: {'group': 5, 'well_id': 'B19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 6}, 291: {'group': 5, 'well_id': 'C19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 6}, 292: {'group': 5, 'well_id': 'D19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 6}, 293: {'group': 6, 'well_id': 'E19', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 6}, 294: {'group': 6, 'well_id': 'F19', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 6}, 295: {'group': 6, 'well_id': 'G19', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 6}, 296: {'group': 7, 'well_id': 'H19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 6}, 297: {'group': 7, 'well_id': 'I19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 6}, 298: {'group': 7, 'well_id': 'J19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 6}, 299: {'group': 8, 'well_id': 'K19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 6}, 300: {'group': 8, 'well_id': 'L19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 6}, 301: {'group': 8, 'well_id': 'M19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 6}, 302: {'group': 0, 'well_id': 'N19', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 303: {'group': 0, 'well_id': 'O19', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 304: {'group': 0, 'well_id': 'P19', 'state': 'empty', 'colour': '#1e0bc8'}, 305: {'group': 0, 'well_id': 'A20', 'state': 'empty', 'colour': '#1e0bc8'}, 306: {'group': 5, 'well_id': 'B20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 7}, 307: {'group': 5, 'well_id': 'C20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 7}, 308: {'group': 5, 'well_id': 'D20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 7}, 309: {'group': 6, 'well_id': 'E20', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 7}, 310: {'group': 6, 'well_id': 'F20', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 7}, 311: {'group': 6, 'well_id': 'G20', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 7}, 312: {'group': 7, 'well_id': 'H20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 7}, 313: {'group': 7, 'well_id': 'I20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 7}, 314: {'group': 7, 'well_id': 'J20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 7}, 315: {'group': 8, 'well_id': 'K20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 7}, 316: {'group': 8, 'well_id': 'L20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 7}, 317: {'group': 8, 'well_id': 'M20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 7}, 318: {'group': 0, 'well_id': 'N20', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 319: {'group': 0, 'well_id': 'O20', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 320: {'group': 0, 'well_id': 'P20', 'state': 'empty', 'colour': '#1e0bc8'}, 321: {'group': 0, 'well_id': 'A21', 'state': 'empty', 'colour': '#1e0bc8'}, 322: {'group': 5, 'well_id': 'B21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 8}, 323: {'group': 5, 'well_id': 'C21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 8}, 324: {'group': 5, 'well_id': 'D21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 8}, 325: {'group': 6, 'well_id': 'E21', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 8}, 326: {'group': 6, 'well_id': 'F21', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 8}, 327: {'group': 6, 'well_id': 'G21', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 8}, 328: {'group': 7, 'well_id': 'H21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 8}, 329: {'group': 7, 'well_id': 'I21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 8}, 330: {'group': 7, 'well_id': 'J21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 8}, 331: {'group': 8, 'well_id': 'K21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 8}, 332: {'group': 8, 'well_id': 'L21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 8}, 333: {'group': 8, 'well_id': 'M21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 8}, 334: {'group': 0, 'well_id': 'N21', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 335: {'group': 0, 'well_id': 'O21', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 336: {'group': 0, 'well_id': 'P21', 'state': 'empty', 'colour': '#1e0bc8'}, 337: {'group': 0, 'well_id': 'A22', 'state': 'empty', 'colour': '#1e0bc8'}, 338: {'group': 5, 'well_id': 'B22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 9}, 339: {'group': 5, 'well_id': 'C22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 9}, 340: {'group': 5, 'well_id': 'D22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 9}, 341: {'group': 6, 'well_id': 'E22', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 9}, 342: {'group': 6, 'well_id': 'F22', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 9}, 343: {'group': 6, 'well_id': 'G22', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 9}, 344: {'group': 7, 'well_id': 'H22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 9}, 345: {'group': 7, 'well_id': 'I22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 9}, 346: {'group': 7, 'well_id': 'J22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 9}, 347: {'group': 8, 'well_id': 'K22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 9}, 348: {'group': 8, 'well_id': 'L22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 9}, 349: {'group': 8, 'well_id': 'M22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 9}, 350: {'group': 0, 'well_id': 'N22', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 351: {'group': 0, 'well_id': 'O22', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 352: {'group': 0, 'well_id': 'P22', 'state': 'empty', 'colour': '#1e0bc8'}, 353: {'group': 0, 'well_id': 'A23', 'state': 'empty', 'colour': '#1e0bc8'}, 354: {'group': 5, 'well_id': 'B23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 10}, 355: {'group': 5, 'well_id': 'C23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 10}, 356: {'group': 5, 'well_id': 'D23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 10}, 357: {'group': 6, 'well_id': 'E23', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 10}, 358: {'group': 6, 'well_id': 'F23', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 10}, 359: {'group': 6, 'well_id': 'G23', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 10}, 360: {'group': 7, 'well_id': 'H23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 10}, 361: {'group': 7, 'well_id': 'I23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 10}, 362: {'group': 7, 'well_id': 'J23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 10}, 363: {'group': 8, 'well_id': 'K23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 10}, 364: {'group': 8, 'well_id': 'L23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 10}, 365: {'group': 8, 'well_id': 'M23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 10}, 366: {'group': 0, 'well_id': 'N23', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 367: {'group': 0, 'well_id': 'O23', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0}, 368: {'group': 0, 'well_id': 'P23', 'state': 'empty', 'colour': '#1e0bc8'}, 369: {'group': 0, 'well_id': 'A24', 'state': 'empty', 'colour': '#1e0bc8'}, 370: {'group': 0, 'well_id': 'B24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 371: {'group': 0, 'well_id': 'C24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 372: {'group': 0, 'well_id': 'D24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 373: {'group': 0, 'well_id': 'E24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 374: {'group': 0, 'well_id': 'F24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 375: {'group': 0, 'well_id': 'G24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 376: {'group': 0, 'well_id': 'H24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 377: {'group': 0, 'well_id': 'I24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 378: {'group': 0, 'well_id': 'J24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 379: {'group': 0, 'well_id': 'K24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 380: {'group': 0, 'well_id': 'L24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 381: {'group': 0, 'well_id': 'M24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 382: {'group': 0, 'well_id': 'N24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 383: {'group': 0, 'well_id': 'O24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0}, 384: {'group': 0, 'well_id': 'P24', 'state': 'empty', 'colour': '#1e0bc8'}}
    for wells in well_dict:
        if well_dict[wells]["state"] == "sample" and well_dict[wells]["group"] == 0:
            well_dict[wells]["state"] = "empty"

    stock = "10mM"
    max_concentration = "90uM"
    min_concentration = "4nM"
    echo_min = "2.5nL"
    final_vol = "12uL"
    # Test the function
    dilution_steps = 10
    dilution_factor = 3
    stock_dilution = 100
    max_solvent_concentration = 1
    vol_needed_pure = calculate_dilution_series(stock, max_concentration, min_concentration, dilution_steps,
                                                dilution_factor, echo_min, final_vol, stock_dilution, max_solvent_concentration)
    print(vol_needed_pure)
    # # #ToDo Make a popup to choose source_layout for dose_reponse_worklist_writer and make it possible to import from excel & CSV instead
    # plate_amount = 8
    # initial_plate = 313
    # assay_name = "alpha_so"
    # volume = "120nL"
    # fill_up = "120nl"
    # sample_per_plate = 8
    # csv_writer = CSVWriter()
    # csv_writer.dose_response_worklist_writer(config, well_dict, source_layout, plate_amount, vol_needed_pure, initial_plate,
    #                               assay_name, volume, sample_per_plate, fill_up)
    # testing(well_dict, vol_needed_pure)

    {1: {'group': 0, 'well_id': 'A1', 'state': 'empty', 'colour': '#1e0bc8'},
     2: {'group': 0, 'well_id': 'B1', 'state': 'empty', 'colour': '#1e0bc8'},
     3: {'group': 0, 'well_id': 'C1', 'state': 'empty', 'colour': '#1e0bc8'},
     4: {'group': 0, 'well_id': 'D1', 'state': 'empty', 'colour': '#1e0bc8'},
     5: {'group': 0, 'well_id': 'E1', 'state': 'empty', 'colour': '#1e0bc8'},
     6: {'group': 0, 'well_id': 'F1', 'state': 'empty', 'colour': '#1e0bc8'},
     7: {'group': 0, 'well_id': 'G1', 'state': 'empty', 'colour': '#1e0bc8'},
     8: {'group': 0, 'well_id': 'H1', 'state': 'empty', 'colour': '#1e0bc8'},
     9: {'group': 0, 'well_id': 'I1', 'state': 'empty', 'colour': '#1e0bc8'},
     10: {'group': 0, 'well_id': 'J1', 'state': 'empty', 'colour': '#1e0bc8'},
     11: {'group': 0, 'well_id': 'K1', 'state': 'empty', 'colour': '#1e0bc8'},
     12: {'group': 0, 'well_id': 'L1', 'state': 'empty', 'colour': '#1e0bc8'},
     13: {'group': 0, 'well_id': 'M1', 'state': 'empty', 'colour': '#1e0bc8'},
     14: {'group': 0, 'well_id': 'N1', 'state': 'empty', 'colour': '#1e0bc8'},
     15: {'group': 0, 'well_id': 'O1', 'state': 'empty', 'colour': '#1e0bc8'},
     16: {'group': 0, 'well_id': 'P1', 'state': 'empty', 'colour': '#1e0bc8'},
     17: {'group': 0, 'well_id': 'A2', 'state': 'empty', 'colour': '#1e0bc8'},
     18: {'group': 0, 'well_id': 'B2', 'state': 'minimum', 'colour': '#ff8000'},
     19: {'group': 0, 'well_id': 'C2', 'state': 'minimum', 'colour': '#ff8000'},
     20: {'group': 0, 'well_id': 'D2', 'state': 'minimum', 'colour': '#ff8000'},
     21: {'group': 0, 'well_id': 'E2', 'state': 'minimum', 'colour': '#ff8000'},
     22: {'group': 0, 'well_id': 'F2', 'state': 'minimum', 'colour': '#ff8000'},
     23: {'group': 0, 'well_id': 'G2', 'state': 'minimum', 'colour': '#ff8000'},
     24: {'group': 0, 'well_id': 'H2', 'state': 'minimum', 'colour': '#ff8000'},
     25: {'group': 0, 'well_id': 'I2', 'state': 'minimum', 'colour': '#ff8000'},
     26: {'group': 0, 'well_id': 'J2', 'state': 'minimum', 'colour': '#ff8000'},
     27: {'group': 0, 'well_id': 'K2', 'state': 'minimum', 'colour': '#ff8000'},
     28: {'group': 0, 'well_id': 'L2', 'state': 'minimum', 'colour': '#ff8000'},
     29: {'group': 0, 'well_id': 'M2', 'state': 'minimum', 'colour': '#ff8000'},
     30: {'group': 0, 'well_id': 'N2', 'state': 'minimum', 'colour': '#ff8000'},
     31: {'group': 0, 'well_id': 'O2', 'state': 'minimum', 'colour': '#ff8000'},
     32: {'group': 0, 'well_id': 'P2', 'state': 'empty', 'colour': '#1e0bc8'},
     33: {'group': 0, 'well_id': 'A3', 'state': 'empty', 'colour': '#1e0bc8'},
     34: {'group': 0, 'well_id': 'B3', 'state': 'max', 'colour': '#790dc1'},
     35: {'group': 0, 'well_id': 'C3', 'state': 'max', 'colour': '#790dc1'},
     36: {'group': 0, 'well_id': 'D3', 'state': 'max', 'colour': '#790dc1'},
     37: {'group': 0, 'well_id': 'E3', 'state': 'max', 'colour': '#790dc1'},
     38: {'group': 0, 'well_id': 'F3', 'state': 'max', 'colour': '#790dc1'},
     39: {'group': 0, 'well_id': 'G3', 'state': 'max', 'colour': '#790dc1'},
     40: {'group': 0, 'well_id': 'H3', 'state': 'max', 'colour': '#790dc1'},
     41: {'group': 0, 'well_id': 'I3', 'state': 'max', 'colour': '#790dc1'},
     42: {'group': 0, 'well_id': 'J3', 'state': 'max', 'colour': '#790dc1'},
     43: {'group': 0, 'well_id': 'K3', 'state': 'max', 'colour': '#790dc1'},
     44: {'group': 0, 'well_id': 'L3', 'state': 'max', 'colour': '#790dc1'},
     45: {'group': 0, 'well_id': 'M3', 'state': 'max', 'colour': '#790dc1'},
     46: {'group': 0, 'well_id': 'N3', 'state': 'max', 'colour': '#790dc1'},
     47: {'group': 0, 'well_id': 'O3', 'state': 'max', 'colour': '#790dc1'},
     48: {'group': 0, 'well_id': 'P3', 'state': 'empty', 'colour': '#1e0bc8'},
     49: {'group': 0, 'well_id': 'A4', 'state': 'empty', 'colour': '#1e0bc8'},
     50: {'group': 1, 'well_id': 'B4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 1},
     51: {'group': 1, 'well_id': 'C4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 1},
     52: {'group': 1, 'well_id': 'D4', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 1},
     53: {'group': 2, 'well_id': 'E4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 1},
     54: {'group': 2, 'well_id': 'F4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 1},
     55: {'group': 2, 'well_id': 'G4', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 1},
     56: {'group': 3, 'well_id': 'H4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 1},
     57: {'group': 3, 'well_id': 'I4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 1},
     58: {'group': 3, 'well_id': 'J4', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 1},
     59: {'group': 4, 'well_id': 'K4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 1},
     60: {'group': 4, 'well_id': 'L4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 1},
     61: {'group': 4, 'well_id': 'M4', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 1},
     62: {'group': 0, 'well_id': 'N4', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     63: {'group': 0, 'well_id': 'O4', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     64: {'group': 0, 'well_id': 'P4', 'state': 'empty', 'colour': '#1e0bc8'},
     65: {'group': 0, 'well_id': 'A5', 'state': 'empty', 'colour': '#1e0bc8'},
     66: {'group': 1, 'well_id': 'B5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 2},
     67: {'group': 1, 'well_id': 'C5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 2},
     68: {'group': 1, 'well_id': 'D5', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 2},
     69: {'group': 2, 'well_id': 'E5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 2},
     70: {'group': 2, 'well_id': 'F5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 2},
     71: {'group': 2, 'well_id': 'G5', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 2},
     72: {'group': 3, 'well_id': 'H5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 2},
     73: {'group': 3, 'well_id': 'I5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 2},
     74: {'group': 3, 'well_id': 'J5', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 2},
     75: {'group': 4, 'well_id': 'K5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 2},
     76: {'group': 4, 'well_id': 'L5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 2},
     77: {'group': 4, 'well_id': 'M5', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 2},
     78: {'group': 0, 'well_id': 'N5', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     79: {'group': 0, 'well_id': 'O5', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     80: {'group': 0, 'well_id': 'P5', 'state': 'empty', 'colour': '#1e0bc8'},
     81: {'group': 0, 'well_id': 'A6', 'state': 'empty', 'colour': '#1e0bc8'},
     82: {'group': 1, 'well_id': 'B6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 3},
     83: {'group': 1, 'well_id': 'C6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 3},
     84: {'group': 1, 'well_id': 'D6', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 3},
     85: {'group': 2, 'well_id': 'E6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 3},
     86: {'group': 2, 'well_id': 'F6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 3},
     87: {'group': 2, 'well_id': 'G6', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 3},
     88: {'group': 3, 'well_id': 'H6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 3},
     89: {'group': 3, 'well_id': 'I6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 3},
     90: {'group': 3, 'well_id': 'J6', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 3},
     91: {'group': 4, 'well_id': 'K6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 3},
     92: {'group': 4, 'well_id': 'L6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 3},
     93: {'group': 4, 'well_id': 'M6', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 3},
     94: {'group': 0, 'well_id': 'N6', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     95: {'group': 0, 'well_id': 'O6', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     96: {'group': 0, 'well_id': 'P6', 'state': 'empty', 'colour': '#1e0bc8'},
     97: {'group': 0, 'well_id': 'A7', 'state': 'empty', 'colour': '#1e0bc8'},
     98: {'group': 1, 'well_id': 'B7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 4},
     99: {'group': 1, 'well_id': 'C7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 4},
     100: {'group': 1, 'well_id': 'D7', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 4},
     101: {'group': 2, 'well_id': 'E7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 4},
     102: {'group': 2, 'well_id': 'F7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 4},
     103: {'group': 2, 'well_id': 'G7', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 4},
     104: {'group': 3, 'well_id': 'H7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 4},
     105: {'group': 3, 'well_id': 'I7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 4},
     106: {'group': 3, 'well_id': 'J7', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 4},
     107: {'group': 4, 'well_id': 'K7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 4},
     108: {'group': 4, 'well_id': 'L7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 4},
     109: {'group': 4, 'well_id': 'M7', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 4},
     110: {'group': 0, 'well_id': 'N7', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     111: {'group': 0, 'well_id': 'O7', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     112: {'group': 0, 'well_id': 'P7', 'state': 'empty', 'colour': '#1e0bc8'},
     113: {'group': 0, 'well_id': 'A8', 'state': 'empty', 'colour': '#1e0bc8'},
     114: {'group': 1, 'well_id': 'B8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 5},
     115: {'group': 1, 'well_id': 'C8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 5},
     116: {'group': 1, 'well_id': 'D8', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 5},
     117: {'group': 2, 'well_id': 'E8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 5},
     118: {'group': 2, 'well_id': 'F8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 5},
     119: {'group': 2, 'well_id': 'G8', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 5},
     120: {'group': 3, 'well_id': 'H8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 5},
     121: {'group': 3, 'well_id': 'I8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 5},
     122: {'group': 3, 'well_id': 'J8', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 5},
     123: {'group': 4, 'well_id': 'K8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 5},
     124: {'group': 4, 'well_id': 'L8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 5},
     125: {'group': 4, 'well_id': 'M8', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 5},
     126: {'group': 0, 'well_id': 'N8', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     127: {'group': 0, 'well_id': 'O8', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     128: {'group': 0, 'well_id': 'P8', 'state': 'empty', 'colour': '#1e0bc8'},
     129: {'group': 0, 'well_id': 'A9', 'state': 'empty', 'colour': '#1e0bc8'},
     130: {'group': 1, 'well_id': 'B9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 6},
     131: {'group': 1, 'well_id': 'C9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 6},
     132: {'group': 1, 'well_id': 'D9', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 6},
     133: {'group': 2, 'well_id': 'E9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 6},
     134: {'group': 2, 'well_id': 'F9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 6},
     135: {'group': 2, 'well_id': 'G9', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 6},
     136: {'group': 3, 'well_id': 'H9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 6},
     137: {'group': 3, 'well_id': 'I9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 6},
     138: {'group': 3, 'well_id': 'J9', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 6},
     139: {'group': 4, 'well_id': 'K9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 6},
     140: {'group': 4, 'well_id': 'L9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 6},
     141: {'group': 4, 'well_id': 'M9', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 6},
     142: {'group': 0, 'well_id': 'N9', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     143: {'group': 0, 'well_id': 'O9', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     144: {'group': 0, 'well_id': 'P9', 'state': 'empty', 'colour': '#1e0bc8'},
     145: {'group': 0, 'well_id': 'A10', 'state': 'empty', 'colour': '#1e0bc8'},
     146: {'group': 1, 'well_id': 'B10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 7},
     147: {'group': 1, 'well_id': 'C10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 7},
     148: {'group': 1, 'well_id': 'D10', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 7},
     149: {'group': 2, 'well_id': 'E10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 7},
     150: {'group': 2, 'well_id': 'F10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 7},
     151: {'group': 2, 'well_id': 'G10', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 7},
     152: {'group': 3, 'well_id': 'H10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 7},
     153: {'group': 3, 'well_id': 'I10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 7},
     154: {'group': 3, 'well_id': 'J10', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 7},
     155: {'group': 4, 'well_id': 'K10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 7},
     156: {'group': 4, 'well_id': 'L10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 7},
     157: {'group': 4, 'well_id': 'M10', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 7},
     158: {'group': 0, 'well_id': 'N10', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     159: {'group': 0, 'well_id': 'O10', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     160: {'group': 0, 'well_id': 'P10', 'state': 'empty', 'colour': '#1e0bc8'},
     161: {'group': 0, 'well_id': 'A11', 'state': 'empty', 'colour': '#1e0bc8'},
     162: {'group': 1, 'well_id': 'B11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 8},
     163: {'group': 1, 'well_id': 'C11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 8},
     164: {'group': 1, 'well_id': 'D11', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 8},
     165: {'group': 2, 'well_id': 'E11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 8},
     166: {'group': 2, 'well_id': 'F11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 8},
     167: {'group': 2, 'well_id': 'G11', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 8},
     168: {'group': 3, 'well_id': 'H11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 8},
     169: {'group': 3, 'well_id': 'I11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 8},
     170: {'group': 3, 'well_id': 'J11', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 8},
     171: {'group': 4, 'well_id': 'K11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 8},
     172: {'group': 4, 'well_id': 'L11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 8},
     173: {'group': 4, 'well_id': 'M11', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 8},
     174: {'group': 0, 'well_id': 'N11', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     175: {'group': 0, 'well_id': 'O11', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     176: {'group': 0, 'well_id': 'P11', 'state': 'empty', 'colour': '#1e0bc8'},
     177: {'group': 0, 'well_id': 'A12', 'state': 'empty', 'colour': '#1e0bc8'},
     178: {'group': 1, 'well_id': 'B12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 9},
     179: {'group': 1, 'well_id': 'C12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 9},
     180: {'group': 1, 'well_id': 'D12', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 9},
     181: {'group': 2, 'well_id': 'E12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 9},
     182: {'group': 2, 'well_id': 'F12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 9},
     183: {'group': 2, 'well_id': 'G12', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 9},
     184: {'group': 3, 'well_id': 'H12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 9},
     185: {'group': 3, 'well_id': 'I12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 9},
     186: {'group': 3, 'well_id': 'J12', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 9},
     187: {'group': 4, 'well_id': 'K12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 9},
     188: {'group': 4, 'well_id': 'L12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 9},
     189: {'group': 4, 'well_id': 'M12', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 9},
     190: {'group': 0, 'well_id': 'N12', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     191: {'group': 0, 'well_id': 'O12', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     192: {'group': 0, 'well_id': 'P12', 'state': 'empty', 'colour': '#1e0bc8'},
     193: {'group': 0, 'well_id': 'A13', 'state': 'empty', 'colour': '#1e0bc8'},
     194: {'group': 1, 'well_id': 'B13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 1, 'concentration': 10},
     195: {'group': 1, 'well_id': 'C13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 2, 'concentration': 10},
     196: {'group': 1, 'well_id': 'D13', 'state': 'sample', 'colour': '#11B4D4', 'replicate': 3, 'concentration': 10},
     197: {'group': 2, 'well_id': 'E13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 1, 'concentration': 10},
     198: {'group': 2, 'well_id': 'F13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 2, 'concentration': 10},
     199: {'group': 2, 'well_id': 'G13', 'state': 'sample', 'colour': '#d84b29', 'replicate': 3, 'concentration': 10},
     200: {'group': 3, 'well_id': 'H13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 1, 'concentration': 10},
     201: {'group': 3, 'well_id': 'I13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 2, 'concentration': 10},
     202: {'group': 3, 'well_id': 'J13', 'state': 'sample', 'colour': '#3CB4D8', 'replicate': 3, 'concentration': 10},
     203: {'group': 4, 'well_id': 'K13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 1, 'concentration': 10},
     204: {'group': 4, 'well_id': 'L13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 2, 'concentration': 10},
     205: {'group': 4, 'well_id': 'M13', 'state': 'sample', 'colour': '#ae4b25', 'replicate': 3, 'concentration': 10},
     206: {'group': 0, 'well_id': 'N13', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     207: {'group': 0, 'well_id': 'O13', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     208: {'group': 0, 'well_id': 'P13', 'state': 'empty', 'colour': '#1e0bc8'},
     209: {'group': 0, 'well_id': 'A14', 'state': 'empty', 'colour': '#1e0bc8'},
     210: {'group': 5, 'well_id': 'B14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 1},
     211: {'group': 5, 'well_id': 'C14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 1},
     212: {'group': 5, 'well_id': 'D14', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 1},
     213: {'group': 6, 'well_id': 'E14', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 1},
     214: {'group': 6, 'well_id': 'F14', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 1},
     215: {'group': 6, 'well_id': 'G14', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 1},
     216: {'group': 7, 'well_id': 'H14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 1},
     217: {'group': 7, 'well_id': 'I14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 1},
     218: {'group': 7, 'well_id': 'J14', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 1},
     219: {'group': 8, 'well_id': 'K14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 1},
     220: {'group': 8, 'well_id': 'L14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 1},
     221: {'group': 8, 'well_id': 'M14', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 1},
     222: {'group': 0, 'well_id': 'N14', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     223: {'group': 0, 'well_id': 'O14', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     224: {'group': 0, 'well_id': 'P14', 'state': 'empty', 'colour': '#1e0bc8'},
     225: {'group': 0, 'well_id': 'A15', 'state': 'empty', 'colour': '#1e0bc8'},
     226: {'group': 5, 'well_id': 'B15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 2},
     227: {'group': 5, 'well_id': 'C15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 2},
     228: {'group': 5, 'well_id': 'D15', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 2},
     229: {'group': 6, 'well_id': 'E15', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 2},
     230: {'group': 6, 'well_id': 'F15', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 2},
     231: {'group': 6, 'well_id': 'G15', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 2},
     232: {'group': 7, 'well_id': 'H15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 2},
     233: {'group': 7, 'well_id': 'I15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 2},
     234: {'group': 7, 'well_id': 'J15', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 2},
     235: {'group': 8, 'well_id': 'K15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 2},
     236: {'group': 8, 'well_id': 'L15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 2},
     237: {'group': 8, 'well_id': 'M15', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 2},
     238: {'group': 0, 'well_id': 'N15', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     239: {'group': 0, 'well_id': 'O15', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     240: {'group': 0, 'well_id': 'P15', 'state': 'empty', 'colour': '#1e0bc8'},
     241: {'group': 0, 'well_id': 'A16', 'state': 'empty', 'colour': '#1e0bc8'},
     242: {'group': 5, 'well_id': 'B16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 3},
     243: {'group': 5, 'well_id': 'C16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 3},
     244: {'group': 5, 'well_id': 'D16', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 3},
     245: {'group': 6, 'well_id': 'E16', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 3},
     246: {'group': 6, 'well_id': 'F16', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 3},
     247: {'group': 6, 'well_id': 'G16', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 3},
     248: {'group': 7, 'well_id': 'H16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 3},
     249: {'group': 7, 'well_id': 'I16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 3},
     250: {'group': 7, 'well_id': 'J16', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 3},
     251: {'group': 8, 'well_id': 'K16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 3},
     252: {'group': 8, 'well_id': 'L16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 3},
     253: {'group': 8, 'well_id': 'M16', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 3},
     254: {'group': 0, 'well_id': 'N16', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     255: {'group': 0, 'well_id': 'O16', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     256: {'group': 0, 'well_id': 'P16', 'state': 'empty', 'colour': '#1e0bc8'},
     257: {'group': 0, 'well_id': 'A17', 'state': 'empty', 'colour': '#1e0bc8'},
     258: {'group': 5, 'well_id': 'B17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 4},
     259: {'group': 5, 'well_id': 'C17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 4},
     260: {'group': 5, 'well_id': 'D17', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 4},
     261: {'group': 6, 'well_id': 'E17', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 4},
     262: {'group': 6, 'well_id': 'F17', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 4},
     263: {'group': 6, 'well_id': 'G17', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 4},
     264: {'group': 7, 'well_id': 'H17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 4},
     265: {'group': 7, 'well_id': 'I17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 4},
     266: {'group': 7, 'well_id': 'J17', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 4},
     267: {'group': 8, 'well_id': 'K17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 4},
     268: {'group': 8, 'well_id': 'L17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 4},
     269: {'group': 8, 'well_id': 'M17', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 4},
     270: {'group': 0, 'well_id': 'N17', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     271: {'group': 0, 'well_id': 'O17', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     272: {'group': 0, 'well_id': 'P17', 'state': 'empty', 'colour': '#1e0bc8'},
     273: {'group': 0, 'well_id': 'A18', 'state': 'empty', 'colour': '#1e0bc8'},
     274: {'group': 5, 'well_id': 'B18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 5},
     275: {'group': 5, 'well_id': 'C18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 5},
     276: {'group': 5, 'well_id': 'D18', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 5},
     277: {'group': 6, 'well_id': 'E18', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 5},
     278: {'group': 6, 'well_id': 'F18', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 5},
     279: {'group': 6, 'well_id': 'G18', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 5},
     280: {'group': 7, 'well_id': 'H18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 5},
     281: {'group': 7, 'well_id': 'I18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 5},
     282: {'group': 7, 'well_id': 'J18', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 5},
     283: {'group': 8, 'well_id': 'K18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 5},
     284: {'group': 8, 'well_id': 'L18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 5},
     285: {'group': 8, 'well_id': 'M18', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 5},
     286: {'group': 0, 'well_id': 'N18', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     287: {'group': 0, 'well_id': 'O18', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     288: {'group': 0, 'well_id': 'P18', 'state': 'empty', 'colour': '#1e0bc8'},
     289: {'group': 0, 'well_id': 'A19', 'state': 'empty', 'colour': '#1e0bc8'},
     290: {'group': 5, 'well_id': 'B19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 6},
     291: {'group': 5, 'well_id': 'C19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 6},
     292: {'group': 5, 'well_id': 'D19', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 6},
     293: {'group': 6, 'well_id': 'E19', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 6},
     294: {'group': 6, 'well_id': 'F19', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 6},
     295: {'group': 6, 'well_id': 'G19', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 6},
     296: {'group': 7, 'well_id': 'H19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 6},
     297: {'group': 7, 'well_id': 'I19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 6},
     298: {'group': 7, 'well_id': 'J19', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 6},
     299: {'group': 8, 'well_id': 'K19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 6},
     300: {'group': 8, 'well_id': 'L19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 6},
     301: {'group': 8, 'well_id': 'M19', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 6},
     302: {'group': 0, 'well_id': 'N19', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     303: {'group': 0, 'well_id': 'O19', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     304: {'group': 0, 'well_id': 'P19', 'state': 'empty', 'colour': '#1e0bc8'},
     305: {'group': 0, 'well_id': 'A20', 'state': 'empty', 'colour': '#1e0bc8'},
     306: {'group': 5, 'well_id': 'B20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 7},
     307: {'group': 5, 'well_id': 'C20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 7},
     308: {'group': 5, 'well_id': 'D20', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 7},
     309: {'group': 6, 'well_id': 'E20', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 7},
     310: {'group': 6, 'well_id': 'F20', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 7},
     311: {'group': 6, 'well_id': 'G20', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 7},
     312: {'group': 7, 'well_id': 'H20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 7},
     313: {'group': 7, 'well_id': 'I20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 7},
     314: {'group': 7, 'well_id': 'J20', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 7},
     315: {'group': 8, 'well_id': 'K20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 7},
     316: {'group': 8, 'well_id': 'L20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 7},
     317: {'group': 8, 'well_id': 'M20', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 7},
     318: {'group': 0, 'well_id': 'N20', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     319: {'group': 0, 'well_id': 'O20', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     320: {'group': 0, 'well_id': 'P20', 'state': 'empty', 'colour': '#1e0bc8'},
     321: {'group': 0, 'well_id': 'A21', 'state': 'empty', 'colour': '#1e0bc8'},
     322: {'group': 5, 'well_id': 'B21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 8},
     323: {'group': 5, 'well_id': 'C21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 8},
     324: {'group': 5, 'well_id': 'D21', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 8},
     325: {'group': 6, 'well_id': 'E21', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 8},
     326: {'group': 6, 'well_id': 'F21', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 8},
     327: {'group': 6, 'well_id': 'G21', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 8},
     328: {'group': 7, 'well_id': 'H21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 8},
     329: {'group': 7, 'well_id': 'I21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 8},
     330: {'group': 7, 'well_id': 'J21', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 8},
     331: {'group': 8, 'well_id': 'K21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 8},
     332: {'group': 8, 'well_id': 'L21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 8},
     333: {'group': 8, 'well_id': 'M21', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 8},
     334: {'group': 0, 'well_id': 'N21', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     335: {'group': 0, 'well_id': 'O21', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     336: {'group': 0, 'well_id': 'P21', 'state': 'empty', 'colour': '#1e0bc8'},
     337: {'group': 0, 'well_id': 'A22', 'state': 'empty', 'colour': '#1e0bc8'},
     338: {'group': 5, 'well_id': 'B22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 9},
     339: {'group': 5, 'well_id': 'C22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 9},
     340: {'group': 5, 'well_id': 'D22', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 9},
     341: {'group': 6, 'well_id': 'E22', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 9},
     342: {'group': 6, 'well_id': 'F22', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 9},
     343: {'group': 6, 'well_id': 'G22', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 9},
     344: {'group': 7, 'well_id': 'H22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 9},
     345: {'group': 7, 'well_id': 'I22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 9},
     346: {'group': 7, 'well_id': 'J22', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 9},
     347: {'group': 8, 'well_id': 'K22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 9},
     348: {'group': 8, 'well_id': 'L22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 9},
     349: {'group': 8, 'well_id': 'M22', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 9},
     350: {'group': 0, 'well_id': 'N22', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     351: {'group': 0, 'well_id': 'O22', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     352: {'group': 0, 'well_id': 'P22', 'state': 'empty', 'colour': '#1e0bc8'},
     353: {'group': 0, 'well_id': 'A23', 'state': 'empty', 'colour': '#1e0bc8'},
     354: {'group': 5, 'well_id': 'B23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 1, 'concentration': 10},
     355: {'group': 5, 'well_id': 'C23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 2, 'concentration': 10},
     356: {'group': 5, 'well_id': 'D23', 'state': 'sample', 'colour': '#66B4DC', 'replicate': 3, 'concentration': 10},
     357: {'group': 6, 'well_id': 'E23', 'state': 'sample', 'colour': '#844b21', 'replicate': 1, 'concentration': 10},
     358: {'group': 6, 'well_id': 'F23', 'state': 'sample', 'colour': '#844b21', 'replicate': 2, 'concentration': 10},
     359: {'group': 6, 'well_id': 'G23', 'state': 'sample', 'colour': '#844b21', 'replicate': 3, 'concentration': 10},
     360: {'group': 7, 'well_id': 'H23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 1, 'concentration': 10},
     361: {'group': 7, 'well_id': 'I23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 2, 'concentration': 10},
     362: {'group': 7, 'well_id': 'J23', 'state': 'sample', 'colour': '#90B4E0', 'replicate': 3, 'concentration': 10},
     363: {'group': 8, 'well_id': 'K23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 1, 'concentration': 10},
     364: {'group': 8, 'well_id': 'L23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 2, 'concentration': 10},
     365: {'group': 8, 'well_id': 'M23', 'state': 'sample', 'colour': '#5a4b1d', 'replicate': 3, 'concentration': 10},
     366: {'group': 0, 'well_id': 'N23', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     367: {'group': 0, 'well_id': 'O23', 'state': 'sample', 'colour': '#ff00ff', 'replicate': 0, 'concentration': 0},
     368: {'group': 0, 'well_id': 'P23', 'state': 'empty', 'colour': '#1e0bc8'},
     369: {'group': 0, 'well_id': 'A24', 'state': 'empty', 'colour': '#1e0bc8'},
     370: {'group': 0, 'well_id': 'B24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     371: {'group': 0, 'well_id': 'C24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     372: {'group': 0, 'well_id': 'D24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     373: {'group': 0, 'well_id': 'E24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     374: {'group': 0, 'well_id': 'F24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     375: {'group': 0, 'well_id': 'G24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     376: {'group': 0, 'well_id': 'H24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     377: {'group': 0, 'well_id': 'I24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     378: {'group': 0, 'well_id': 'J24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     379: {'group': 0, 'well_id': 'K24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     380: {'group': 0, 'well_id': 'L24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     381: {'group': 0, 'well_id': 'M24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     382: {'group': 0, 'well_id': 'N24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     383: {'group': 0, 'well_id': 'O24', 'state': 'empty', 'colour': '#1e0bc8', 'replicate': 0, 'concentration': 0},
     384: {'group': 0, 'well_id': 'P24', 'state': 'empty', 'colour': '#1e0bc8'}}
