import pandas as p

data = p.read_csv("central_park_data.csv")

gre_cnt = len(data[data["Primary Fur Color"] == "Gray"])
cin_cnt = len(data[data["Primary Fur Color"] == "Cinnamon"])
blk_cnt = len(data[data["Primary Fur Color"] == "Black"])

d_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gre_cnt, cin_cnt, blk_cnt]
}

df_count = p.DataFrame(d_dict)
df_count.to_csv("Fur_color_count.csv")
print(df_count)