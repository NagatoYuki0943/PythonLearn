import yagmail  # pip install yagmail
import ruamel.yaml as ryaml


# 设置SMTP服务器
smtp_server = "smtp.qq.com"
port = 587  # 465, 587
# 端口465和587在电子邮件发送中有一些重要的区别:
# 加密方式:
#     端口465使用隐式TLS/SSL加密,在连接建立时就开始加密。
#     端口587使用STARTTLS命令,先建立非加密连接,然后升级到TLS加密。
# 标准化状态:
#     端口465最初被指定用于SMTPS,但后来被废弃。
#     端口587是IETF标准化的邮件提交端口,被广泛推荐使用。
# 使用场景:
#     端口465主要用于需要立即加密的场景,或支持旧版客户端。
#     端口587更适合现代邮件基础设施,提供更灵活的加密选项。
# 兼容性:
#     端口587与现代邮件系统和客户端有更好的兼容性。
#     一些旧的邮件客户端可能仍默认使用端口465。
# 安全性:
#     两个端口都可以提供安全的加密传输。
#     端口587通过STARTTLS提供更灵活的安全升级选项。
# 推荐使用:
#     目前大多数邮件服务提供商和专家推荐使用端口587。
#     除非有特殊需求,否则应优先选择端口587。


# 发送邮件
def send_email(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
):
    try:
        yag = yagmail.SMTP(
            user=sender_email,
            password=sender_password,
            host=smtp_server,
            port=port,
            smtp_starttls=True,
            smtp_ssl=False,
        )
        contents = [body]
        yag.send(recipient_email, subject, contents, attachments=None)

        print("邮件已成功发送！")

    except yagmail.YagConnectionClosed as e:
        print(f"发生连接错误: {e}")

    except yagmail.YagAddressError as e:
        print(f"发生地址错误: {e}")

    except Exception as e:
        print(f"发生错误: {e}")

    else:
        print("SMTP 会话已成功关闭")

    finally:
        print("邮件发送操作完成")


def main():
    # 读取配置文件
    with open("email.yaml", "r", encoding="utf-8") as f:
        yaml = ryaml.YAML(typ="safe")
        config = yaml.load(f)

    email1 = config["email1"]
    email2 = config["email2"]
    email3 = config["email3"]

    send_email(
        email1["username"],
        email1["password"],
        email2["username"],
        "测试邮件",
        "这是一封测试邮件",
    )

    send_email(
        email1["username"],
        email1["password"],
        email3["username"],
        "测试邮件",
        "这是一封测试邮件",
    )


# 邮件已成功发送！
# SMTP 会话已成功关闭
# 邮件发送操作完成
# 邮件已成功发送！
# SMTP 会话已成功关闭
# 邮件发送操作完成


if __name__ == "__main__":
    main()
