from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox, QInputDialog, QLineEdit
from random_recipe import Ui_MainWindow
import sys
from random import randrange
# import qdarkstyle
# import pprint


class MyGui(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.run_count = 0

        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_all_select.clicked.connect(self.check_all)
        self.pushButton_add.clicked.connect(self.add_recipe)

    def run(self):
        self.run_count += 1
        recipe_list = []
        for item in self.groupBox.findChildren(QCheckBox):
            if item.isChecked():
                recipe_list.append(item.text())
        if not recipe_list:
            QMessageBox.warning(self, '错误', '需要选择食谱')
            return
        index = randrange(0, len(recipe_list))
        self.textBrowser.append(f'随即结果{self.run_count}: {recipe_list[index]}')

    def check_all(self):
        all_check_list = self.groupBox.findChildren(QCheckBox)
        flag = all_check_list[0].isChecked()
        for item in all_check_list:
            if flag:
                item.setChecked(False)
            else:
                item.setChecked(True)

    def add_recipe(self):
        value, flag = QInputDialog.getText(self, "添加食谱", "请输入希望添加的食谱:", QLineEdit.Normal, "焖面")
        if flag:
            checkbox = QCheckBox(value)
            self.verticalLayout_3.addWidget(checkbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mygui = MyGui()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # qdarkstyle.load_stylesheet_pyqt5()
    mygui.show()
    sys.exit(app.exec_())
