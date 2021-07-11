# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# ------------------------------------------------------------
# File: handle.py
# Created Date: 2020/6/24
# Created Time: 0:14
# Author: Hypdncy
# Author Mail: hypdncy@outlook.com
# Copyright (c) 2020 Hypdncy
# ------------------------------------------------------------
#                       .::::.
#                     .::::::::.
#                    :::::::::::
#                 ..:::::::::::'
#              '::::::::::::'
#                .::::::::::
#           '::::::::::::::..
#                ..::::::::::::.
#              ``::::::::::::::::
#               ::::``:::::::::'        .:::.
#              ::::'   ':::::'       .::::::::.
#            .::::'      ::::     .:::::::'::::.
#           .:::'       :::::  .:::::::::' ':::::.
#          .::'        :::::.:::::::::'      ':::::.
#         .::'         ::::::::::::::'         ``::::.
#     ...:::           ::::::::::::'              ``::.
#    ````':.          ':::::::::'                  ::::..
#                       '.:::::'                    ':'````..
# ------------------------------------------------------------

import logging

from modle.common.loophole.loopholes import Loopholes
from modle.common.translate.baidu import TranBaidu
from modle.data.hosts import DataHosts
from modle.data.loops import DataLoops
from modle.docx.hosts import DocxHosts
from modle.docx.loops import DocxLoops


class Handle(object):
    def __init__(self, docxtype):
        """
        初始化类，并开始函数
        :param scantype:
        """
        self.docxtype = docxtype
        logging.info("开始初始化数据")
        logging.info("---开始读取数据")
        self.LOOPHOLES = Loopholes()
        self.LOOPHOLES.run()

        logging.info("---开始翻译数据")
        TranBaidu(self.LOOPHOLES).run()

    def run_hosts(self):
        """
        开始任务
        :return:
        """
        logging.info("开始生成主机排序报告")
        logging.info("---开始处理数据")
        DataHosts(self.LOOPHOLES).run()

        logging.info("---开始处理文档")
        DocxHosts(self.LOOPHOLES).run()

    def run_loops(self):
        """
        开始任务
        :return:
        """
        logging.info("开始生成漏洞排序报告")
        logging.info("---开始处理数据")
        DataLoops(self.LOOPHOLES).run()

        logging.info("---开始处理文档")
        DocxLoops(self.LOOPHOLES).run()

    def run_host(self):
        pass

    def run_all(self):
        self.run_loops()
        self.run_hosts()
        self.run_host()

    def run(self):
        func_type_run = {
            "hosts": self.run_hosts,
            "loops": self.run_loops,
            "host": self.run_host,
            "all": self.run_all
        }
        func_type_run[self.docxtype]()
        logging.info("---程序结束---")