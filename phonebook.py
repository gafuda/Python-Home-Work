import pandas as pd
def readDB():
    return pd.read_json("phonebook.json")

def exportDF(type, df):
    match type:
        case "1":
            df.to_csv("output.csv", index=False)
        case "2":
            df.to_excel("output.xlsx", index=False)

def importDF(type, df):
    df2 = None
    match type:
        case "1":
            df2 = pd.read_csv("input.csv", index_col=False)
        case "2":
            df2 = pd.read_excel("input.xlsx", index_col=False)
    frames = [df, df2]
    result = pd.concat(frames)
    result = result.drop_duplicates(subset=['phone'])
    result = result.set_index('id')
    result.to_json("phonebook.json", orient="records")

if __name__ == "__main__":
    df = readDB()
    print("Для экспорта введите 1, для импорта введите 2")
    type = input()
    print("Выбор типа экспорта: csv - 1, excel - 2")
    type2 = input()
    if type == "1":
        exportDF (type2, df)
    if type == "2":
        importDF (type2, df)
