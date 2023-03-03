#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
# require only template with words, line, and styling for report
import datetime
# to generate today date
import logging



def generate_report(filename,title,content):
    # start doc
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    layout = []
    # generate elements of report 
    blank_line = Spacer(1,20)
    title = Paragraph(title, styles["h1"])
    content = Paragraph(content, styles["BodyText"])
    # build report
    layout.append(title)
    layout.append(blank_line)
    layout.append(content)
    report.build(layout)
    logging.info("Report {} sucessfully generated".format(filename))

if __name__ == '__main__':
    # testing code
    logging.basicConfig(level=logging.DEBUG)
    filename = "processed.pdf"
    title = "Processed Update on " + datetime.date.today().strftime("%d/%m/%Y")
    content = "name: Apple <br/>weight: 500 lbs"
    generate_report(filename,title,content)