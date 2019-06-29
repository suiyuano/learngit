package com.system.service;

//import com.system.po.Userlogin;
import com.system.po.Userregister;

public interface RegisterService {
    //根据名字查找用户
    Userregister findByName(String name) throws Exception;

    //保存用户注册信息
    void save(Userregister userregister) throws Exception;

    //根据姓名删除
//    void removeByName(String name) throws Exception;

    //根据用户名更新
//    void updateByName(String name, Userregister userlogin);
}
