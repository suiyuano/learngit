# coding=utf-8
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
import pymysql, time,datetime

pymysql.install_as_MySQLdb()

app = Flask(__name__)
"""
1. 配置数据库
    a.导入SQLALchemy扩展
    b.创建db对象, 并配置参数
    c.终端创建数据库
2. 添加作者和书模型(类)
    a.模型继承自db.Model
    b.__tablename__:表名
    c. db.Column:字段
    d. db.relationship:关系引用
3. 添加数据
4. 使用模板显示数据库查询到的数据
    a.查询所有的作者信息, 让信息传递给模板
    b.模板中按照格式, 依次for循环作者和书籍即可(通过作者获取书籍, 用的是关系引用)
5. 使用WTF显示表单 
    a.自定义表单类
    b.模板中显示
    c.设置secret_key
6. 实现相关的增删逻辑
    a.添加作者/书籍
    b.删除书籍: redirect(重定向)/url_for(指向路由)/for else  的使用.
    c.删除作者(要先删除该作者的书籍, 再删除该作者)
"""

# 配置数据库的地址URI , 格式 "数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名"  , 端口号可以不写.
# python3中用的mysql驱动是mysql-connector , 已经不支持python2的MySQLdb驱动.
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:2016141462167@127.0.0.1/books_demo?charset=utf8mb4"
# 跟踪数据库的修改 --> 不建议开启 , 一是消耗性能 , 二是未来的版本中会移除.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "hwhefsewljfejrlesjfl"  # 没设置secret_key会有报错提醒
# 将app作为参数传入这个关联工具 , 创建一个两者相关联对象db
db = SQLAlchemy(app)

current_user = ''


def log(*args, **kwargs):
    print('log: ', *args, **kwargs)


# 注意: web框架里面的模型类基本都是要继承自导入的模块中的某个父类 , 这样才会起到关联的作用.
# class Author(db.Model):
#     """创建作者子类"""
#     __tablename__ = "authors"  # 定义表名
#     # 定义字段
#     # db.Column表示是一个字段 , db.Integer就代表id这个字段的数据类型是整数 , primary_key代表主键(主关键字) , 是作为表的行的唯一标识.
#     # db.String代表是字符串类型 , 字符串长度定义个n个字节 , unique(唯一的) , unique=True代表这列不允许出现重复的值.
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)  # string的长度随便写个2的倍数就行了
#     # 在"一对多"的一中定义author_book属性 , 该属性不会出现在字段中 , 后面的backref="author"是给Book反向引用的
#     # 由于是"一对多" , 所以"多"的地方用Book参数 , "一"的地方用不加s的实例对象参数author.
#     author_book = db.relationship("Book", backref="author")
#
#     def __repr__(self):
#         """返回定制消息, 与__str__作用类似"""
#         return "Author: %d %s" % (self.id, self.name)


# class Book(db.Model):
#     """创建书籍子类"""
#     __tablename__ = "books"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))  # 表名.id 来建立外键关联
#
#     def __repr__(self):
#         return "Book: %d %s" % (self.id, self.name)

class Book(db.Model):
    """创建书籍类"""
    __tablename__ = "book"
    author = db.Column(db.String(10), nullable=False)
    pub_name = db.Column(db.String(20), nullable=False)
    bname = db.Column(db.String(20), nullable=False)
    pub_date = db.Column(db.String(10), nullable=False)
    bno = db.Column(db.Integer, nullable=False, primary_key=True)
    summary = db.Column(db.String(100), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    remain = db.Column(db.Integer, nullable=False)

    book_borrows = db.relationship('Borrow_info', backref='book')

    def __repr__(self):
        return "Book: 作者：{} 出版社：{} 书名：{} 出版日期：{} 书籍编号：{} 摘要：{} 馆藏数：{} 剩余：{}".format(self.author, self.pub_name,
                                                                                    self.bname, self.pub_date, self.bno,
                                                                                    self.summary, self.total,
                                                                                    self.remain)


class User(db.Model):
    """创建用户类"""
    __tablename__ = "user"
    udept = db.Column(db.String(20), nullable=False)
    ugrade = db.Column(db.String(10), nullable=False)
    uname = db.Column(db.String(10), nullable=False)
    usex = db.Column(db.String(4), nullable=False)
    uid = db.Column(db.String(20), nullable=False, primary_key=True)
    pswd = db.Column(db.String(20), nullable=False)
    uidenty = db.Column(db.Integer, nullable=False)

    user_borrows = db.relationship('Borrow_info', backref='user')

    def __repr__(self):
        return "User: 专业：{} 年级：{} 姓名：{} 性别：{} 学号：{} 密码：{} 身份：{} ".format(self.udept, self.ugrade, self.uname, self.usex,
                                                                         self.uid,
                                                                         self.pswd, self.uidenty)


class Borrow_info(db.Model):
    """创建借阅信息类"""
    __tablename__ = "borrow_info"
    # bno = db.Column(db.String(20), nullable=False, primary_key=True)
    borrow_id = db.Column(db.String(10), nullable=False, primary_key=True)
    bname = db.Column(db.String(10), nullable=False)
    borrow_date = db.Column(db.String(20), nullable=False)
    return_date = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.String(20), db.ForeignKey("user.uid"))  # 表名.id 来建立外键关联
    book_no = db.Column(db.Integer, db.ForeignKey("book.bno"))  # 表名.id 来建立外键关联

    def __repr__(self):
        return "Borrow_info: 借阅编号：{} 书名：{} 借书日期：{} 还书日期：{} 借书人学号：{} 书籍编号：{}".format(self.borrow_id, self.bname,
                                                                                    self.borrow_date, self.return_date,
                                                                                    self.user_id, self.book_no)


