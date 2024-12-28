import pandas as pd
import pathlib as pl
from Models.Model import ModelClass

currentPath = pl.Path().resolve()
print(str(currentPath) + '\\Content\\World Bank Indicators.xlsx')
file = pd.read_excel(str(currentPath) + '\\Content\\World Bank Indicators.xlsx')

modelInstance = []
slNo = 0
for _, row in file.tail(5).iterrows():
    model = ModelClass(
        slNo=slNo + 1,
        countryName = row.get("Country Name"),
        date = row.get("Date"),
        mobileSubs = row.get("Business: Mobile phone subscribers"),
        internetSubs = row.get("Business: Internet users (per 100 people)")
    )
    print(_)
    modelInstance.append(model)

for row in modelInstance:
    print(row)
