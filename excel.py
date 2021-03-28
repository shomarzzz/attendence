import xlrd
import xlsxwriter
sub = ["Roll", "English 1st", "English 2nd", "Bangla 1st", "Bangla 2nd", "G.Math", "H.Math", "ICT", "Religion",
       "Physics", "Chemistry", "Biology"]


def detect(subject, present, present_or_absent):
    if present_or_absent:
        i = 1
    else:
        i = -1
    workbook = xlrd.open_workbook("student.xlsx")
    worksheet = workbook.sheet_by_index(0)
    all_rows = []
    for row in range(worksheet.nrows):
        cur_row = []
        for col in range(worksheet.ncols):
            cur_row.append(worksheet.cell_value(row, col))
        all_rows.append(cur_row)
    print(all_rows)
    for i in range(worksheet.nrows):
        if all_rows[i][0] in present:
            all_rows[i][sub.index(subject)] += i
    print(all_rows)
    workbook = xlsxwriter.Workbook("student.xlsx")
    worksheet = workbook.add_worksheet()
    for row in range(len(all_rows)):
        for col in range(len(all_rows[0])):
            worksheet.write(row, col, all_rows[row][col])
    workbook.close()