class TrueForm(FlaskForm):
    """表单扩展常用的模型(类)有三种: StringField, PasswordField,  SubmitField , 这里只用到两种
        然后传入参数并创建出各自的实例对象 , 以供其它地方使用.
    """
    author = StringField("作者", validators=[DataRequired()])
    book = StringField("书籍", validators=[DataRequired()])
    submit = SubmitField("添加")


class LoginForm(FlaskForm):
    username = StringField('用户名', render_kw={'placeholder': '学号'})
    password = PasswordField('密码', render_kw={'placeholder': '密码'})
    remember = BooleanField('记住我')
    submit = SubmitField('登陆')


class ReferBook(FlaskForm):
    author = StringField('作者', render_kw={'placeholder': '作者'})
    pub_name = StringField('出版社', render_kw={'placeholder': '出版社'})
    bname = StringField('书名', render_kw={'placeholder': '书名'})
    pub_date = StringField('出版日期', render_kw={'placeholder': '出版日期'})
    bno = StringField('书籍编号', render_kw={'placeholder': '书籍编号'})
    summary = StringField('摘要', render_kw={'placeholder': '摘要'})
    submit = SubmitField('查询')


class ReferUser(FlaskForm):
    udept = StringField('专业', render_kw={'placeholder': '专业'})
    ugrade = StringField('年级', render_kw={'placeholder': '年级'})
    uname = StringField('姓名', render_kw={'placeholder': '姓名'})
    usex = StringField('性别', render_kw={'placeholder': '性别'})
    uid = StringField('学号', render_kw={'placeholder': '学号'})
    # uidenty = StringField('身份')   默认注册普通用户
    submit = SubmitField('查询')


class UserForm(FlaskForm):
    udept = StringField('专业', validators=[DataRequired()], render_kw={'placeholder': '专业'})
    ugrade = StringField('年级', validators=[DataRequired()], render_kw={'placeholder': '年级'})
    uname = StringField('姓名', validators=[DataRequired()], render_kw={'placeholder': '姓名'})
    usex = StringField('性别', validators=[DataRequired()], render_kw={'placeholder': '性别'})
    uid = StringField('学号', validators=[DataRequired()], render_kw={'placeholder': '学号'})
    pswd = StringField('密码', validators=[DataRequired()], render_kw={'placeholder': '密码'})
    # uidenty = StringField('身份')   默认注册普通用户
    submit = SubmitField('确认修改')


class BookInfo(FlaskForm):
    author = StringField('作者', validators=[DataRequired()], render_kw={'placeholder': '作者'})
    pub_name = StringField('出版社', validators=[DataRequired()], render_kw={'placeholder': '出版社'})
    bname = StringField('书名', validators=[DataRequired()], render_kw={'placeholder': '书名'})
    pub_date = StringField('出版日期', validators=[DataRequired()], render_kw={'placeholder': '出版日期'})
    # bno = StringField('书籍编号', validators=[DataRequired()],render_kw={'placeholder': '书籍编号'})
    summary = StringField('摘要', validators=[DataRequired()], render_kw={'placeholder': '摘要'})
    total = StringField('馆藏数', validators=[DataRequired()], render_kw={'placeholder': '馆藏数'})
    remain = StringField('剩余', validators=[DataRequired()], render_kw={'placeholder': '剩余'})
    submit = SubmitField('确认修改书籍信息！')


class BorrowForm(FlaskForm):
    user = StringField('学号', validators=[DataRequired()], render_kw={'placeholder': '学号'})
    book_name = StringField('书名', render_kw={'placeholder': '书名'})
    book_id = StringField('书名', render_kw={'placeholder': '书籍编号'})
    submit = SubmitField('借书')


class ReturnForm(FlaskForm):
    user = StringField('学号', validators=[DataRequired()], render_kw={'placeholder': '学号'})
    book_name = StringField('书名',validators=[DataRequired()], render_kw={'placeholder': '书名'})
    book_id = StringField('书名', render_kw={'placeholder': '书籍编号'})
    submit = SubmitField('还书')


class AddbookForm(FlaskForm):
    author = StringField('作者', render_kw={'placeholder': '作者'})
    pub_name = StringField('出版社', render_kw={'placeholder': '出版社'})
    bname = StringField('书名', render_kw={'placeholder': '书名'})
    pub_date = StringField('出版日期', render_kw={'placeholder': '出版日期'})
    bno = StringField('书籍编号', render_kw={'placeholder': '书籍编号'})
    summary = StringField('摘要', render_kw={'placeholder': '摘要'})
    total = StringField('馆藏数', render_kw={'placeholder': '馆藏数'})
    remain = StringField('剩余', render_kw={'placeholder': '剩余'})
    submit = SubmitField('增加书籍')


class AdduserForm(FlaskForm):
    udept = StringField('专业', validators=[DataRequired()], render_kw={'placeholder': '专业'})
    ugrade = StringField('年级', validators=[DataRequired()], render_kw={'placeholder': '年级'})
    uname = StringField('姓名', validators=[DataRequired()], render_kw={'placeholder': '姓名'})
    usex = StringField('性别', validators=[DataRequired()], render_kw={'placeholder': '性别'})
    uid = StringField('学号', validators=[DataRequired()], render_kw={'placeholder': '学号'})
    pswd = StringField('密码', validators=[DataRequired()], render_kw={'placeholder': '密码'})
    uidenty = StringField('身份', validators=[DataRequired()], render_kw={'placeholder': '身份'})
    submit = SubmitField('增加用户')


