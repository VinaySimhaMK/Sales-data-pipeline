import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


def extract():
    customers = pd.read_csv("customers.csv")
    orders = pd.read_csv("orders.csv")
    return customers, orders


def clean(customers, orders):
    orders = orders.drop_duplicates().copy()
    orders["amount"] = orders["amount"].fillna(0)
    customers["city"] = customers["city"].str.title()
    return customers, orders


def join(customers, orders):
    joined = pd.merge(orders, customers, on="customer_id", how="left")
    return joined


def load(joined):
    conn = sqlite3.connect("sales.db")
    joined.to_sql("sales_report", conn, if_exists="replace", index=False)
    conn.close()
    print("Saved to sales.db")

def visualize(joined):
    report = joined.copy()
    report["city"] = report["city"].fillna("Unknown")
    totals = report.groupby("city")["amount"].sum().sort_values(ascending=False)

    totals.plot(kind = "bar")
    plt.title("Total Sales by City")
    plt.ylabel("Total")
    plt.tight_layout()
    plt.savefig("sales_by_city.png")
    plt.show()

def check_db():
    conn = sqlite3.connect("sales.db")
    query = """SELECT city, SUM(amount) AS total
    FROM sales_report
    GROUP BY city
    ORDER BY total DESC"""
    print(pd.read_sql(query, conn))
    conn.close()

def main():
    customers, orders = extract()
    customers, orders = clean(customers, orders)
    joined = join(customers, orders)
    load(joined)
    check_db()
    visualize(joined)

main()
