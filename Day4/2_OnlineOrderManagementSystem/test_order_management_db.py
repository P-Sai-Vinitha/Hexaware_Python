import inspect
import order_management

def test_add_customer_query():
    db = order_management.OrderManagementDB()
    expected_query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_customer)
    assert expected_query in actual_query

def test_add_product_query():
    db = order_management.OrderManagementDB()
    expected_query = "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(db.add_product)
    assert expected_query in actual_query

def test_place_order_insert_order():
    db = order_management.OrderManagementDB()
    expected_query = "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)"
    actual_query = inspect.getsource(db.place_order)
    assert expected_query in actual_query

def test_insert_order_items_query():
    db = order_management.OrderManagementDB()
    expected_query = "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)"
    actual_query = inspect.getsource(db.place_order)
    assert expected_query in actual_query

def test_generate_invoice_query():
    db = order_management.OrderManagementDB()
    expected_query = "SELECT o.order_id, o.order_date, c.name, c.email, o.total_amount"
    actual_query = inspect.getsource(db.generate_invoice)
    assert expected_query in actual_query

def test_view_order_history_query():
    db = order_management.OrderManagementDB()
    expected_query = "SELECT o.order_id, o.order_date, o.total_amount"
    actual_query = inspect.getsource(db.view_order_history)
    assert expected_query in actual_query

def test_sales_report_query():
    db = order_management.OrderManagementDB()
    expected_query = "SELECT order_date, SUM(total_amount)"
    actual_query = inspect.getsource(db.sales_report)
    assert expected_query in actual_query

# --- Method signature tests ---
def test_add_customer_signature():
    sig = inspect.signature(order_management.OrderManagementDB.add_customer)
    assert list(sig.parameters.keys()) == ["self", "name", "email"]

def test_add_product_signature():
    sig = inspect.signature(order_management.OrderManagementDB.add_product)
    assert list(sig.parameters.keys()) == ["self", "product_name", "price", "stock"]

def test_place_order_signature():
    sig = inspect.signature(order_management.OrderManagementDB.place_order)
    assert list(sig.parameters.keys()) == ["self", "customer_id", "items", "order_date"]

def test_generate_invoice_signature():
    sig = inspect.signature(order_management.OrderManagementDB.generate_invoice)
    assert list(sig.parameters.keys()) == ["self", "order_id"]

def test_view_order_history_signature():
    sig = inspect.signature(order_management.OrderManagementDB.view_order_history)
    assert list(sig.parameters.keys()) == ["self", "customer_id"]

def test_sales_report_signature():
    sig = inspect.signature(order_management.OrderManagementDB.sales_report)
    assert list(sig.parameters.keys()) == ["self", "start_date", "end_date"]
