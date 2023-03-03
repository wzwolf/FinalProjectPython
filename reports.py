#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
# require only template with words, line, and styling for report
import datetime
# to generate today date
import logging


def generate_report(report_input):
    """
    report_input - dictionary of values
    takes processed data from supplier-data/description
    return 
    Processed Update on <Today's date>
    [blank line]
    name: <Apple>
    weight: <500> lbs
    [blank line]
    name: <Avocado>
    weight: <200> lbs
    [blank line]
    ...
    """
    # start doc
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(report_input["filename"])
    layout = []
    # generate elements of report 
    blank_line = Spacer(1,30)
    title = Paragraph(report_input["title"]+report_input["today_date"], styles["h1"])
    # build report
    layout.append(title)
    layout.append(blank_line)
    # generate content element of report
    for text in report_input["content"]:
        content = Paragraph(text,styles["BodyText"])
        layout.append(content)
        layout.append(blank_line)
    report.build(layout)
    logging.info("Report {} sucessfully generated".format(report_input["filename"]))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    report_info = {}
    report_info["filename"] = "processed.pdf"
    report_info["title"] = "Processed Update on "
    report_info["today_date"] = datetime.date.today().strftime("%d/%m/%Y")
    report_info["content"] = []
    generate_report(report_input=report_info)