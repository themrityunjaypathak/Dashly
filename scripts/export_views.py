# ---------------- Loading Python Packages ---------------- 

# Importing Libraries
import os
import sys
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine

# ---------------- Configuration ---------------- 

# Setting up Logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, "export_views.log")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[
                        logging.FileHandler(log_file, mode="a"),
                        logging.StreamHandler()
                    ])

# Adding utils to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Loading Environment File
load_dotenv()

# Loading Database Credentials from Environment File
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Creating SQLAlchemy Engine to upload the Data to Neon PostgreSQL Database
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?sslmode=require&channel_binding=require", pool_pre_ping=True)
logging.info("SQLAlchemy Engine created successfully")

# ---------------- Exporting Views as CSV Files ---------------- 

# List of Views to Export
views = ["segment_wise_sales_and_profit",
         "region_wise_sales_and_profit",
         "month_wise_sales_and_profit",
         "top_customers_by_sales",
         "shipping_performance",
         "overall_sales_performance",
         "state_wise_sales_and_customer_base",
         "segment_wise_monthly_sales_and_profit",
         "region_wise_monthly_sales",
         "overall_customers_performance",
         "avg_discount_per_order_per_customer",
         "category_wise_monthly_sales_and_profit",
         "sub_category_wise_sales_and_profit",
         "category_wise_sales_profit_and_orders",
         "state_wise_most_purchased_sub_category"
        ]

# Exporting SQL Views as CSV Files
from utils.export_views import export_views_as_csv
export_views_as_csv(views, engine)
logging.info("Views exported as CSVs successfully")