class DeleteBook(FlaskForm):
    bname = StringField('书名', render_kw={'placeholder': '书名'})
    submit = SubmitField('删除书籍')


class DeleteUser(FlaskForm):
    uid = StringField('学号', validators=[DataRequired()], render_kw={'placeholder': '学号'})
    submit = SubmitField('删除用户')


def calculate_date(date1, date2):
    # 偷了个懒，假设一个月30天
    year1=int(date1[0:3])
    year2=int(date2[0:3])
    month1 = int(date1[4:6])
    month2 = int(date2[4:6])
    day1 = int(date1[7:9])
    day2 = int(date2[7:9])
    d1=datetime.date(year1,month1,day1)
    d2=datetime.date(year2,month2,day2)
    days=d2-d1
    log('days:{}'.format(days))
    days=str(days)
    days=days.split()[0]
    days=int(days)
    log('days:{},type:{}'.format(days,type(days)))
    # if month2[0] == '0':
    #     month2 = month2[1]
    #     month1 = month1[1]
    # else:
    #     if month1[0] == '0':
    #         month1 = month1[1]
    # days = 0
    # if month1 == month2:
    #     day1 = date1[7:9]
    #     day2 = date2[7:9]
    #     if day2[0] == '0':
    #         day2 = month2[1]
    #         day1 = month1[1]
    #     else:
    #         if day1[0] == '0':
    #             day1 = month1[1]
    #     days = days + int(day2) - int(day1)
    #     log('1:{}'.format(str(days)))
    #     return days
    # else:
    #     months = int(month2) - int(month1)
    #     days = months * 30
    #     day1 = date1[7:9]
    #     day2 = date2[7:9]
    #     if day2[0] == '0':
    #         day2 = month2[1]
    #         day1 = month1[1]
    #     else:
    #         if day1[0] == '0':
    #             day1 = month1[1]
    #     days = days + int(day2) - int(day1)
    #     log('2:{}'.format(str(days)))
    return days


def make_borrow_info():
    user1 = User(udept='计算机', ugrade=2016, uname='王正文', usex='男', uid=2016141462225, pswd=777777, uidenty=0)
    user2 = User(udept='计算机', ugrade=2016, uname='余长才', usex='男', uid=2016141462110, pswd=888888, uidenty=0)
    user3 = User(udept='计算机', ugrade=2016, uname='马亚尔', usex='男', uid=2016141462007, pswd=999999, uidenty=0)
    db.session.add_all([user1, user2, user3])
    db.session.commit()
    book1 = Book(author='金庸', pub_name='青年出版社', bname='射雕英雄传', pub_date='19790901', bno=1, summary='这是一部江湖武打类小说',
                 total=10, remain=10)
    book2 = Book(author='金庸', pub_name='青年出版社', bname='天龙八部', pub_date='20000120', bno=2, summary='这是一部关于武林秘籍的小说',
                 total=10, remain=8)  # 借出去两本
    book3 = Book(author='金庸', pub_name='北京出版社', bname='鹿鼎记', pub_date='19341030', bno=3, summary='这部小说还曾被拍成了电影',
                 total=3, remain=3)
    book4 = Book(author='鲁迅', pub_name='中央文学出版社', bname='狂人日记', pub_date='19430503', bno=4, summary='鲁迅先生的小说',
                 total=1, remain=1)
    book5 = Book(author='鲁迅', pub_name='少数民族出版社', bname='阿Q正传', pub_date='19790101', bno=5,
                 summary='这是一部特别出名的讽刺意味深重的小说',
                 total=2, remain=2)
    book6 = Book(author='巴金', pub_name='四川大学出版社', bname='家', pub_date='20001009', bno=6, summary='这是一部讲述了很多复杂关系的小说',
                 total=7, remain=7)
    book7 = Book(author='巴金', pub_name='计算机学院出版社', bname='春', pub_date='19880921', bno=7, summary='这是一部特别有深度的小说',
                 total=20, remain=20)
    book8 = Book(author='巴金', pub_name='名字好难出版社', bname='秋', pub_date='20051230', bno=8, summary='这是巴金老先生的小说',
                 total=10, remain=10)
    book9 = Book(author='韩寒', pub_name='幼儿教育出版社', bname='三重门', pub_date='20160725', bno=9, summary='这是韩寒处女座小说',
                 total=5, remain=4)  # 借出去一本
    book10 = Book(author='韩寒', pub_name='机械工业出版社', bname='长安乱', pub_date='19990130', bno=10, summary='这是韩寒代表作小说',
                  total=5, remain=4)  # 借出去一本
    # book2 = Book(name="<<天龙八部>>", author_id=author1.id)
    #     # book3 = Book(name="<<鹿鼎记>>", author_id=author1.id)
    #     # book4 = Book(name="<<笑傲江湖>>", author_id=author1.id)
    #     # book5 = Book(name="<<武林外史>>", author_id=author2.id)
    #     # book6 = Book(name="<<萧十一郎>>", author_id=author2.id)
    #     # book7 = Book(name="<<小李飞刀>>", author_id=author2.id)
    #     # book8 = Book(name="<<狂人日记>>", author_id=author3.id)
    #     # book9 = Book(name="<<阿Q正传>>", author_id=author3.id)
    #     # book10 = Book(name="<<家>>", author_id=author4.id)
    #     # book11 = Book(name="<<春>>", author_id=author4.id)
    #     # book12 = Book(name="<<秋>>", author_id=author4.id)
    db.session.add_all([book1, book2, book3, book4, book5, book6,
                        book7, book8, book9, book10])
    db.session.commit()
    borrow_info1 = Borrow_info(borrow_id=1, bname='天龙八部', borrow_date='20180906', return_date='20181207',
                               user_id=user1.uid, book_no=book2.bno)
    borrow_info2 = Borrow_info(borrow_id=2, bname='天龙八部', borrow_date='20181206', return_date='20181219',
                               user_id=user2.uid, book_no=book2.bno)
    borrow_info3 = Borrow_info(borrow_id=3, bname='三重门', borrow_date='20181007', return_date='20181219',
                               user_id=user1.uid, book_no=book9.bno)
    borrow_info4 = Borrow_info(borrow_id=4, bname='长安乱', borrow_date='20180701', return_date='20180827',
                               user_id=user3.uid, book_no=book10.bno)
    db.session.add_all([borrow_info1, borrow_info2, borrow_info3, borrow_info4])
    db.session.commit()


