// pages/share/share.js
Page({
  
  data: {
    access_token: null
  },
  
  onLoad: function(){
    var that=this
      wx.request({
        url: 'https://api.weixin.qq.com/cgi-bin/token',
        data:{
          grant_type:'client_credential',
          appid:'wx4537dd85987be83b',
          secret: 'f10d099a99bb1004eeb493037e25a391'
        },
        success: function(res) {
         // console.log(res)
          that.setData({
            access_token: res.data.access_token
          })
          wx.request({
            url: 'https://api.weixin.qq.com/wxa/getwxacode',
            method:'POST',
            header: {
              'content-type': 'application/json'
            },
            data: {
              access_token: res.data.access_token,
              path:'pages/report/report'
            },
            success: function(res){
              console.log(res)
            }
          })
        }
      })
    },

  onShareAppMessage: function (res) {
    if (res.from === 'button') {
      // 来自页面内转发按钮
      console.log(res.target)
    }
    return {
      title: '我的美食报告',
      path: '/pages/report/report'
    }
    wx.showShareMenu({
      withShareTicket: true
    })
    wx.updateShareMenu({
      withShareTicket: true,
      success() {
      }
    })
  }

})