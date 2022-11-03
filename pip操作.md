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

## help

```shell
> pip --help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to
                              stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL
                              Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```



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

# pipdeptree查看包依赖

> 安装

```shell
pip install pipdeptree
```

> 使用 pipdeptree 查看 torch 依赖结构

```shell
pipdeptree -p torch
```

> 查看本机python已存在的全部包的依赖结构

```shell
pipdeptree
```

> 查看哪些包依赖 torch

```shell
pipdeptree -p torch -r
```

