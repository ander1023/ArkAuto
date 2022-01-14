# -*- encoding=utf8 -*-
__author__ = "ander"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["android://127.0.0.1:5037/emulator-5554?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


# script content
print("start...")

wait(Template(r"tpl1642001226694.png", record_pos=(-0.002, 0.116), resolution=(1280, 720)))
snapshot(msg="请填写测试点.")
wait(Template(r"tpl1642001430437.png", record_pos=(-0.459, -0.25), resolution=(1280, 720)))

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)
wait(Template(r"tpl1642147290374.png", record_pos=(-0.294, -0.252), resolution=(1280, 720)))
wait(Template(r"tpl1642147630815.png", record_pos=(-0.427, -0.068), resolution=(1280, 720)))
wait(Template(r"tpl1642148714222.png", record_pos=(0.409, 0.032), resolution=(1280, 720)))