def make_monitor():
    monitor1 = User(udept='计算机', ugrade=2016, uname='杨随缘', usex='男', uid=2016141462167, pswd=666666, uidenty=1)
    db.session.add_all([monitor1])
    db.session.commit()


def add_user(udept, ugrade, uname, usex, uid, pswd, uidenty=0):
    udept = udept
    ugrade = ugrade
    uname = uname
    usex = usex
    uid = uid
    pswd = pswd
    uidenty = uidenty
    user_query = User.query.filter_by(uid=uid).first()

    if user_query:
        uid_query = User.query.filter_by(uid=uid).first()  # 查询并拿数据
        if uid_query:
            log("您要添加的用户已经存在!")
            try:
                update_user = User(udept=udept, ugrade=ugrade, uname=uname, usex=usex, uid=uid, pswd=pswd,
                                   uidenty=uidenty)
                db.session.merge(update_user)
            except Exception as e:
                db.session.rollback()  # 回滚操作
                return False
        else:
            try:
                new_user = User(udept=udept, ugrade=ugrade, uname=uname, usex=usex, uid=uid, pswd=pswd, uidenty=uidenty)
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                log("添加新用户错误!")
                db.session.rollback()  # 回滚操作
                return False
    else:
        # 5.如果不存在
        try:
            new_user = User(udept=udept, ugrade=ugrade, uname=uname, usex=usex, uid=uid, pswd=pswd, uidenty=uidenty)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            log("添加新用户错误!")
            db.session.rollback()  # 回滚操作
            return False

    return True


def registration(udept, ugrade, uname, usex, uid, pswd, uidenty=0):
    udept = udept
    ugrade = ugrade
    uname = uname
    usex = usex
    uid = uid
    pswd = pswd
    uidenty = uidenty
    uid_existed = User.query.filter_by(uid=uid).first()
    if uid_existed:
        flash('You has been registrated!')
        return redirect(url_for('/'))
    else:
        new_user = add_user(udept=udept, ugrade=ugrade, uname=uname, usex=usex, uid=uid, pswd=pswd, uidenty=uidenty)
        if_registrated = User.query.filter_by(uid=uid).first()  # 查询数据库中是否有该记录
        if if_registrated:
            log('Successfully registrated!')
            flash('Successfully registrated!')
            return redirect(url_for('/'))
        else:
            log('Unsuccessfully registrated!')
            flash('please try registration one more time!')
            return redirect(url_for('/'))


# @app.route("/monitor_index", methods=["GET", "POST"])
# def add_author_book():
#     true_form = TrueForm()
#     """
#     1.调用WTF的函数实现验证
#     2.验证通过则获取数据
#         3.判断作者是否存在
#         4.如果作者存在, 则判断书籍是否存在, 没有重复的书籍就添加数据, 如果重复就提示错误.
#         5.如果作者不存在, 就添加作者和书籍
#     6.验证不通过就提示错误.
#     """
#     # 调用WTF的函数实现验证
#     if true_form.validate_on_submit():
#         # 2.验证通过则获取此时填入的数据
#         author_name = true_form.author.data
#         book_name = true_form.book.data
#         # 3.判断作者是否存在, Author.query.filter_by(name=author_name)是查询, .first()才是拿到数据.
#         author_query = Author.query.filter_by(name=author_name).first()
#         # 4.如果作者存在
#         if author_query:
#             book_query = Book.query.filter_by(name=book_name).first()  # 查询并拿数据
#             if book_query:
#                 flash("您要添加的书籍已存在!")
#             else:
#                 try:
#                     new_book = Book(name="<<%s>>" % book_name, author_id=author_query.id)
#                     db.session.add(new_book)
#                     db.session.commit()
#                 except Exception as e:
#                     flash("添加书籍错误!")
#                     db.session.rollback()  # 回滚操作
#         else:
#             # 5.如果作者不存在
#             try:
#                 new_author = Author(name=author_name)
#                 db.session.add(new_author)
#                 db.session.commit()
#                 new_book = Book(name="<<%s>>" % book_name, author_id=new_author.id)
#                 db.session.add(new_book)
#                 db.session.commit()
#             except Exception as e:
#                 flash("添加作者和书籍错误!")
#                 db.session.rollback()
#     else:
#         # 验证不通过
#         if request.method == "POST":
#             flash("参数错误!")
#     # 查询所有的作者信息, 让信息传递给模板
#     all_authors = Author.query.all()
#     return render_template("book_manage.html", all_authors=all_authors, form=true_form)


