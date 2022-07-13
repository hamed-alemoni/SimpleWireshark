def search_in_table_widget(table_widget, text_edit, column_names: list):
    if text_edit.toPlainText():
        # get whole search text edit text
        text = text_edit.toPlainText().split()

        searched_text = find_searched_text(text)

        column_name = find_column_name(text)

        column_name_index = find_index_of_column_name(column_names, column_name)

        if column_name_index != -1:

            hide_unmatched_rows(table_widget, column_name_index, searched_text)


def hide_unmatched_rows(table_widget, column_index, text):

    for row in range(table_widget.rowCount()):
        # get each item in the that particular column
        item = table_widget.item(row, column_index)
        # hide any row that doesn't match with user filter
        table_widget.setRowHidden(row, text not in item.text().lower())


def find_column_name(text: list) -> str:
    column_name = ''
    # find the column name that the program search in
    for i in range(len(text) - 1):
        column_name += text[i].lower() + ' '
    column_name = column_name.strip()

    return column_name


def find_index_of_column_name(column_names: list, column_name: str) -> int:

    column_names = [value.lower() for value in column_names]

    if column_name in column_names:
        # find index of that column
        column_name_index = column_names.index(column_name)

        return column_name_index

    return -1


def find_searched_text(text: list) -> str:
    # the text that user want to filter with that
    searched_text = text[-1].lower()
    return searched_text
