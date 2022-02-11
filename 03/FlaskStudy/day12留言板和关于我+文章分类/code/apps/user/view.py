'''
用户控制器
使用模板继承

ajax手机号
cookie session
'''

from operator import or_
import re
from flask import Blueprint, url_for, request, session, jsonify, Response, g  # g 本次请求的一个对象
from flask.templating import render_template
import requests
from werkzeug.utils import redirect
from apps.utils import SmsSendAPIDemo
from apps.user.models import User, Photo, Aboutme, MessageBoard
from apps.article.models import Article, ArticleType
from werkzeug.utils import secure_filename #  安全文件名 去除空格和特殊符号
from exts import db
from werkzeug.security import generate_password_hash, check_password_hash    # 加密,解密密码
from sqlalchemy import or_, and_, not_
from datetime import datetime, timedelta
import random
from settings import Config
import os


# url_prefix 是url前缀,必须有 '/'
# 作用是 127.0.0.2:5000/user 加上自己的路由
user_bp = Blueprint(name='user', import_name=__name__, url_prefix='/user')


# 需要登录的path列表,注意有 /user
required_login_list = [
                    '/user/center',
                    '/user/update',
                    '/user/upphoto',
                    '/user/delphoto',
                    '/user/addaboutme',
                    '/user/aboutme',
                    '/article/publish',
                    '/article/comment',
                        ]


# 钩子函数
# 第一次被请求调用
@user_bp.before_app_first_request   # 蓝图的方法中有app, app自身的不用再加上app
def first_request():
    #print('before_app_first_request')
    pass


# 每次请求之前调用
@user_bp.before_app_request
def before_request():
    # 得到请求路径
    path = request.path
    # print(path) # /user/
    if path in required_login_list:
        # id = request.cookies.get('uid', None)
        id = session.get('uid', None)
        # 没有登录
        if not id:
            return redirect(url_for('user.login'))
        else:
            user = User.query.get(id)
            # 放在本次请求的对象中
            g.user = user


# 每次请求之后调用,对response做处理
@user_bp.after_app_request
def after_request(response: Response): # 参数必须有response,因为前面的函数会传递过来
    # 处理response
    # response.set_cookie('a', 'test', 60)
    return response


# 在after之后,也有参数
@user_bp.teardown_app_request
def teardown_app_request(response: Response):
    print('teardown_app_request')
    return response


# 自定义模板过滤器
@user_bp.app_template_filter('cdecode')
def cdecode(content):
    '''
    将blob转换为文本
    '''
    return content.decode('utf-8')


# 首页,获取cookie,session
@user_bp.route('/')
def index():
    # 接收页码数,默认为1
    page = int(request.args.get('page', 1))

    # 获取文章和类型列表 倒叙                                           页数       每页数量
    pagination = Article.query.order_by(-Article.pdatetime).paginate(page=page, per_page=3)
    # print(pagination)   # flask_sqlalchemy.Pagination object at 0x000001DD8A59C190>
    # print(pagination.items)     # [<Article 7>, <Article 5>, <Article 4>]
    # print(pagination.total)     # 8  总数
    # print(pagination.pages)     # 3  总页数
    # print(pagination.page)      # 2  当前页数
    # print(pagination.has_prev)  # True  是否有上一页
    # print(pagination.prev_num)  # 1     前一页页码
    # print(pagination.has_next)  # Ture  是否有下一页
    # print(pagination.next_num)  # 3     前一页页码

    types = ArticleType.query.all()

    # 1.获取cookie,也是字典格式,可以设置默认值
    # uid = request.cookies.get('uid', None)
    # 2.session方式 字典格式
    uid = session.get('uid', None)

    # 判断用户是否登录
    if uid:
        user = User.query.get(uid)
        return render_template('user/index.html', user=user, pagination=pagination, types=types)
    else:
        return render_template('user/index.html', pagination=pagination, types=types)


# ajax手机号唯一
@user_bp.route('/checkphone', methods=['GET','POST'])
def checkphone():
    phone = request.args.get('phone')
    # 是否存在
    user = User.query.filter(User.isdelete==False, User.phone==phone).all()
    if user:
        return {'code':1, 'msg':'号码已经被注册'}
    else:
        return {'code':0, 'msg':'号码可以使用'}


