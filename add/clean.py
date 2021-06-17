#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,platform

def _cls():
	if os.name == "nts":
		os.system("cls")
	else:
		os.system("clear")

_cls()