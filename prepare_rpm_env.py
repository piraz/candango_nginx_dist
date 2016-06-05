#!/usr/bin/env python
from __future__ import print_function
import os

RPMBUILDER_USER = 'rpmbuilder'


def rpmbuilder_user_exists():
    u_files = open("/etc/passwd", 'r')
    for line in u_files.readlines():
        if RPMBUILDER_USER == line.split(":")[0]:
            u_files.close()
            return True
    u_files.close()
    return False


def create_rpmbuilder_user():
    print("Creating rpmbuilder user ...", end="")
    os.system("useradd %s" % RPMBUILDER_USER)
    print(" [OK].")

if __name__ == "__main__":
    if not rpmbuilder_user_exists():
        create_rpmbuilder_user()
    else:
        print("The user rpmbuilder already exists.")

