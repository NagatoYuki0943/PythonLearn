import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


# 创建邮件内容
def create_email(
    sender_email: str, recipient_email: str, subject: str, body: str
) -> str:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, "plain"))  # 'plain' 可替换为 'html' 发送HTML格式邮件

    return msg.as_string()


# 发送邮件
def send_email(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
):
    # 创建邮件内容
    message = create_email(sender_email, recipient_email, subject, body)

    try:
        # 连接到SMTP服务器并发送邮件
        # with smtplib.SMTP_SSL(smtp_server, port) as server: # SSL 加密
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # 启用TLS加密
            server.login(sender_email, sender_password)  # 登录到邮箱账户
            server.sendmail(sender_email, recipient_email, message)  # 发送邮件

        print("邮件已成功发送！")

    except smtplib.SMTPException as e:
        print(f"发生 SMTP 错误: {e}")

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


# 发送成功, 但是仍然有如下报错
# 邮件发送失败！ (-1, b'\x00\x00\x00')
# 邮件发送操作完成
# 邮件发送失败！ (-1, b'\x00\x00\x00')
# 邮件发送操作完成


if __name__ == "__main__":
    main()
