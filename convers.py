import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QLineEdit, QGridLayout, QMessageBox, QFrame, QAction, QWidget
from PyQt5.QtCore import Qt


class UnitConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建菜单栏
        menubar = self.menuBar()

        # 创建“说明”菜单选项
        instruction_action = QAction('使用说明', self)
        instruction_action.triggered.connect(self.show_instruction)
        menubar.addAction(instruction_action)

        # 创建“关于”菜单选项
        about_action = QAction('关于', self)
        about_action.triggered.connect(self.show_about)
        menubar.addAction(about_action)

        self.setWindowTitle('营造尺计算器')
        self.setGeometry(500, 400, 800, 360)


        # 创建一个中心窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 20, 20, 0)  

        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)

        first_row_layout = QVBoxLayout()
        cai_layout = QHBoxLayout()
        cai_layout.setAlignment(Qt.AlignLeft)  

        chi_layout = QHBoxLayout()
        first_row_layout.addLayout(cai_layout)
        first_row_layout.addLayout(chi_layout)

        cai_deng_label = QLabel('选择材等：')
        cai_deng_label.setFixedWidth(120)  
        self.cai_deng_combo = QComboBox()
        self.cai_deng_combo.addItems(['一等材', '二等材', '三等材', '四等材', '五等材', '六等材', '七等材', '八等材'])
        self.cai_deng_combo.setCurrentIndex(2)  
        self.cai_deng_combo.setFixedWidth(120)  
        self.cai_deng_combo.currentTextChanged.connect(self.update_results)  
        cai_layout.addWidget(cai_deng_label)  
        cai_layout.addWidget(self.cai_deng_combo)  

        chi_to_cm_label = QLabel('输入1尺等于：')
        chi_to_cm_label.setFixedWidth(120)  
        self.chi_to_cm_edit = QLineEdit()
        self.chi_to_cm_edit.setPlaceholderText('请输入1尺等于的厘米数')
        self.chi_to_cm_edit.setText('31.2')  
        self.chi_to_cm_edit.setFixedWidth(120)  
        self.chi_to_cm_edit.setAlignment(Qt.AlignRight)  
        self.chi_to_cm_edit.textChanged.connect(self.update_results)  
        chi_to_cm_unit_label = QLabel('厘米')
        chi_layout.addWidget(chi_to_cm_label)
        chi_layout.addWidget(self.chi_to_cm_edit)
        chi_layout.addWidget(chi_to_cm_unit_label)

        first_row_widget = QWidget()
        first_row_widget.setLayout(first_row_layout)
        first_row_widget.setFixedWidth(400)  
        top_layout.addWidget(first_row_widget)

        self.result_grid = QGridLayout()
        self.result_grid.setHorizontalSpacing(0)  
        self.result_grid.setVerticalSpacing(0)  

        self.result_labels = [[QLabel() for _ in range(5)] for _ in range(3)]  
        for i in range(3):
            for j in range(5):
                label = self.result_labels[i][j]
                label.setAlignment(Qt.AlignLeft)
                label.setFixedHeight(50)  
                label.setFixedWidth(120)  
                label.setTextInteractionFlags(Qt.TextSelectableByMouse)  
                self.result_grid.addWidget(label, i, j)

        result_widget = QWidget()
        result_widget.setLayout(self.result_grid)
        result_widget.setFixedHeight(150)  
        result_widget.setContentsMargins(0, 0, 0, 0)  
        top_layout.addWidget(result_widget)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)

        module1_layout = QGridLayout()
        module1_layout.setHorizontalSpacing(10)
        module1_layout.setVerticalSpacing(10)
        module1_layout.setContentsMargins(20, 0, 20, 20)  

        self.cai_edit = QLineEdit()
        self.cai_edit.setFixedWidth(120)
        self.cai_edit.setAlignment(Qt.AlignRight)  
        cai_unit_label = QLabel('材')

        self.kuai_edit = QLineEdit()
        self.kuai_edit.setFixedWidth(120)
        self.kuai_edit.setAlignment(Qt.AlignRight)  
        kuai_unit_label = QLabel('栔')

        self.fen_du_edit = QLineEdit()
        self.fen_du_edit.setFixedWidth(120)
        self.fen_du_edit.setAlignment(Qt.AlignRight)  
        fen_du_unit_label = QLabel('分°')

        module1_layout.addWidget(self.cai_edit, 0, 2)
        module1_layout.addWidget(cai_unit_label, 0, 3)
        module1_layout.addWidget(self.kuai_edit, 0, 4)
        module1_layout.addWidget(kuai_unit_label, 0, 5)
        module1_layout.addWidget(self.fen_du_edit, 0, 6)
        module1_layout.addWidget(fen_du_unit_label, 0, 7)

        self.chi_edit = QLineEdit()
        self.chi_edit.setFixedWidth(120)
        self.chi_edit.setAlignment(Qt.AlignRight)  
        chi_unit_label = QLabel('尺')

        self.cun_edit = QLineEdit()
        self.cun_edit.setFixedWidth(120)
        self.cun_edit.setAlignment(Qt.AlignRight)  
        cun_unit_label = QLabel('寸')

        self.fen_edit = QLineEdit()
        self.fen_edit.setFixedWidth(120)
        self.fen_edit.setAlignment(Qt.AlignRight)  
        fen_unit_label = QLabel('分')

        self.li_edit = QLineEdit()
        self.li_edit.setFixedWidth(120)
        self.li_edit.setAlignment(Qt.AlignRight)  
        li_unit_label = QLabel('厘')

        module1_layout.addWidget(self.chi_edit, 1, 0)
        module1_layout.addWidget(chi_unit_label, 1, 1)
        module1_layout.addWidget(self.cun_edit, 1, 2)
        module1_layout.addWidget(cun_unit_label, 1, 3)
        module1_layout.addWidget(self.fen_edit, 1, 4)
        module1_layout.addWidget(fen_unit_label, 1, 5)
        module1_layout.addWidget(self.li_edit, 1, 6)
        module1_layout.addWidget(li_unit_label, 1, 7)

        self.cm_edit = QLineEdit()
        self.cm_edit.setFixedWidth(120)
        self.cm_edit.setAlignment(Qt.AlignRight)  
        cm_unit_label = QLabel('厘米')

        module1_layout.addWidget(self.cm_edit, 2, 6)
        module1_layout.addWidget(cm_unit_label, 2, 7)

        self.module1_result_labels = [[QLabel() for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                label = self.module1_result_labels[i][j]
                label.setAlignment(Qt.AlignCenter)
                label.setFixedHeight(50)
                label.setFixedWidth(150)
                label.setTextInteractionFlags(Qt.TextSelectableByMouse)  
                module1_layout.addWidget(label, i,8 + j)

        main_layout.addLayout(module1_layout)

        self.cai_to_cun_ratio = 7.5  
        self.update_results(self.cai_deng_combo.currentText())

        self.cai_edit.textChanged.connect(lambda: self.update_module1_results(0))
        self.kuai_edit.textChanged.connect(lambda: self.update_module1_results(0))
        self.fen_du_edit.textChanged.connect(lambda: self.update_module1_results(0))
        self.chi_edit.textChanged.connect(lambda: self.update_module1_results(1))
        self.cun_edit.textChanged.connect(lambda: self.update_module1_results(1))
        self.fen_edit.textChanged.connect(lambda: self.update_module1_results(1))
        self.li_edit.textChanged.connect(lambda: self.update_module1_results(1))
        self.cm_edit.textChanged.connect(lambda: self.update_module1_results(2))

    def update_results(self, cai_deng):
        cai_to_cun_ratios = {
            '一等材': 9,
            '二等材': 8.25,
            '三等材': 7.5,
            '四等材': 7.2,
            '五等材': 6.6,
            '六等材': 6,
            '七等材': 5.25,
            '八等材': 4.5
        }
        self.cai_to_cun_ratio = cai_to_cun_ratios.get(cai_deng, 7.5)  

        chi_to_cm_text = self.chi_to_cm_edit.text()
        if not chi_to_cm_text.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, '输入错误', '请输入正确的数字，精度2位')
            return
        chi_to_cm = float(chi_to_cm_text)

        cai_to_cun = self.cai_to_cun_ratio
        cai_to_chi = cai_to_cun / 10
        cai_to_cm = cai_to_chi * chi_to_cm

        kuai_to_fen_du = 6
        kuai_to_cun = kuai_to_fen_du * (1 / 15) * cai_to_cun
        kuai_to_chi = kuai_to_cun / 10
        kuai_to_cm = kuai_to_chi * chi_to_cm

        fen_du_to_cun = (1 / 15) * cai_to_cun
        fen_du_to_chi = fen_du_to_cun / 10
        fen_du_to_cm = fen_du_to_chi * chi_to_cm

        self.result_labels[0][0].setText('1材')
        self.result_labels[0][1].setText(f'= {15:.2f} 分°')
        self.result_labels[0][2].setText(f'= {cai_to_chi:.2f} 尺')
        self.result_labels[0][3].setText(f'= {cai_to_cun:.2f} 寸')
        self.result_labels[0][4].setText(f'= {cai_to_cm:.2f} 厘米')

        self.result_labels[1][0].setText('1栔')
        self.result_labels[1][1].setText(f'= {kuai_to_fen_du:.2f} 分°')
        self.result_labels[1][2].setText(f'= {kuai_to_chi:.2f} 尺')
        self.result_labels[1][3].setText(f'= {kuai_to_cun:.2f} 寸')
        self.result_labels[1][4].setText(f'= {kuai_to_cm:.2f} 厘米')

        self.result_labels[2][0].setText('1分°')
        self.result_labels[2][1].setText('')  
        self.result_labels[2][2].setText(f'= {fen_du_to_chi:.2f} 尺')
        self.result_labels[2][3].setText(f'= {fen_du_to_cun:.2f} 寸')
        self.result_labels[2][4].setText(f'= {fen_du_to_cm:.2f} 厘米')

        self.update_module1_results(0)
        self.update_module1_results(1)
        self.update_module1_results(2)

    def update_module1_results(self, row):
        try:
            if row == 0:
                cai = float(self.cai_edit.text() or 0)
                kuai = float(self.kuai_edit.text() or 0)
                fen_du = float(self.fen_du_edit.text() or 0)
                total_cun = (cai * self.cai_to_cun_ratio) + (kuai * (6 / 15) * self.cai_to_cun_ratio) + (fen_du * (1 / 15) * self.cai_to_cun_ratio)
            elif row == 1:
                chi = float(self.chi_edit.text() or 0)
                cun = float(self.cun_edit.text() or 0)
                fen = float(self.fen_edit.text() or 0)
                li = float(self.li_edit.text() or 0)
                total_cun = (chi * 10) + cun + (fen / 10) + (li / 100)
            elif row == 2:
                cm = float(self.cm_edit.text() or 0)
                total_cun = cm / (float(self.chi_to_cm_edit.text()) / 10)

            chi_to_cm = float(self.chi_to_cm_edit.text())
            total_cm = total_cun * (chi_to_cm / 10)
            total_m = total_cm / 100

            self.module1_result_labels[row][0].setText(f'= {total_cun:.2f} 寸')
            self.module1_result_labels[row][1].setText(f'= {total_cm:.2f} 厘米')
            self.module1_result_labels[row][2].setText(f'= {total_m:.2f} 米')
        except ValueError:
            for j in range(3):
                self.module1_result_labels[row][j].setText('总寸数: -')

    def show_about(self):
        abot_message = """
        <h4><center>关于工具</center></h4>
        <p>这是基于宋式大木作的营造尺计算器工具，根据材等进行各种营造尺和公制尺寸的换算。<br>默认营造尺1尺=31.2厘米（可以自行设定）</p>
        <hr>
        <h6>作者：孜然鸡丁</h6>
        <h6>邮箱：ryantxq@sina.com</h6>
        <h6>网站：<a href="https://www.moonstone.fun">月石MoonStone</a></h6>
        """
        QMessageBox.about(self, '关于', abot_message)

    def show_instruction(self):
        use_message = """
        <h4><center>使用说明</center></h4>
        <ol>
        <li>先选择所用材等，总共分为1等材~8等材</li>
        <li>再输入1营造尺对应的公制厘米数，默认设置为1尺 = 31.2厘米</li>
        <li>下方左边可以分别按照材、栔、分°，尺、寸、分、厘或者公制厘米数，计算对应的以尺和厘米为单位的数值</li>
        </ol>
        <hr>
        <p>八个材等分别对应1材的尺寸为：</p>
        <ul>
        <li>一等材：9寸</li>
        <li>二等材：8.25寸</li>
        <li>三等材：7.5寸</li>
        <li>四等材：7.2寸</li>
        <li>五等材：6.6寸</li>
        <li>六等材：6寸</li>
        <li>七等材：5.25寸</li>
        <li>八等材：4.5寸</li>
        </ul>
        <hr>
        <p>材份制中材、栔、分°对应关系：</p>
        <ul>
        <li>1材 = 15分°</li>
        <li>1栔 = 6分°</li>
        </ul>
        """
        QMessageBox.about(self, '使用说明', use_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UnitConverter()
    ex.show()
    sys.exit(app.exec_())