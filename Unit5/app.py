from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def hello_world():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)

@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    supplier=database.get_supplier_name(supplier_id)
    return render_template('products.html', products=products, supplier=supplier) 

@app.route("/categories")
def categories():
    categories=database.get_all_categories()
    return render_template('categories.html', categories=categories)

@app.route("/categories/<int:category_id>")
def category_products(category_id):
    category_products=database.get_category_products(category_id)
    category=database.get_category_name(category_id)
    return render_template('category_products.html', category_products=category_products, category=category)