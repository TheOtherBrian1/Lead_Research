import pandas as pd
from sqlalchemy import create_engine
from private_info import postgreSQL_credentials, data_path

covid_data = pd.read_csv(data_path)

engine = create_engine(
    f'postgresql://postgres:{postgreSQL_credentials}@localhost:5432/covid_data')

covid_data.to_sql(
    'covid_death_figures',
    engine
)