# 网页中删除书籍-->将book_id参数传到路由, 路由再将book_id传入delete_book函数内部使用.
# < >尖括号代表路由参数, 路由需要接受参数
# 删除书籍
# @app.route("/delete_book/<bno>", methods=["GET", "POST"])
# def delete_book(bno):
#     # 1.查询书籍并拿数据
#     book = Book.query.get(bno)
#     try:
#         db.session.delete(book)
#         db.session.commit()
#     except Exception as e:
#         flash("删除错误!")
#         db.session.rollback()
#     # redirect重定向回到根路径, redirect接收路由地址参数, 或者直接接收网址参数(http://xxxxx.com)
#     # url_for("index"): 需要传入视图函数名, 返回该视图函数对应的路由地址(url)
#     return redirect(url_for('/'))


# 删除用户
# @app.route("/delete_user/<uid>", methods=["GET", "POST"])
# def delete_user(uid):
#     # 1.查询用户并拿数据
#     user = User.query.get(uid)
#     try:
#         # 查询书籍并删除, 直接在查询后面跟 .delete()就可以直接将查询到的结果删除掉
#         User.query.filter_by(uid=uid).delete()
#         db.session.delete(user)
#         db.session.commit()
#     except Exception as e:
#         flash("删除错误!")
#         db.session.rollback()  # 回滚
#     return redirect(url_for('/'))  # 重定向回到根路径
#

# @app.route('/login/<uid>/<password>')
# def login(uid, password):
#     registrate_record = User.query.filter_by(uid=uid).first()
#     if registrate_record == None:
#         return 'please registrate firstly!'
#     else:
#         registrate_record = str(registrate_record)
#         check_pswd = registrate_record.find(password)
#         if check_pswd == -1:
#             return 'Please enter correct password!'
#         else:
#             log(registrate_record)
#             log(registrate_record[-1])
#             if registrate_record[-1] == str(0):
#                 return 'hello,user!'
#             else:
#                 return 'hello,monitor!'

#
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = form.username.data
#         password = form.password.data
#         log(user)
#         log(password)
#         uid = str(user)
#         registrate_record = User.query.filter_by(uid=uid).first()
#
#         if registrate_record == None:
#             flash('please registrate firstly!')
#             log('please registrate firstly!')
#         else:
#             registrate_record = str(registrate_record)
#             check_pswd = registrate_record.find(password)
#             if check_pswd == -1:
#                 flash('Please enter correct password!')
#                 log('Please enter correct password!')
#             else:
#                 log(registrate_record)
#                 log(registrate_record[-1])
#                 if registrate_record[-1] == str(0):
#                     log('go to userpage')
#                     return redirect(url_for('index'))
#                 else:
#                     log('go to monitor page')
#                     return redirect(url_for('book_manage.html'))
#     else:
#         flash('something wrong!')
#         log('something wrong!')
#     return render_template('login.html', form=form)
#     # return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        log(user)
        log(password)
        uid = str(user)
        registrate_record = User.query.filter_by(uid=uid).first()

        if registrate_record == None:
            flash('please registrate firstly!')
            log('please registrate firstly!')
        else:
            registrate_record = str(registrate_record)
            check_pswd = registrate_record.find(password)
            if check_pswd == -1:
                flash('Please enter correct password!')
                log('Please enter correct password!')
            else:
                current_user = user  # 把当前用户记录下来
                log(registrate_record)
                u1 = registrate_record.find('身份：')
                identity = registrate_record[u1 + 3:u1 + 4]
                log(identity)
                if identity == str(0):
                    log('go to user page')
                    return redirect(url_for('redict_to_user'))
                else:
                    log('go to monitor page')
                    return redirect(url_for('redict_to_monitor'))
    else:
        flash('something wrong!')
        log('something wrong!')
    return render_template('index.html', form=form)


@app.route('/redict_to_user', methods=['GET', 'POST'])
def redict_to_user():
    return render_template('user.html')


@app.route('/redict_to_login', methods=['GET', 'POST'])
def redict_to_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        log(user)
        log(password)
        uid = str(user)
        registrate_record = User.query.filter_by(uid=uid).first()

        if registrate_record == None:
            flash('please registrate firstly!')
            log('please registrate firstly!')
        else:
            registrate_record = str(registrate_record)
            check_pswd = registrate_record.find(password)
            if check_pswd == -1:
                flash('Please enter correct password!')
                log('Please enter correct password!')
            else:
                log(registrate_record)
                log(registrate_record[-1])
                u = registrate_record.find('身份：')  # 第一个切割点
                identy = registrate_record[u + 3:u + 4]
                if identy == str(0):
                    log('go to user page')
                    return redirect(url_for('redict_to_user'))
                else:
                    log('go to monitor page')
                    return redirect(url_for('redict_to_monitor'))
    else:
        flash('something wrong!')
        log('something wrong!')
    return render_template('index.html', form=form)


@app.route('/redict_to_monitor', methods=['GET', 'POST'])
def redict_to_monitor():
    return render_template('monitor.html')


@app.route('/show_borrowinfo')
def show_borrowinfo():
    borrow_infos = Borrow_info.query.all()
    # log(type(borrow_infos))    #<class 'list'>
    log(borrow_infos)
    return render_template('borrow_info.html', borrow_infos=borrow_infos)


