package com.system.service.impl;

//import com.system.po.Userlogin;
import com.system.po.Userlogin;
import com.system.po.UserloginExample;
import com.system.po.Userregister;
import com.system.service.RegisterService;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class RegisterServiceImpl implements RegisterService {
    @Autowired
    private RegisterMapper registerMapper;

    public Userregister findByName(String name) throws Exception{
        UserloginExample userloginExample = new UserloginExample();

        UserloginExample.Criteria criteria = userloginExample.createCriteria();
        criteria.andUsernameEqualTo(name);

        List<Userlogin> list = RegisterMapper.selectByExample(userloginExample);

        return list.get(0);
    }
    public void save(Userlogin userlogin) throws Exception {
        RegisterMapper.insert(userlogin);
    }

}
