from importlib.metadata import distributions

# 打印所有安装包的名称和版本
for dist in distributions():
    print(f"{dist.metadata["Name"]} ({dist.version})")
