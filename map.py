import pandas as pd
import requests
import json

# 替换为您的API密钥
api_key = "AIzaSyDml69VgJcbPLQB6y-h6TZr1_foREj8po0"

# 读取Excel文件中的地址数据
df = pd.read_excel("addresses.xlsx")

# 获取出发地址和到达地址列表
origins = df["Origin"].tolist()
destinations = df["Destination"].tolist()

# 创建一个空的列表来存储结果
result = []

# 计算每对地址之间的距离
for i in range(len(origins)):
    origin = origins[i]
    destination = destinations[i]

    # 构建URL
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}"

    # 发送GET请求
    response = requests.get(url)

    # 解析响应
    data = json.loads(response.text)

    # 检查响应中是否包含距离信息
    if "distance" in data["rows"][0]["elements"][0]:
        # 获取距离信息
        distance = data["rows"][0]["elements"][0]["distance"]["text"]

        # 将结果添加到列表中
        result.append([origin, destination, distance])
    else:
        # 输出错误消息和完整的响应数据
        print(f"无法计算从 {origin} 到 {destination} 的距离")
        print(json.dumps(data, indent=4))

# 将列表转换为DataFrame
result = pd.DataFrame(result, columns=["Origin", "Destination", "Distance"])

# 将结果保存到新的Excel文件中
result.to_excel("distances.xlsx", index=False)
