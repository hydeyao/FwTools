import FwGuide
from openpyxl import Workbook
from openpyxl import load_workbook


def init_class():
    guide = FwGuide.FwGuide(1, "ssddss", FwGuide.PID("m", "f", "s"), FwGuide.PCB("fw1", "fw2", "fw3"),
                            FwGuide.FilePath("p1", "p2", "p3"), FwGuide.BurnWay("w1", "w2", "w3"))
    workbook = load_workbook("./FW_Guide_List.xlsx")
    worksheet = workbook.active
    rows = worksheet.max_row
    columns = worksheet.max_column
    fw_list = []
    for row in range(rows - 2):
        guide = FwGuide.FwGuide(worksheet.cell(row + 3, 1).value, worksheet.cell(row + 3, 2).value,
                                FwGuide.PID(worksheet.cell(row + 3, 3).value,
                                            worksheet.cell(row + 3, 4).value,
                                            worksheet.cell(row + 3, 5).value),
                                FwGuide.PCB(worksheet.cell(row + 3, 6).value,
                                            worksheet.cell(row + 3, 7).value,
                                            worksheet.cell(row + 3, 8).value),
                                FwGuide.FilePath(worksheet.cell(row + 3, 9).value,
                                                 worksheet.cell(row + 3, 10).value,
                                                 worksheet.cell(row + 3, 11).value),
                                FwGuide.BurnWay(worksheet.cell(row + 3, 12).value,
                                                worksheet.cell(row + 3, 13).value,
                                                worksheet.cell(row + 3, 14).value))
        fw_list.insert(row, guide)
    print(fw_list)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    init_class()