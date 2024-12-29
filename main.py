import pandas as pd
import pathlib as pl
from docx import Document
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
    slNo = slNo + 1
    modelInstance.append(model)

# for row in modelInstance:
    # print(row.slNo)

doc = Document(str(currentPath) + "\\Templates\\World Bank Indicators.docx")
flag = 1
for modelRow in modelInstance:
    for table in doc.tables:
        if flag == 1:
            table._tbl.remove(table._tbl.tr_lst[1])
            flag = 0
        row = table.add_row()
        row.cells[0].text = str(modelRow.slNo)
        row.cells[1].text = modelRow.countryName
        row.cells[2].text = str(modelRow.date)
        row.cells[3].text = str(modelRow.mobileSubs)
        row.cells[4].text = str( modelRow.internetSubs)
        # table.add_row

doc.save(str(currentPath) + "\\Templates\\World Bank Indicators_test.docx")