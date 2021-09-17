import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts


def get_all_suppliers():
    return query("""SELECT * FROM supplier""")

def get_supplier_products(supplier_id):
    return query("""SELECT * FROM Product
                    INNER JOIN Category
	                    ON Product.CategoryId=Category.Id                 
                    WHERE SupplierId = ?""", supplier_id)                 

def get_supplier_name(supplier_id):
    return query("""
                    SELECT CompanyName FROM Supplier
                    WHERE Id = ?""", supplier_id)

def get_all_categories():
    return query("""SELECT Category.CategoryName, Category.Description,  Category.Id, COUNT(Product.Id) AS ProductCount
                    FROM Category
                    INNER JOIN Product
		                ON Category.Id=Product.CategoryId
		            GROUP By CategoryName""")
def get_category_products(category_id):
    return query("""SELECT Product.ProductName, Supplier.CompanyName, Category.CategoryName, Category.Id, Supplier.Id AS SupplierID
                    FROM Product
                    INNER JOIN Supplier
		                ON Product.SupplierId=Supplier.Id
                    INNER JOIN Category
		                ON Product.CategoryId=Category.Id
                    WHERE CategoryId=?""", category_id)
def get_category_name(category_id):
    return query("""
                    SELECT CategoryName FROM Category
                    WHERE Id = ?""", category_id)
