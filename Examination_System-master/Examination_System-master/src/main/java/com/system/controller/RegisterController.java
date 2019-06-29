package com.system.controller;

import com.system.po.Userlogin;
import com.system.po.Userregister;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.subject.Subject;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Created by 长恨歌是假的 on 2019/6/29.
 */

@Controller
public class RegisterController {

    //注册跳转
    @RequestMapping(value = "/register",method = {RequestMethod.GET})
    public String registerUI() throws Exception {
        return "../../register";
    }

    //注册表单处理
    @RequestMapping(value = "/register",method = {RequestMethod.POST})
//    public String register(Userregister userregister) throws Exception{
        public String register(Userregister userregister) {
            String username=userregister.getUsername();
            // 如果数据库中没有该用户，可以注册，否则跳转页面
            if (RegisterService.findByUserName(username) == null) {
                // 添加用户
                RegisterService.register(userregister);
　　　　　　　// 注册成功跳转到主页面
                return "/login";
            }else {
                // 注册失败跳转到错误页面
                return "error";
            }



    }

}
