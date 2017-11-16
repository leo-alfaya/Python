import xlrd
import xlwt


def open_workbook(filename):
    return xlrd.open_workbook(filename=filename)


def create_workbook():
    return xlwt.Workbook()


workbook_base = open_workbook("CONTATO APP.xlsx")
worksheet_base = workbook_base.sheet_by_index(0)

values = worksheet_base.col(0)
nome_email = [x.value.split(";") for x in values]
del nome_email[0]

row = 0

workbook_dest = create_workbook()
workbook_dest.add_sheet("lista_emails")
worksheet_dest = workbook_dest.get_sheet(0)

for x in nome_email:
    worksheet_dest.write(row, 0, x[0])
    worksheet_dest.write(row, 1, x[1])
    row += 1

workbook_dest.save("Emails.xls")
