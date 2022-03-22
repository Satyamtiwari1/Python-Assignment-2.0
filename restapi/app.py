<<<<<<< HEAD
from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS

from Customer_Database import get_customer, get_customer_by_id, insert_customer, update_customer
from Orders_Database import get_Order_by_id, get_Orders, insert_Orders, update_Order
from Products_Database import get_Product, get_Product_by_id, insert_Product, update_Product #added to top of file
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# For Customer Table
@app.route('/api/Customer', methods=['GET'])
def api_get_Customers():
    return jsonify(get_customer())

@app.route('/api/Customer/<CustomerID>', methods=['GET'])
def api_get_Customer(CustomerID):
    return jsonify(get_customer_by_id(CustomerID))

@app.route('/api/Customer',  methods = ['POST'])
def api_add_Customer():
    customer_data = request.json
    return jsonify(insert_customer(customer_data))

@app.route('/api/Customer',  methods = ['PUT'])
def api_update_Customer():
    customer_data = request.get_json()
    return jsonify(update_customer(customer_data))
#For Products Table
@app.route('/api/Product', methods=['GET'])
def api_get_Products():
    return jsonify(get_Product())

@app.route('/api/Product/<ProductID>', methods=['GET'])
def api_get_Product(ProductID):
    return jsonify(get_Product_by_id(ProductID))

@app.route('/api/Product',  methods = ['POST'])
def api_add_Product():
    product_data = request.json
    return jsonify(insert_Product(product_data))

@app.route('/api/Product',  methods = ['PUT'])
def api_update_Product():
    Product_data = request.get_json()
    return jsonify(update_Product(Product_data))
# For Orders Table
@app.route('/api/Order', methods=['GET'])
def api_get_Orders():
    return jsonify(get_Orders())

@app.route('/api/Order/<OrderID>', methods=['GET'])
def api_get_Order(OrderID):
    return jsonify(get_Order_by_id(OrderID))

@app.route('/api/Order',  methods = ['POST'])
def api_add_Order():
    Order_data = request.json
    return jsonify(insert_Orders(Order_data))

@app.route('/api/Order',  methods = ['PUT'])
def api_update_Order():
    Order_data = request.get_json()
    return jsonify(update_Order(Order_data))

# @app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
# def api_delete_user(user_id):
#     return jsonify(delete_user(user_id))

if __name__ == "__main__":
    #app.debug = True
    app.run(debug=True)
=======
from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS

from Customer_Database import get_customer, get_customer_by_id, insert_customer, update_customer
from Orders_Database import get_Order_by_id, get_Orders, insert_Orders, update_Order
from Products_Database import get_Product, get_Product_by_id, insert_Product, update_Product #added to top of file
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# For Customer Table
@app.route('/api/Customer', methods=['GET'])
def api_get_Customers():
    return jsonify(get_customer())

@app.route('/api/Customer/<CustomerID>', methods=['GET'])
def api_get_Customer(CustomerID):
    return jsonify(get_customer_by_id(CustomerID))

@app.route('/api/Customer',  methods = ['POST'])
def api_add_Customer():
    customer_data = request.json
    return jsonify(insert_customer(customer_data))

@app.route('/api/Customer',  methods = ['PUT'])
def api_update_Customer():
    customer_data = request.get_json()
    return jsonify(update_customer(customer_data))
#For Products Table
@app.route('/api/Product', methods=['GET'])
def api_get_Products():
    return jsonify(get_Product())

@app.route('/api/Product/<ProductID>', methods=['GET'])
def api_get_Product(ProductID):
    return jsonify(get_Product_by_id(ProductID))

@app.route('/api/Product',  methods = ['POST'])
def api_add_Product():
    product_data = request.json
    return jsonify(insert_Product(product_data))

@app.route('/api/Product',  methods = ['PUT'])
def api_update_Product():
    Product_data = request.get_json()
    return jsonify(update_Product(Product_data))
# For Orders Table
@app.route('/api/Order', methods=['GET'])
def api_get_Orders():
    return jsonify(get_Orders())

@app.route('/api/Order/<OrderID>', methods=['GET'])
def api_get_Order(OrderID):
    return jsonify(get_Order_by_id(OrderID))

@app.route('/api/Order',  methods = ['POST'])
def api_add_Order():
    Order_data = request.json
    return jsonify(insert_Orders(Order_data))

@app.route('/api/Order',  methods = ['PUT'])
def api_update_Order():
    Order_data = request.get_json()
    return jsonify(update_Order(Order_data))

# @app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
# def api_delete_user(user_id):
#     return jsonify(delete_user(user_id))

if __name__ == "__main__":
    #app.debug = True
    app.run(debug=True)
>>>>>>> faecfc5bd35e0c9e68f76409f8510f35eb5885e9
    