"""Main file for launching application."""
from src.interface.root import View
import src.bin.validation as validation

# pylint: disable=pointless-statement
if __name__ == "__main__":
    validation  # run a system validation script
    v = View()
