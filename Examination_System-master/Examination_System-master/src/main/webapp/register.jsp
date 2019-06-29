<%--
  Created by IntelliJ IDEA.
  User: 长恨歌是假的
  Date: 2019/6/27
  Time: 9:09
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title></title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入bootstrap -->
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
    <!-- 引入JQuery  bootstrap.js-->
    <script src="/js/jquery-3.2.1.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
</head>
<body>
<!-- 顶栏 -->
<div class="container" id="top">
<div class="row">
    <div class="col-md-12">
        <!--加入导航条标题-->
        <div class="navbar navbar-default" role="navigation">
            　<div class="navbar-header">
            　    <a href="##" class="navbar-brand">教务信息查询系统</a>
            　</div>
        </div>

    </div>
</div>
</div>
<!-- 中间主体 -->
<div class="container" id="content">
    <div class="row">
<%--        <jsp:include page="menu.jsp"></jsp:include>--%>
        <div class="col-md-10">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <div class="row">
                        <h1 style="text-align: center;">新用户注册！</h1>
                    </div>
                </div>
                <div class="panel-body">

                    <form name="regis" class="form-horizontal" role="form" action="/register.jsp" id="editfrom" method="post" onsubmit="return check()">

                        <div class="form-group">
                            <label for="inputEMAIL3" class="col-sm-2 control-label">用户名</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" name="User_name" id="inputEmail3" placeholder="请输入用户名" >
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">姓名</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" name="name" id="inputEmail3" placeholder="请输入姓名" >
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
                            <div class="col-sm-10">
                                <input type="password" name="password1" class="form-control" id="inputPassword3" placeholder="请输入密码">
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="inputPassword3" class="col-sm-2 control-label">确认密码</label>
                            <div class="col-sm-10">
                                <input type="password" name="password2" class="form-control" id="inputPassword3" placeholder="请再次输入密码">
                            </div>
                        </div>


                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">请输入学院</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" name="college" id="inputEmail3" placeholder="请输入学院">
                            </div>
                        </div>


                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">年级</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control" name="grade" id="inputEmail3" placeholder="请输入年级" >
                                </div>
                        </div>

<%--                        <select name="major">--%>
<%--                            <option>--请选择专业--</option>--%>
<%--                            <option value="option1">计算机系</option>--%>
<%--                            <option value="option2">设计系</option>--%>
<%--                            <option value="option3">财经系</option>--%>
<%--                        </select>--%>

                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">专业</label>
                            <div class="col-sm-10">
<%--                                <input type="text" class="form-control" name="grade" id="inputEmail3" placeholder="请输入年级" >--%>
                                 <select name="major">
                                         <option>--请选择专业--</option>
                                         <option value="option1">计算机系</option>
                                         <option value="option2">设计系</option>
                                         <option value="option3">财经系</option>
                                 </select>
                            </div>
                        </div>

                        <div class="form-group" style="text-align: center">
                            <button class="btn btn-default" type="submit">提交</button>
                            <button class="btn btn-default" >重置</button>
                        </div>
                    </form>
                </div>

            </div>

        </div>
    </div>
</div>
<div class="container" id="footer">
    <div class="row">
        <div class="col-md-12"></div>
    </div>
</div>
</body>
<script>
    $("#nav li:nth-child(5)").addClass("active")
    function check() {
        // if(reset.oldPassword.value==""||reset.oldPassword.value==null)
        // {alert("请输入旧账户密码");return false;}
        // if(reset.password1.value==""||reset.password1.value==null)
        // {alert("请输入重置密码");return false;}
        // if(regis.password2.value==""||regis.password2.value==null)
        // {alert("请输入再次输入密码");return false;}
        if(regis.password1.value != regis.password2.value)
        {alert("两次密码不正确");return false;}
    }
</script>
</html>
