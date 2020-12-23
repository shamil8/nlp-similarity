from rating import get_rating_tasks
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('/app/data/rating_tasks.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Add a number format for cells with money.
rating_format = workbook.add_format({'num_format': '# ##0'})

# Adjust the column width.
worksheet.set_column(1, 1, 15)

# Write some data headers.
worksheet.write('A1', 'Название задачи', bold)
worksheet.write('B1', 'Рейтинг', bold)


# Start from the first cell below the headers.
row = 1
col = 0

for name, rating in get_rating_tasks():
    # Convert the date string into a datetime object.
    worksheet.write_string(row, col, name)
    worksheet.write_number(row, col + 1, rating, rating_format)
    row += 1

workbook.close()
