from config import get_connection
from mysql.connector import Error

class OrderManagementDB:
    def add_customer(self, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO customers (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            print(f"Customer {name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_product(self, product_name, price, stock):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)",
                (product_name, price, stock)
            )
            conn.commit()
            print(f"Product {product_name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def place_order(self, customer_id, items, order_date):
        """
        items = [(product_id, quantity), ...]
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            total_amount = 0.0
            order_items_data = []

            conn.start_transaction()

            for product_id, qty in items:
                cursor.execute("SELECT price, stock FROM products WHERE product_id = %s", (product_id,))
                result = cursor.fetchone()
                if not result:
                    raise Exception(f"Invalid product ID: {product_id}")
                price, stock = result
                if stock < qty:
                    raise Exception(f"Insufficient stock for product {product_id}")
                total_amount += price * qty
                order_items_data.append((product_id, qty, price))

                cursor.execute("UPDATE products SET stock = stock - %s WHERE product_id = %s", (qty, product_id))

            cursor.execute(
                "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)",
                (customer_id, order_date, total_amount)
            )
            order_id = cursor.lastrowid

            for product_id, qty, price in order_items_data:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)",
                    (order_id, product_id, qty, price)
                )

            conn.commit()
            print(f"Order {order_id} placed successfully. Total: {total_amount}")
            return order_id
        except Exception as e:
            conn.rollback()
            print(f"Order failed: {e}")
        finally:
            cursor.close()
            conn.close()

    def generate_invoice(self, order_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.order_id, o.order_date, c.name, c.email, o.total_amount
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                WHERE o.order_id = %s
            """, (order_id,))
            order = cursor.fetchone()

            cursor.execute("""
                SELECT p.product_name, oi.quantity, oi.item_price
                FROM order_items oi
                JOIN products p ON oi.product_id = p.product_id
                WHERE oi.order_id = %s
            """, (order_id,))
            items = cursor.fetchall()

            print("Invoice:")
            print(order)
            for item in items:
                print(item)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def view_order_history(self, customer_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.order_id, o.order_date, o.total_amount
                FROM orders o
                WHERE o.customer_id = %s
            """, (customer_id,))
            rows = cursor.fetchall()
            print(f"Order history for customer {customer_id}:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def sales_report(self, start_date, end_date):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT order_date, SUM(total_amount) 
                FROM orders
                WHERE order_date BETWEEN %s AND %s
                GROUP BY order_date
            """, (start_date, end_date))
            rows = cursor.fetchall()
            print("Sales Report:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
