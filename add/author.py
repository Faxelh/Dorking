#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time
Dev_F =("""
\t\033[1;97m╔═══════════════════════════════╗
\t\033[1;97m║\033[1;91m[\033[1;93m©\033[1;91m]\033[38;5;95m Dev \033[1;97m:\033[38;5;214m Faxel ── \033[38;5;112m\033[3;5;1m@faxelh\033[3;0;0m  \033[1;91m[\033[1;93m©\033[1;91m]\033[1;97m║
\t\033[1;97m╚═══════════════════════════════╝""")

author =("""  \033[1;97m║\x1b[48;5;198;3;5;5;1;97m              MES_INFORMATIONS             \x1b[48;0;0;3;0;0;1;97m║
  \033[1;97m╔═══════════════════════════════════════════╗
  \033[1;97m║\033[38;5;29m Author    \033[1;91m: \033[38;5;112mFaxel \033[1;91m| \033[38;5;115m@faxelh               \033[1;97m║
  \033[1;97m║\033[38;5;29m Fb        \033[1;91m: \033[38;5;247mhttps://facebook.com/threatz0 \033[1;97m║
  \033[1;97m║\033[38;5;29m Github    \033[1;91m: \033[38;5;247mhttps://github.com/threat0    \033[1;97m║
  \033[1;97m║\033[38;5;29m Blog      \033[1;91m: \033[38;5;247mhttps://faxelh.blogspot.com   \033[1;97m║
  \033[1;97m║\033[38;5;29m Twitter   \033[1;91m: \033[38;5;247mhttps://twitter.com/faxelhs   \033[1;97m║
  \033[1;97m║\033[38;5;29m Tool Name \033[1;91m: \033[38;5;247mGitHub & Google Dorking       \033[1;97m║
  \033[1;97m╚═══════════════════════════════════════════╝""")

def Auto(a):
    for o in a + "\n":
        sys.stdout.write(o);sys.stdout.flush();time.sleep(.025)
print(Dev_F);Auto(author);sys.exit()