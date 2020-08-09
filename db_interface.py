import xlsxwriter
import xlrd

def write_to_database(item_name, buy_price, sell_price, quantity):
    existing_data = read_from_database()

    wb = xlsxwriter.Workbook("transactions.xlsx")
    ws = wb.add_worksheet()

    # Write existing data
    if len(existing_data) !=0:
        for row in range(len(existing_data)):
           ws.write(row, 0, existing_data[row][0])
           ws.write(row, 1, existing_data[row][1])
           ws.write(row, 2, existing_data[row][2])
           ws.write(row, 3, existing_data[row][3])
           ws.write(row, 4, existing_data[row][4])

    
    # Write headers
    ws.write(0, 0, "ID")
    ws.write(0, 1, "Item name")
    ws.write(0, 2, "Buy price")
    ws.write(0, 3, "Sell price")
    ws.write(0, 4, "Quantity")

    # Write new data
    if len(existing_data) == 0:
        ws.write(1, 0, 1)
        ws.write(1, 1, item_name)
        ws.write(1, 2, buy_price)
        ws.write(1, 3, sell_price)
        ws.write(1, 4, quantity)
    else:
        ws.write(len(existing_data), 0, len(existing_data))
        ws.write(len(existing_data), 1, item_name)
        ws.write(len(existing_data), 2, buy_price)
        ws.write(len(existing_data), 3, sell_price)
        ws.write(len(existing_data), 4, quantity)

    # Save file
    wb.close()


def read_from_database():
    wb = xlrd.open_workbook("transactions.xlsx")
    ws = wb.sheet_by_index(0)

    #Columns are [ID, item name, buy price, sell price, quantity]
    all_rows = []
    for i in range(ws.nrows):
        current_row = []
        current_row.append(ws.cell_value(i, 0)) #getting the ID of the current row
        current_row.append(ws.cell_value(i, 1))
        current_row.append(ws.cell_value(i, 2))
        current_row.append(ws.cell_value(i, 3))
        current_row.append(ws.cell_value(i, 4))
        all_rows.append(current_row)

    return all_rows