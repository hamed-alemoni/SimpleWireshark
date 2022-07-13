def clear_text_edit(table_widget, text_edit):
    text_edit.clear()

    for row in range(table_widget.rowCount()):
        if table_widget.isRowHidden(row):
            table_widget.showRow(row)
