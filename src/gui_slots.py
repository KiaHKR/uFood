class GuiSlots:
    """Class that contains methods used to run logic from the GUI as well as
    update the GUI."""

    selected_ingredients = []

    def __init__(self):
        """Constructor of GuiSlots"""
        self.selected_ingredients = []

    def on_search_changed(self, left_panel, db_ingredients, text, list_box):
        self.drop_down_list(left_panel)
        self.filter_list(db_ingredients, text, list_box)

    def drop_down_list(self, left_panel):
        """Refreshes the visibility of list, depending on whether text has
        been input or not."""
        if left_panel.children()[2].children()[1].text():
            left_panel.children()[2].children()[4].setVisible(True)
        else:
            left_panel.children()[2].children()[4].setVisible(False)

    def filter_list(self, db_ingredients, text, list_box):
        """Filters contents of list depending on input.
        Adjusts height of result box, depending on number of results."""
        list_box.clear()
        result_list = []

        # TODO --- REPLACE WITH A DB QUERY THAT HANDLES SORTING
        for i in db_ingredients:
            if text in i and i not in self.selected_ingredients:
                result_list.append(i)
        # TODO ---

        list_box.addItems(result_list)

        if len(result_list) > 5:
            list_box.setFixedHeight(5 * 23)
        else:
            list_box.setFixedHeight(len(result_list) * 23)

    def select_ingredient(self, ingredient_obj, selected_item, search_bar):
        """Selects ingredient from list."""
        self.selected_ingredients.append(selected_item)
        ingredient_obj.update_ingredients(self.selected_ingredients)

        search_bar.clear()