# 注册
@user_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html', user=None) # 必需传递用户,不然报错
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        # 与模型结合
        # 1. 找到模型类并创建对象
        user = User()
        # 2. 给对象的属性赋值
        user.username = username
        user.phone = phone
        user.email = email
        if password == repassword:
            # user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()    # hexdigest() 转换为字符串

            # 密码格式 pbkdf2:sha256$salt$hash
            user.password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)    # 这个方法也能加密
            # return user.password # pbkdf2:sha256:260000$0mNOkiQR$f4d7d4bfcd2059faec0a0b4274470b73981b471e40f94adba841dcf6203fd7dd
            # 添加
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit()
            return redirect(url_for('user.index')) # url_for()里面填写的是 Blueprint + func名字
        else:
            return render_template('user/register.html', msg='两次密码不同', user=user)


# 登录,添加cookie
@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        # 查询
        # user_list = User.query.filter(username==username).all()
        user_list = User.query.filter(User.username==username).all()
        # print(user_list) # 用户对象列表
        for user in user_list:
            # user就是每一个用户对象
            # 参数1: 经过加密的密码
            # 参数2: 字符串
            # return: True/False
            res = check_password_hash(pwhash=user.password, password=password)
            if res:
                # # 1.cookie
                # response = redirect(url_for('user.index'))
                # # 设置cookie
                # # key value 最大时长 默认情况是尽可能的长
                # # key,value必须为str
                # # 或者使用 expires: 过期时间 expires=datetime.now()+timedelta(hour=1)
                # response.set_cookie(key='uid', value=str(user.id), max_age=3600)
                # return response

                # 2.session 字典的使用方式
                session['uid'] = user.id
                return redirect(url_for('user.index'))
        else:
            return render_template('user/login.html', msg="账户或密码错误", username=username)


# ajax发送短信息
@user_bp.route('/sendmsg')
def sendmsg():
    SECRET_ID = "ef8a1e23fc76790c80c97bf6134a75a2"      # 产品密钥ID，产品标识
    SECRET_KEY = "f951ca65d2437d4432a8e0a4c9183e91"     # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "98d06d9b06ba49d68f38cbb5c453299f"    # 业务ID，易盾根据产品业务特点分配
    api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)

    phone = request.args.get('phone')

    # 验证用户是否注册
    user = User.query.filter(User.phone==phone ).first()
    if not user:
        return jsonify(code=401, msg='手机号未注册')

    params = {
        "mobile": phone,
        "templateId": "10084",
        "paramType": "json",
        "params": "json格式字符串.要自己替换掉 "
    }
    # 发送短息验证码
    res = api.send(params)

    session[phone] = 123456
    return jsonify(code=200, msg='短信发送成功')

    # 下面没法使用,所以使用上面的代替
    if res is not None:
        if res["code"] == 200:
            taskId = res["result"]["taskId"]
            print("taskId = %s" % taskId)

            # 保存在session
            session[phone] = 241036
            # 返回json对象
            return jsonify(code=200, msg='短信发送成功')
        else:
            print("ERROR: ret.code=%s,msg=%s" % (res['code'], res['msg']))
            return jsonify(code=400, msg='短信发送失败')


# 接收验证码登录
@user_bp.route('/phonelogin', methods=['GET','POST'])
def phonelogin():
    phone = request.form.get('phone')
    code = request.form.get('code')
    print(type(code))               # str
    print(type(session.get(phone))) # int

    if eval(code) == session.get(phone):
        user = User.query.filter(User.phone==phone).first()
        if user:
            # 登录成功
            del session[phone]
            session['uid'] = user.id
            return redirect(url_for('user.index'))
        else:
            # 登录失败
            return render_template('user/login.html', msg="号码未注册", phone=phone)
    else:
        return render_template('user/login.html', msg="验证码错误", phone=phone)


# 退出登录,删除cookie
@user_bp.route('/logout')
def logout():
    response =  redirect(url_for('user.index'))
    # 1.删除cookie
    # response.delete_cookie(key='uid')
    # 2.删除session
    # del session['uid']
    session.clear()   # 清除全部session
    return response


# 用户中心
@user_bp.route('/center')
def center():
    # 查到所有类型
    types = ArticleType.query.all()
    # 图片 查询自己并且没删除的
    photos = Photo.query.filter(Photo.user_id==g.user.id, Photo.isdelete==False).all()
    # 留言 查询自己并且没删除的
    messages = MessageBoard.query.filter(MessageBoard.post_user_id==g.user.id, MessageBoard.isdelete==False).all()
    #                                               g是本次请求的对象,在before_app_request中获取了用户,这里不用在获取了
    return render_template('user/center.html', user=g.user, types=types, photos=photos, messages=messages)


# 允许的扩展名
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'bmp', 'gif']


