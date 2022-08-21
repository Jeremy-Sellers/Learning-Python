import openpyxl
# Exercise one Find all companies and how many products they produce
# Loads workbook and all files
inventory_file = openpyxl.load_workbook('inventory.xlsx')
product_list = inventory_file['Sheet1']

# Calculate amount of products per supplier, set Dictionary to empty
products_per_supplier = {}

# range allows for rows ot be looped through starting at 2nd row to skio descriptor row

# for every row in product_list from row 2 to last row
for product_row in range(2, product_list.max_row + 1):
    # grab name from product_row column 4
    supplier_name = product_list.cell(product_row, 4).value
    # if name already exists set value to current_num_products
    if supplier_name in products_per_supplier:
        current_num_products = products_per_supplier[supplier_name]
        # then increase value by 1
        products_per_supplier[supplier_name] = current_num_products + 1
    else:
        print('adding new supplier')
        # Adds new supplier to dicitonary and sets value to one
        products_per_supplier[supplier_name] = 1

print(products_per_supplier)
# End of first Exercise