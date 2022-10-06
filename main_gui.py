from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox
from random_recipe import Ui_MainWindow
import sys
import random
import pprint


class MyGui(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_all_select.clicked.connect(self.check_all)
        self.pushButton_add.clicked.connect(self.add_recipe)

    def run(self):
        recipe_list = []
        for item in self.groupBox.findChildren(QCheckBox):
            if item.isChecked():
                recipe_list.append(item.text())
        if not recipe_list:
            QMessageBox.warning(self, '错误', '需要选择食谱')
            return
        index = random.randrange(0, len(recipe_list))
        self.label_result.setText(recipe_list[index])

    def check_all(self):
        all_check_list = self.groupBox.findChildren(QCheckBox)
        flag = all_check_list[0].isChecked()
        for item in all_check_list:
            if flag:
                item.setChecked(False)
            else:
                item.setChecked(True)

    def add_recipe(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mygui = MyGui()
    mygui.show()
    sys.exit(app.exec_())