@app.route('/show_outdate')
def show_outdate():
    # borrow_infos = Borrow_info.query.all()
    # outdates = []
    # for each in borrow_infos:
    #     each = str(each)
    #     u1 = each.find('借书日期：')  # 切割点1
    #     borrow_date = each[u1 + 5:u1 + 13]
    #     log(borrow_date)
    #     u2 = each.find('还书日期：')  # 切割点2
    #     return_date = each[u2 + 5:u2 + 13]
    #     days = calculate_date(borrow_date, return_date)
    #     if days >= 30:  # 假设最长借书期限为30天
    #         outdates.append(each)
    # log(outdates)

    borrow_infos = Borrow_info.query.filter(                # 从未还的书里面找
        Borrow_info.return_date.like("%" + time.strftime('%Y%m%d', time.localtime(time.time() + 86400)) + "%"),
    ).all()

    outdates = []
    for each in borrow_infos:
        each = str(each)
        u1 = each.find('借书日期：')  # 切割点1
        borrow_date = each[u1 + 5:u1 + 13]
        log(borrow_date)
        # u2 = each.find('还书日期：')  # 切割点2
        # return_date = each[u2 + 5:u2 + 13]
        return_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        days = calculate_date(borrow_date, return_date)
        if days >= 30:  # 假设最长借书期限为30天
            outdates.append(each)
    users=[]
    for every in outdates:
        u=every.find('借书人学号：')
        uid=every[u+6:u+19]
        user_info=User.query.filter_by(uid=uid).first()
        users.append(user_info)
    return render_template('outdate.html', outdates=outdates,users=users)


def tell_outdate(uid):
    # borrow_infos = Borrow_info.query.all()

    borrow_infos = Borrow_info.query.filter(                             #从未还的书里面找
        Borrow_info.user_id.like("%" + uid + "%"),
        Borrow_info.return_date.like("%" + time.strftime('%Y%m%d', time.localtime(time.time()+86400)) + "%"),
    ).all()

    outdates = []
    for each in borrow_infos:
        each = str(each)
        u1 = each.find('借书日期：')  # 切割点1
        borrow_date = each[u1 + 5:u1 + 13]
        log(borrow_date)
        # u2 = each.find('还书日期：')  # 切割点2
        # return_date = each[u2 + 5:u2 + 13]
        return_date=time.strftime('%Y%m%d', time.localtime(time.time()))
        days = calculate_date(borrow_date, return_date)
        if days >= 30:  # 假设最长借书期限为30天
            outdates.append(each)
    log(outdates)
    flag = 0  # 没有超期未还的书
    for each_outdate in outdates:
        exist = each_outdate.find(uid)
        if exist == -1:
            continue
        else:
            flag = 1  # 有超期未还的书
            break
    if flag == 0:
        return 'on'
    else:
        return 'yes'


@app.route('/refer_book', methods=['GET', 'POST'])
def refer_book():
    form = ReferBook()
    if form.validate_on_submit():
        author = form.author.data
        pub_name = form.pub_name.data
        bname = form.bname.data
        pub_date = form.pub_name.data
        bno = form.bno.data
        summary = form.summary.data
        books = Book.query.all()
        refered = []
        if author != None:
            author_query = Book.query.filter_by(author=author).all()
            if author_query == []:
                author_query = Book.query.all()
            # log(author_query)
        else:
            author_query = Book.query.all()
        if pub_name != None:
            pub_name_query = Book.query.filter_by(pub_name=pub_name).all()
            if pub_name_query == []:
                pub_name_query = Book.query.all()
            # log(pub_name_query)
        else:
            pub_name_query = Book.query.all()
        if bname != None:
            bname_query = Book.query.filter_by(bname=bname).all()
            if bname_query == []:
                bname_query = Book.query.all()
            # log(bname_query)
        else:
            bname_query = Book.query.all()
        if pub_date != None:
            pub_date_query = Book.query.filter_by(pub_date=pub_date).all()
            if pub_date_query == []:
                pub_date_query = Book.query.all()
            # log(pub_date_query)
        else:
            pub_date_query = Book.query.all()
        if bno != None:
            bno_query = Book.query.filter_by(bno=bno).all()
            if bno_query == []:
                bno_query = Book.query.all()
            # log(bno_query)
        else:
            bno_query = Book.query.all()
        if summary != None:
            summary_query = Book.query.filter_by(summary=summary).all()
            if summary_query == []:
                summary_query = Book.query.all()
            log(summary_query)
        else:
            summary_query = Book.query.all()
        for a in author_query:  # 遍历寻找六个列表的交集
            for b in pub_name_query:
                for c in bname_query:
                    for d in pub_date_query:
                        for e in bno_query:
                            for f in summary_query:
                                if a == b == c == d == e == f:
                                    refered.append(a)

        if refered == books:
            refered = []
        else:
            pass
        log('refered:{}'.format(refered))
        return render_template('refer_book.html', form=form, refered=refered)

    return render_template('refer_book.html', form=form)


@app.route('/change_userinfo', methods=['GET', 'POST'])
def change_userinfo():
    form = UserForm()
    if form.validate_on_submit():
        uid = form.uid.data
        # add_user(udept=udept,ugrade=ugrade,uname=uname,usex=usex,uid=uid,pswd=pswd) #这样写是不对的
        record = User.query.filter_by(uid=uid).first()
        record.udept = form.udept.data
        record.ugrade = form.ugrade.data
        record.uname = form.uname.data
        record.usex = form.usex.data
        record.uid = form.uid.data
        record.pswd = form.pswd.data
        db.session.commit()
        return redirect(url_for('redict_to_login'))
    else:
        flash('出错啦！')
        log('出错啦！')
    return render_template('change_userinfo.html', form=form)


