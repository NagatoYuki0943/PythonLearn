"""https://kimi.moonshot.cn/chat/cp7j4i6bi7sbkj5c306g"""

import os


"""
设置临时变量

linux:
    # 不允许使用空格
    export HF_TOKEN="abcdefghijklmnopqrstuvwxyz"

powershell:
    # 设置一个简单的变量
    $HF_TOKEN = "abcdefghijklmnopqrstuvwxyz"

    # 设置环境变量
    $env:HF_TOKEN = "abcdefghijklmnopqrstuvwxyz"
"""


hf_token = os.getenv("HF_TOKEN", "")
print(hf_token)
# abcdefghijklmnopqrstuvwxyz
