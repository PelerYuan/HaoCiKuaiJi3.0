import logging
import os
from urllib.parse import quote

from PySide6.QtCore import QUrl
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QDialog

from DataStract.WordTest import WordTest
from Models.EditWordModel import EditWordModel
from Views.TestResultDialog import Ui_Dialog
from pyecharts import options as opts
from pyecharts.charts import Liquid


class TestResultModel(Ui_Dialog, QDialog):
    def __init__(self, data: WordTest, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.data: WordTest = data

        self.init()
        self.event_connect()

    def init(self):
        self.listWidget.addItems(self.data.get_wrong_words())
        self.generate_chart()
        absolute_path = os.path.abspath("./data/pyechart/test_result.html")
        file_url = f"file:///{quote(absolute_path.replace('\\', '/'))}"
        self.webEngineView.setUrl(file_url)

    def generate_chart(self):
        local_assets_path = "./assess/"
        c = (
            Liquid(init_opts=opts.InitOpts(width="500px", js_host=local_assets_path))
            .add("Correct percentage", [self.data.get_correct_percentage()],
                 is_outline_show=False,
                 center=["50%", "50%"],
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title="Correct percentage"))
            .render("./data/pyechart/test_result.html")  # 输出 HTML
        )

    def event_connect(self):
        ...