# 更新数据
@user_bp.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        email = request.form.get('email')
        # files,要特殊处理
        icon = request.files.get('icon')
        # print('------>', icon)  # <FileStorage: '6CF818492B05295D6162467C6E351214.jpg' ('image/jpeg')>
        # FileStorage 属性
        # 属性: filename 获取file名字
        # 方法: save('保存路径')
        icon_name = icon.filename

        # 保存到数据库
        user = g.user
        user.username = username
        user.phone = phone
        user.email = email

        # 必须是图片格式,没有上传图片就不就修改
        if icon_name.split('.')[-1] in ALLOWED_EXTENSIONS:
            # 安全文件名 去除空格和特殊符号,会删除中文字符
            icon_name = secure_filename(icon_name)
            # 绝对路径
            file_path = os.path.join(Config.UPLOAD_ICON_DIR, icon_name)
            # 保存文件,save(路径)
            icon.save(file_path)
            user.icon = 'upload/icon/' + icon_name  # 保存到数据库使用相对路径

        db.session.commit()
    return redirect(url_for('user.center'))


#上传图片
@user_bp.route('/upphoto', methods=['GET', 'POST'])
def upphoto():
    photo = request.files.get('photo')
    photo_name = photo.filename
    # 必须是图片格式,没有上传图片就不就修改
    if photo_name.split('.')[-1] in ALLOWED_EXTENSIONS:
        # 随机名字
        r = str(random.randint(1, 99999))
        photo_name = r + photo_name
        # 绝对路径
        file_path = os.path.join(Config.UPLOAD_PHOTO_DIR, photo_name)
        # 保存文件,save(路径)
        photo.save(file_path)

        photo = Photo()
        # 实际存储路径
        photo.name = 'upload/photo/' + photo_name
        photo.user_id = session.get('uid')
        db.session.add(photo)
        db.session.commit()

    return redirect(url_for('user.center'))


# 软删除图片
@user_bp.route('/delphoto', methods=['GET', 'POST'])
def delphoto():
    photoid = request.args.get('id')

    photo = Photo.query.get(photoid)
    photo.isdelete = True   # 软删除
    db.session.commit()
    return {'code':200, 'msg': '删除成功'}


# 所有图片
@user_bp.route('/allphoto', methods=['GET', 'POST'])
def allphoto():
    # 接收页码数,默认为1
    page = int(request.args.get('page', 1))
    # 分页
    photos = Photo.query.paginate(page=page, per_page=2)
    user = None
    if session.get('uid'):
        user = User.query.get(session.get('uid'))
    return render_template('user/allphotos.html', photos=photos, user=user)


# 添加个人详情
@user_bp.route('addaboutme', methods=['GET', 'POST'])
def addaboutme():
    content = request.form.get('aboutme-content')
    # 添加
    aboutme = Aboutme()
    aboutme.user_id = g.user.id
    aboutme.content = content.encode('utf-8')   #content为 db.BLOB,要手动转换
    db.session.add(aboutme)
    db.session.commit()
    # 返回aboutme界面
    return redirect(url_for('user.aboutme'))


# 我的页面
@user_bp.route('aboutme', methods=['GET', 'POST'])
def aboutme():
    return render_template('user/aboutme.html', user=g.user)


# 添加,显示留言
@user_bp.route('message_board', methods=['GET', 'POST'])
def message_board():
    page = int(request.args.get('page', 1))
    # 获取用户
    uid = session.get('uid', None)
    user = None
    if uid:
        user = User.query.get(uid)

    if request.method == 'POST':
        message = request.form.get('message')
        # 添加
        message_board = MessageBoard()
        message_board.message = message
        # 有uid就添加,不然不添加,就是匿名用户
        if uid:
            message_board.post_user_id = uid
        db.session.add(message_board)
        db.session.commit()

    # 查询留言
    messages = MessageBoard.query.filter(MessageBoard.isdelete==False).order_by(-MessageBoard.mdatetime).paginate(page=page, per_page=2)
    return render_template('user/messageboard.html', user=user, messages=messages)


# 删除留言
@user_bp.route('delete_message', methods=['GET', 'POST'])
def delete_message():
    message_id = request.args.get('id')
    message_board= MessageBoard.query.get(message_id)
    message_board.isdelete = True
    db.session.commit()
    return {'code':200, 'msg': '删除成功'}

# 错误页面
@user_bp.route('error')
def error():
    referer = request.headers.get('Referer')
    return render_template('500.html', error_msg="错误", referer=referer)