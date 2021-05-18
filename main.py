"""Main file for launching application."""
import src.interface.view as view
import src.bin.validation as validation

# pylint: disable=pointless-statement
if __name__ == "__main__":
    validation  # run a system validation script
    v = view.View()
