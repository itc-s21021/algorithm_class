data = ["oota", "9", "takazato", "asahi", "4", "五", "水", "nagamine", "愛", "日本", "夜露死苦", "okuto", "みやざと", "漢字", "文", "akamine", "oomasu", "ぷよぷよ", "hiyane"]
print(data, "元のデータ")

for i in range(0, 18):
    m = i
    for j in range(i+1, 19):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]
    print(data, i+1)
print(data, "ソートのデータ")