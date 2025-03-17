import json
import pandas as pd

# 读取 Excel 文件
song_df = pd.read_excel('./music.xlsx')
# 将所有列转换为 object 类型，然后用 None 替换 NaN
song_df = song_df.astype(object).where(pd.notnull(song_df), None)

song_list = []
for index, row in song_df.iterrows():
    song_data = {
        "index": index,
        "song_name": row.iloc[0],
        "artist": row.iloc[1],
        "language": row.iloc[2],
        "remarks": row.iloc[3],
        "initial": row.iloc[4],
        "sticky_top": row.iloc[5],
        "paid": row.iloc[6],
        "BVID": row.iloc[7]
    }
    if row.iloc[5] == 1:
        song_list.insert(0, song_data)
    else:
        song_list.append(song_data)

with open("../public/music_list.json", 'w', encoding='utf-8') as f:
    json.dump(song_list, f, ensure_ascii=False, indent=2)
