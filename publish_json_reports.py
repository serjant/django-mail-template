#!/usr/bin/env python
import os
from json2html import *


def main():
    for file in os.listdir("./reports"):
        if file.endswith(".json"):
            f = open(os.path.join("./reports", file), 'r')
            input = f.readlines()
            html_report = json2html.convert(json=input[0])
            f = open(os.path.join("./reports", file + ".html"), 'w')
            f.writelines(html_report)


if __name__ == '__main__':
    main()
