# Sales Data Pipeline

A small end-to-end data pipeline built with Python, pandas and SQLite. It reads raw sales data, cleans it, joins two tables, saves the result into a database, and draws a chart.

## What it does
1. **Extract:** reads `customers.csv` and `orders.csv`
2. **Clean:** removes duplicate orders, fills blank amounts with 0, and fixes inconsistent city names (for example `bangalore` becomes `Bangalore`)
3. **Join:** combines orders with customer details using a left join on `customer_id`
4. **Load:** saves the joined table into a SQLite database (`sales.db`, table `sales_report`)
5. **Visualize:** draws a bar chart of total sales by city

## Problems in the raw data, and how the pipeline handles them
| Problem | How it's handled |
|---|---|
| Order 102 appears twice | Duplicate removed |
| Order 105 has no amount | Filled with 0 (an assumption for this practice project) |
| One city is written in lowercase | Standardised to title case |
| Order 104 belongs to a customer who isn't in the customers file | A left join keeps it, and the chart shows it as "Unknown" instead of dropping it silently |

## Example result
Total sales by city, read back from the database with SQL:

| city | total |
|---|---|
| Chennai | 210.0 |
| Unknown (no matching customer) | 120.0 |
| Bangalore | 50.0 |
| Hyderabad | 0.0 |

The chart is saved in `Output/sales_by_city.png`.

## Project structure
- `Code/pipeline.py`: the pipeline, with one function for each step
- `Data/customers.csv` and `Data/orders.csv`: the raw input data
- `Output/sales_by_city.png`: the chart the pipeline makes

## How to run
1. Install Python, then install the tools with `pip install pandas matplotlib`
2. Copy `customers.csv` and `orders.csv` into the same folder as `pipeline.py`
3. Run `python pipeline.py`
4. Close the chart window when it appears

The database file `sales.db` is created when the pipeline runs. It isn't included in this repository.

## Tools used
Python, pandas, SQLite, matplotlib

## Author
Vinay Simha M K
