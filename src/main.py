"""Main file."""

from ui import views as v


if __name__ == '__main__':
    v.Views(windowTitle=v.product_name, windowIcon=v.Views.set_product_icon())
