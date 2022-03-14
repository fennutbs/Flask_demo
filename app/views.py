# -*- coding:utf-8 -*-

from flask import request, abort, make_response, jsonify
from app.models import *
from flask_restful import fields, marshal

user_login = {
    'id': fields.String,
    'pwd': fields.String,
    'age': fields.Integer,
    'email': fields.String,
    'address': fields.String,
    'phone': fields.String
}
('/register')

@app.route
def register():
    # 注册页面的渲染
    return "成功"


# 注册成功，向数据库添加用户列表，表单格式
@app.route('/register/add', methods=['GET', 'POST'])
def register_add():
    id = request.form['id']
    pwd = request.form['pwd']
    phone = request.form['phone']
    age = request.form['age']
    email = request.form['email']
    address = request.form['address']
    user = User(id=id, pwd=pwd, phone=phone, age=age, email=email, address=address)
    # User.age = request.form['age']
    db.session.add(user)
    db.session.commit()
    return "添加成功"


# 登录页面，验证密码，返回成功失败,status的状态有0，1，-1
@app.route('/login', methods=['GET', 'POST'])
def login():
    _id = request.form.get('id')
    _pwd = request.form.get('pwd')
    print(_id, _pwd)
    user = User.query.get(_id)
    if user.pwd == _pwd:
        res = make_response("login success")
        res.status = 1
        res.headers['token'] = '123456'
        return jsonify(marshal(user, user_login))
    elif user.pwd != _pwd:
        res = make_response("login fail")
        res.status = 0
        res.headers['token'] = '123456'
        return "login fail"
    else:
        res = make_response("id不存在")
        res.status = -1
        return "id不存在"


# 修改信息页面,包括原来的密码和新密码
@app.route('/person/changePwd', methods=['GET', 'POST'])
def changePwd():
    _id = request.form.get('id')
    _oldPwd = request.form.get('old_pwd')
    _newPwd = request.form.get('new_pwd')
    # 验证是否正确
    user = User.query.get(_id)
    print(_oldPwd, user.pwd)
    if user.pwd == _oldPwd:
        User.query.filter(User.id == _id).update({"pwd": _newPwd})
        db.session.commit()
        return "修改密码成功"
    else:
        return "密码输入错误"


# 注销页面，表单信息为id和pwd
@app.route('/person/logout', methods=['GET', 'POST'])
def logout():
    _id = request.form.get('id')
    _pwd = request.form.get('pwd')
    # 验证是否正确
    user = User.query.get(_id)
    if user.pwd == _pwd:
        User.query.filter(User.id == _id).delete()
        db.session.commit()
        return "注销成功"
    else:
        return "用户验证错误，注销失败"


# 修改用户的手机号码信息
@app.route('/person/changePhone', methods=['GET', 'POST'])
def changePhone():
    _id = request.form.get('id')
    _pwd = request.form.get('pwd')
    _newPhone = request.form.get('newPhone')
    # 验证是否正确
    user = User.query.get(_id)
    if user.pwd == _pwd:
        User.query.filter(User.id == _id).update({"phone": _newPhone})
        db.session.commit()
        return "修改手机号码成功"
    else:
        return "用户验证错误，手机号码修改失败"