@app.route('/borrow', methods=['GET', 'POST'])
def borrow_book():
    form = BorrowForm()
    if form.validate_on_submit():
        user = form.user.data
        book_name = form.book_name.data
        book_id = form.book_id.data
        user_record = User.query.filter_by(uid=user).first()
        refered = []
        if user_record:
            if_outdate = tell_outdate(user)
            if if_outdate == 'yes':
                log('有超期未还的书不能借！')
                # flash('有超期未还的书不能借！')
                message='有超期未还的书不能借！'
                return render_template('borrow.html', form=form, message=message)
            else:
                books = Book.query.all()
                if book_name != None:
                    bname_query = Book.query.filter_by(bname=book_name).all()
                    if bname_query == []:
                        bname_query = Book.query.all()
                    # log(bname_query)
                else:
                    bname_query = Book.query.all()
                if book_id != None:
                    bno_query = Book.query.filter_by(bno=book_id).all()
                    if bno_query == []:
                        bno_query = Book.query.all()
                    # log(bno_query)
                else:
                    bno_query = Book.query.all()
                for a in bname_query:
                    for b in bno_query:
                        if a == b:
                            refered.append(a)
                if refered == books:
                    refered = []  # 要借的书在这个列表里面
                else:
                    pass

                # record=refered[0]
                # parts=record.split()

                borrow_id = Borrow_info.query.count() + 1
                bname = book_name  # 其实不能直接这样得到，需要重构这个API
                borrow_date = '{}'.format(time.strftime('%Y%m%d', time.localtime(time.time())))
                return_date = '{}'.format(time.strftime('%Y%m%d', time.localtime(time.time()+86400)))    #还书日期为当天时间的后一天表示还未还书！
                user_id = user
                book_no = book_id  # 其实不能直接这样得到，需要重构这个API
                borrow_info = Borrow_info(borrow_id=borrow_id, bname=bname, borrow_date=borrow_date,
                                          return_date=return_date,
                                          user_id=user_id, book_no=book_no)
                db.session.add(borrow_info)
                db.session.commit()  # 更新借阅表

                this_book = Book.query.filter_by(bname=bname).first()
                this_book.remain = this_book.remain - 1
                db.session.commit()  # 更新书表
                log('借书成功！')
                message='借书成功！'
                # flash('借书成功！')
                return render_template('borrow.html', form=form,message=message)
    else:
        log('用户不存在！')
        flash('用户不存在！')
    return render_template('borrow.html', form=form)


@app.route('/return', methods=['GET', 'POST'])
def return_book():
    form = ReturnForm()
    if form.validate_on_submit():
        user = form.user.data
        book_name = form.book_name.data
        book_id = form.book_id.data
        borrow_infos = Borrow_info.query.all()
        user_query = Borrow_info.query.filter_by(user_id=user).all()
        if book_name != None:
            bname_query = Borrow_info.query.filter_by(bname=book_name).all()
            if bname_query == []:
                bname_query = Borrow_info.query.all()
        else:
            bname_query = Borrow_info.query.all()
        if book_id != None:
            bno_query = Borrow_info.query.filter_by(book_no=book_id).all()
            if bno_query == []:
                bno_query = Borrow_info.query.all()
        else:
            bno_query = Borrow_info.query.all()

        this_borrow = Borrow_info.query.filter(
            Borrow_info.user_id.like("%" + user + "%"),
            Borrow_info.bname.like("%" + book_name + "%"),
        ).all()

        this_book = Book.query.filter_by(bname=book_name).first()
        this_book.remain = this_book.remain + 1
        db.session.commit()  # 更新书表

        this_borrow[0].return_date='{}'.format(time.strftime('%Y%m%d', time.localtime(time.time())))    #把还书日期改为今天，更新借阅表
        db.session.commit()
        log('还书成功！')


        days=calculate_date(this_borrow[0].borrow_date,this_borrow[0].return_date)
        if days>=30:
            message='您该书籍超出借书期限：{}天！'.format(days-30)
        else:
            message='您已按时还书！'


        # for a in user_query:
        #     for b in bname_query:
        #         for c in bno_query:
        #             if a == b == c:
        #                 #db.session.delete(a)  # 删除借阅记录,,,不应该删除记录！而是应该把还书日期改为今天！
        #
        #                 this_book = Book.query.filter_by(bname=book_name).first()
        #                 this_book.remain = this_book.remain + 1
        #                 db.session.commit()  # 更新书表
        #                 log('还书成功！')
        #                 flash('还书成功！')
        #                 # 如果超期，显示超期日期
        return render_template('return.html', form=form,message=message)
    return render_template('return.html', form=form)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddbookForm()
    if form.validate_on_submit():
        author = form.author.data
        pub_name = form.pub_name.data
        bname = form.bname.data
        pub_date = form.pub_date.data
        bno = form.bno.data
        summary = form.summary.data
        total = form.total.data
        remain = form.remain.data
        new_book = Book(author=author, pub_name=pub_name, bname=bname, pub_date=pub_date, bno=bno, summary=summary,
                        total=total, remain=remain)
        db.session.add(new_book)
        db.session.commit()
        if_add = Book.query.filter_by(bname=bname).first()
        if if_add:
            message = 'Successfully add the new book!'
        else:
            message = 'Unccessfully add the new book!'
        return render_template('add_book.html', form=form, message=message)
    return render_template('add_book.html', form=form)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AdduserForm()
    if form.validate_on_submit():
        udept = form.udept.data
        ugrade = form.ugrade.data
        uname = form.uname.data
        usex = form.usex.data
        uid = form.uid.data
        pswd = form.pswd.data
        uidenty = form.uidenty.data
        new_user = User(udept=udept, ugrade=ugrade, uname=uname, usex=usex, uid=uid, pswd=pswd, uidenty=uidenty)
        db.session.add(new_user)
        db.session.commit()
        if_add = User.query.filter_by(uid=uid).first()
        if if_add:
            message = 'Successfully add the new user!'
        else:
            message = 'Unccessfully add the new user!'
        return render_template('add_user.html', form=form, message=message)
    return render_template('add_user.html', form=form)


