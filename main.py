import pandas as pd
import pathlib as pl

currentPath = pl.Path().resolve()
print(str(currentPath) + '\\World Bank Indicators.xlsx')
file = pd.read_excel(str(currentPath) + '\\World Bank Indicators.xlsx')

print(file.head(1)['Population: Total (count)'])