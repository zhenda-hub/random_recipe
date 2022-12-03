from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from ui.random_recipe import Ui_MainWindow
import sys
from random import randrange
from collections import Counter
from json import dumps
# import qdarkstyle
# import pprint


class MyGui(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('statics/food.ico'))
        self.result = []

        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_all_select.clicked.connect(self.check_all)
        self.pushButton_add.clicked.connect(self.add_recipe)
        self.pushButton_reset.clicked.connect(self.reset)

    def run(self):
        recipe_list = []
        for item in self.groupBox.findChildren(QCheckBox):
            if item.isChecked():
                recipe_list.append(item.text())
        if not recipe_list:
            QMessageBox.warning(self, '错误', '需要选择食谱')
            return
        index = randrange(0, len(recipe_list))
        # self.textBrowser.append(f'随即结果{self.run_count}: {recipe_list[index]}')
        self.result.append(recipe_list[index])
        counter = Counter(self.result)
        output_str = dumps(counter, ensure_ascii=False, indent=4)

        self.textBrowser.setText('运行结果：')
        self.textBrowser.append(f'{output_str}')
        self.textBrowser.append('前三甲：')
        self.textBrowser.append(f'{counter.most_common(3)}')

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
            check_box = QCheckBox(value)
            self.verticalLayout_3.addWidget(check_box)

    def reset(self):
        self.result = []
        self.textBrowser.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mygui = MyGui()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # qdarkstyle.load_stylesheet_pyqt5()
    mygui.show()
    sys.exit(app.exec_())