@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    form = DeleteBook()
    if form.validate_on_submit():
        bname = form.bname.data
        # if_borrow = Borrow_info.query.filter_by(bname=bname).first()
        if_borrow = Borrow_info.query.filter(
            Borrow_info.bname.like("%" + bname + "%"),
        ).all()
        if if_borrow:
            message = '这书还有人在借未还！'
        else:
            book = Book.query.filter_by(bname=bname).first()
            db.session.delete(book)
            db.session.commit()
            message = '删除书籍成功！'
        return render_template('delete_book.html', form=form, message=message)
    return render_template('delete_book.html', form=form)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    form = DeleteUser()
    if form.validate_on_submit():
        uid = form.uid.data
        if_borrow = Borrow_info.query.filter_by(user_id=uid).first()
        if if_borrow:
            message = '有书未还，用户不能删除！'
        else:
            user = User.query.filter_by(uid=uid).first()
            db.session.delete(user)
            db.session.commit()
            message = '删除用户成功！'
        return render_template('delete_user.html', form=form, message=message)
    return render_template('delete_user.html', form=form)


@app.route('/change_bookinfo', methods=['GET', 'POST'])
def change_bookinfo():
    form = BookInfo()
    if form.validate_on_submit():
        bname = form.bname.data
        record = Book.query.filter_by(bname=bname).first()

        record.pub_date = form.pub_date.data
        # record.bno = form.bno.data

        record.summary = form.summary.data
        record.total = form.total.data
        record.remain = form.remain.data
        record.author = form.author.data
        record.pub_name = form.pub_name.data
        record.bname = form.bname.data
        db.session.commit()
        message = Book.query.filter_by(bname=bname).first()
        return render_template('change_bookinfo.html', form=form, message=message)
    return render_template('change_bookinfo.html', form=form)


@app.route('/refer_user', methods=['GET', 'POST'])
def refer_user():
    form = ReferUser()
    if form.validate_on_submit():
        udept = form.udept.data
        ugrade = form.ugrade.data
        uname = form.uname.data
        usex = form.usex.data
        uid = form.uid.data
        users = User.query.all()
        log('users:{}'.format(users))
        refered = []
        if udept != None:
            udept_query = User.query.filter_by(udept=udept).all()
            log('udept_query1:{}'.format(udept_query))
            if udept_query == []:
                udept_query = User.query.all()
                log('udept_query:{}'.format(udept_query))
        else:
            udept_query = User.query.all()

        if ugrade != None:
            ugrade_query = User.query.filter_by(ugrade=ugrade).all()
            if ugrade_query == []:
                ugrade_query = User.query.all()
                log('ugrade_query:{}'.format(ugrade_query))
        else:
            ugrade_query = User.query.all()

        if uname != None:
            uname_query = User.query.filter_by(uname=uname).all()
            log('uname_query1:{}'.format(uname_query))
            if uname_query == []:
                uname_query = User.query.all()
                log('uname_query:{}'.format(uname_query))
            # log(author_query)
        else:
            uname_query = User.query.all()

        if usex != None:
            usex_query = User.query.filter_by(usex=usex).all()
            if usex_query == []:
                usex_query = User.query.all()
            # log(author_query)
        else:
            usex_query = User.query.all()

        if uid != None:
            uid_query = User.query.filter_by(uid=uid).all()
            if uid_query == []:
                uid_query = User.query.all()
            # log(author_query)
        else:
            uid_query = User.query.all()

        for a in udept_query:  # 遍历寻找六个列表的交集
            for b in ugrade_query:
                for c in uname_query:
                    for d in usex_query:
                        for e in uid_query:
                            if a == b == c == d == e:
                                refered.append(a)

        # if refered == users:
        #     refered = []
        # else:
        #     pass
        log('refered:{}'.format(refered))
        borrows = Borrow_info.query.filter_by(user_id=uid).all()
        return render_template('refer_user.html', form=form, refered=refered, borrows=borrows)

    return render_template('refer_user.html', form=form)


def main():
    # 先删除所有表, 在创建表之前要先删掉表
    db.drop_all()
    # 再创建所有表
    db.create_all()
    make_monitor()
    make_borrow_info()
    # calculate_date('20180906','20181207')
    # app.run(debug=True)
    # all_results = Borrow_info.query.filter(
    #     Borrow_info.user_id.like("%" + '2016141462225' + "%"),
    #     Borrow_info.bname.like("%" + '天龙八部' + "%"),
    # ).all()
    # log('all_results:{}'.format(all_results))
    app.run()


if __name__ == '__main__':
    main()
