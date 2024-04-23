import pandas as pd 
from sqlalchemy import create_engine

conne_str = 'postgresql://postgres:1234@localhost/pizzahouse'
db = create_engine(conne_str)
connec = db.connect()

df = pd.read_csv('/Users/Akku/Desktop/SqlPizzaProject/pizzatypes.csv')
df.to_sql('pizzatypess', con=connec, if_exists='replace', index=False)
