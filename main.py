import sql_data
import numpy as np
import pandas as pd

# sql = sql_data.Postgre()
#
# sql.labsoft.to_csv(r'C:\Users\Vita\OneDrive - VITA PARTERS CONSULTORIA E INVESTIMENTOS LTDA - ME\Python projects\auto_risco\labsoft.csv')
# sql.labprog.to_csv(r'C:\Users\Vita\OneDrive - VITA PARTERS CONSULTORIA E INVESTIMENTOS LTDA - ME\Python projects\auto_risco\labprog.csv')


labsoft = pd.read_csv(r'C:\Users\Vita\OneDrive - VITA PARTERS CONSULTORIA E INVESTIMENTOS LTDA - ME\Python projects\auto_risco\labsoft.csv',index_col=[0])
labprog = pd.read_csv(r'C:\Users\Vita\OneDrive - VITA PARTERS CONSULTORIA E INVESTIMENTOS LTDA - ME\Python projects\auto_risco\labprog.csv',index_col=[0])
print(labsoft)


final_df = (labsoft.assign(day_of_week=labsoft.index.dayofweek
                               , year=labsoft.index.year
                               , month=labsoft.index.month
                               , day=labsoft.index.day
                               , day_of_year=labsoft.index.dayofyear
                               , hour=labsoft.index.hour
                               , hour_x=np.sin(2. * np.pi * labsoft.index.hour / 24.)
                               , hour_y=np.cos(2 * np.pi * labsoft.index.hour / 24.)
                               , day_of_year_x=np.sin(2. * np.pi * labsoft.index.dayofyear / 365.)
                               , day_of_year_y=np.cos(2. * np.pi * labsoft.index.dayofyear / 365.)
                               )
                )

print(final_df)