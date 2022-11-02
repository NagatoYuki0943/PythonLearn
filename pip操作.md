# 配置文件位置

```shell
C:\Users\Frostbite\AppData\Roaming\pip\pip.ini
```

# pypi 镜像使用帮助

> 临时使用

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

> 设为默认

```shell
python -m pip install --user --upgrade pip  #更新pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

# pip命令

## 安装

```shell
pip install  numpy

pip install -r requirements.txt # 按照requirements.txt中全部文件

pip install 本地whl文件
```

## 列出所有的安装包

```shell
pip list
```

## 查看已安装的包

```shell
pip show packagename
```

## 检测更新

```shell
pip list --outdated
```

## 升级包

```shell
pip list --outdated
```

## 升级包

```shell
pip install --upgrade packagename
```

## 卸载包

```shell
pip uninstall packagename
```

## 更新pip

```shell
python -m pip install --upgrade pip
```

# 缓存位置

```shell
C:\Users\Frostbite\AppData\Local\pip\cache
```





# 注意

## pywin32 不能更新，否则没法使用conda

# 错误

## No module named 'pip'错误

> 解决方式 `python -m ensurepip`
>
> `C:\Users\Frostbite\AppData\Roaming\Python\Python38\site-packages` 中的pip删除即可避免错误