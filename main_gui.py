from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
# from ui.random_recipe import Ui_MainWindow
from ui.random_recipe2 import Ui_MainWindow
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
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)  # 最大化最小化设置
        self.setWindowIcon(QIcon('statics/food.ico'))  # 图标设置

        self.result = []
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_add.clicked.connect(self.add_recipe)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_load.clicked.connect(self.load)

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

    def reset(self):
        self.result = []
        self.textBrowser.setText('')

    # def check_all(self):
    #     all_check_list = self.groupBox.findChildren(QCheckBox)
    #     flag = all_check_list[0].isChecked()
    #     for item in all_check_list:
    #         if flag:
    #             item.setChecked(False)
    #         else:
    #             item.setChecked(True)

    def add_recipe(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def _open_file(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mygui = MyGui()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # qdarkstyle.load_stylesheet_pyqt5()
    mygui.show()
    sys.exit(app.exec_())
