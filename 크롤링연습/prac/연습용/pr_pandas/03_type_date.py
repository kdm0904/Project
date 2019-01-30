import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./naverKeywordResult.json")
print(df.count())

print(df['postdate'])

df['postdate'] = pd.to_datetime(df['postdate'], format="%Y%m%d")
df = df.head(100)

# 1월
dfUpperJan = df[df['postdate'] >= "2018-01-01"]
print(dfUpperJan.count())

dfJan = df[(df['postdate'] >= "2018-01-01") & (df['postdate'] <= "2018-01-31")]
dfFeb = df[(df['postdate'] >= "2018-02-01") & (df['postdate'] <= "2018-02-28")]
dfMar = df[(df['postdate'] >= "2018-03-01") & (df['postdate'] <= "2018-03-31")]
print(dfJan.count())
print(dfFeb.count())
print(dfMar.count())

print(df['postdate'].min())
print(df['postdate'].max())
