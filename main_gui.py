import os.path
from PyQt5.QtCore import Qt, QCoreApplication
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox, QInputDialog, QLineEdit
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
# from ui.random_recipe import Ui_MainWindow
from ui.random_recipe2 import Ui_MainWindow
import sys
from random import randrange
from collections import Counter
from json import dumps
from functools import partial
import json


# import qdarkstyle
# import pprint


class MyGui(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)  # 最大化最小化设置
        self.setWindowIcon(QIcon('statics/food.ico'))  # 图标设置

        self.result = []  # 结果
        self.options = []  # 选项池
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_reset.clicked.connect(self.reset)
        # self.pushButton_add.clicked.connect(self.add_options)
        self.pushButton_clear_options.clicked.connect(self.clear_all)
        self.lineEdit_input.returnPressed.connect(self.add_options)  # 输入框的回车信号
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_load.clicked.connect(self.load)

    def run(self):
        if not self.options:
            QtWidgets.QMessageBox.warning(self, '提示', '请添加选项')
            return
        # for item in self.groupBox_options.findChildren(QtWidgets.QLabel):
        #     recipe_list.append(item.text())

        # 随机一个
        index = randrange(0, len(self.options))
        self.result.append(self.options[index])
        # 转换Counter输出
        counter = Counter(self.result)
        output_str = dumps(counter, ensure_ascii=False, indent=4)

        self.textBrowser.setText('运行结果：')
        self.textBrowser.append(f'{output_str}')
        self.textBrowser.append('前三甲：')
        self.textBrowser.append(f'{counter.most_common(3)}')

    def reset(self):
        self.result = []
        self.textBrowser.setText('')

    def clear_all(self):
        pushButton_list = self.groupBox_options.findChildren(QtWidgets.QPushButton)
        for item in pushButton_list:
            item.click()

    def add_options(self):
        option_name = self.lineEdit_input.text()

        if option_name:
            self.options.append(option_name)
            self._add_option(option_name)

        self.lineEdit_input.setText('')  # 重置输入框

    def _add_option(self, option_name):
        horizontalLayout_option = QtWidgets.QHBoxLayout()
        label_option_name = QtWidgets.QLabel(self.groupBox_options)
        horizontalLayout_option.addWidget(label_option_name)

        pushButton_delete = QtWidgets.QPushButton(self.groupBox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_delete.sizePolicy().hasHeightForWidth())
        pushButton_delete.setSizePolicy(sizePolicy)
        horizontalLayout_option.addWidget(pushButton_delete)
        horizontalLayout_option.setStretch(0, 2)
        horizontalLayout_option.setStretch(1, 1)
        self.verticalLayout_3.addLayout(horizontalLayout_option)

        _translate = QCoreApplication.translate
        label_option_name.setText(_translate("MainWindow", option_name))
        pushButton_delete.setText(_translate("MainWindow", "-"))

        # 添加删除信号
        pushButton_delete.clicked.connect(
            partial(self.delete_option, label_option_name, pushButton_delete, horizontalLayout_option))

    def delete_option(self, label, pushButton, horizontalLayout):
        self.options.remove(label.text())
        label.deleteLater()
        pushButton.deleteLater()
        horizontalLayout.deleteLater()

    def save(self):
        # {
        #     'options': []
        # }
        file_abspath, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "文件保存", "./settings",
                                                                        "txt Files (*.txt)")
        print('file_abspath', file_abspath)
        print('file_abspath', type(file_abspath))
        print('file_type', file_type)
        print('file_type', type(file_type))

        out_dict = {'options': self.options}
        try:
            json.dump(out_dict, open(file_abspath, 'w', encoding='u8'), ensure_ascii=False, indent=4)
        except:
            pass
        # if file_abspath:
        #     json.dump(out_dict, open(file_abspath, 'w', encoding='u8'), ensure_ascii=False, indent=4)
        #

    def load(self):
        file_abspath, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "选取txt文件", "./settings",
                                                                        "txt Files (*.txt)")
        print('file_abspath', file_abspath)
        print('file_abspath', type(file_abspath))
        print('file_type', file_type)
        print('file_type', type(file_type))
        try:
            load_dict = json.load(open(file_abspath, 'r', encoding='u8'))
        except:  # 文件load错误
            pass
        else:
            self.clear_all()
            self.options = load_dict.get('options', [])  # 默认为空列表
            for item in self.options:
                self._add_option(item)


def gene_fold(fold):
    if not os.path.exists(fold):
        os.makedirs(fold)


if __name__ == '__main__':
    # 创建文件夹
    gene_fold('settings')
    # 启动应用
    app = QtWidgets.QApplication(sys.argv)

    mygui = MyGui()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # qdarkstyle.load_stylesheet_pyqt5()
    mygui.show()

    sys.exit(app.exec_())
