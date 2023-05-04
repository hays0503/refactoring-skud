from PySide6.QtWidgets import QWidget,QTreeWidget,QTreeWidgetItem
from PySide6.QtGui import QBrush

import json

from GUI.CommonFunc.info_color import pick_color

class TreeListEthernet(QWidget):
    """Виджет для отображении информации которая приходит и уходит в интернет и из него
    """
    def __init__(self):
        super().__init__()
        self.tree_widget = QTreeWidget()
        self.set_header()
        self.set_style()
    
    def set_header(self):
        """
            Установка заголовка
        """
        self.tree_widget.setHeaderLabels(
            ["__Событие__", "___Дата события___", "___Серийный номер___"])
        # Включаем сортировку по колонкам
        self.tree_widget.setSortingEnabled(True)
        # Разрешить перенос слов
        self.tree_widget.setWordWrap(True)

    def set_style(self):
        self.tree_widget.setColumnWidth(0, 700)
        self.tree_widget.setColumnWidth(1, 150)
        self.tree_widget.setColumnWidth(2, 150)

    def add_new_item(self, string: str, address_in_converter: int):
        json_acceptable_string = string.replace("'", "\"")
        data = json.loads(json_acceptable_string)
        data_dict = dict(data)

        items = []
        if len(data_dict["messages"]) != 0:
            Header = [str(data_dict["messages"][0]["operation"]),
                      str(data_dict["date"]), str(data_dict["sn"])]
            for operation in data_dict["messages"]:
                item = QTreeWidgetItem(Header)
                operation: dict
                Child = QTreeWidgetItem([operation.__str__()])
                item.addChild(Child)
            # Изменение цвета для лучшее читаемости
            item.setBackground(0, QBrush(pick_color(address_in_converter)))
            item.setBackground(1, QBrush(pick_color(address_in_converter)))
            item.setBackground(2, QBrush(pick_color(address_in_converter)))
            items.append(item)