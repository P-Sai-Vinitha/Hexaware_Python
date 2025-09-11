from order_management import OrderManagementDB

db = OrderManagementDB()

db.add_customer("Neethu", "neethu@gmail.com")
db.add_customer("Vinitha", "vinitha@gmail.com")

db.add_product("Laptop", 50000, 10)
db.add_product("Mouse", 500, 50)

order_id = db.place_order(1, [(1, 2), (2, 1)], "2025-09-11")

db.generate_invoice(order_id)

db.view_order_history(1)

db.sales_report("2025-09-10", "2025-09-12")
