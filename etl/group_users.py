import pandas as pd
import argparse
import os
import logging
from sqlalchemy import create_engine
from datetime import datetime


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


parser = argparse.ArgumentParser(description="Group users by bank, company, and pincode")
parser.add_argument("--db-uri", required=True, help="Database connection string")
parser.add_argument("--output-dir", default="etl/output", help="where to save output csvs")
args = parser.parse_args()


engine = create_engine(args.db_uri)
logging.info("Db connection is established...")


query = """
select 
    u.id as user_id,
    u.first_name,
    u.last_name,
    u.pincode,
    e.company_name,
    b.bank_name
from users u
join employment_info e on u.id = e.user_id
join user_bank_info b on u.id = b.user_id;
"""

df = pd.read_sql(query, engine)
logging.info(f"Total rows fetched: {len(df)}")


if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
    logging.info(f"Created folder: {args.output_dir}")

ts = datetime.now().strftime("%Y%m%d_%H%M%S")


def group_and_save(data, col, file_prefix):
    grouped = data.groupby(col).agg(user_count=('user_id', 'count'), user_ids=('user_id', lambda x: ','.join(map(str, x)))).reset_index()
    
    output_file = os.path.join(args.output_dir, f"{file_prefix}_{ts}.csv")
    grouped.to_csv(output_file, index=False)
    logging.info(f"Saved -> {output_file}")


group_and_save(df, "bank_name", "by_bank")
group_and_save(df, "company_name", "by_company")
group_and_save(df, "pincode", "by_pincode")

logging.info("ETL completed")
