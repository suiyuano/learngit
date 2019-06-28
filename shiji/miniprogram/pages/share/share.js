// pages/share/share.js
Page({
  
  data: {
    imgurl:'',
    access_token: '',
    xcxCodeImageData:null,
    id:1
  },
  
  onLoad: function (){
    var that=this
    // scene 需要使用 decodeURIComponent 才能获取到生成二维码时传入的 scene
    // const id = decodeURIComponent(query.scene)
    

    // wx.request({
    //   url: 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=22_JKJztMLIEZlPPN7W8QeDETZ4oV2y7gGcqbZncX28wwHyG0PAJp5s6BT_czxG3N8byEwuGUbi5KGjZUPa9kD66WTPWziq__BG9Phk-2e4ln_pjlxduR4aRZWWMW8GcHGOYbybEZFp4llUF3L2RXVeAFAVBZ', //获取小程序B接口二维码
    //   method: "POST",
    //   responseType: 'arraybuffer', //这一行非常重要，重中之重
    //   data: {
    //     scene: '22a45fds',
    //     page: "pages/report/report",
    //     width: 280,
    //     is_hyaline: true
    //   },
    //   header: {
    //     'content-type': 'application/json;charset=utf-8'
    //   },
    //   success(res) {
    //     console.log('successful get QRcode:' + res.data);
    //     var base64 = wx.arrayBufferToBase64(res.data);
    //     that.setData({
    //       imgurl: "data:image/PNG;base64," + base64
    //     })
    //   }

    // })



    // wx.cloud.callFunction({
    //   name: 'getQRcode', // 云函数名称
    //   data: { // 小程序码所需的参数
    //     page: "pages/report/report",
    //     // id: decodeURIComponent(that.query.scene),
    //     // id:that.data.id
    //   },
    //   complete: res => {
    //     console.log('callFunction getQRcode result: ', res.result)
    //     that.setData({ // 获取返回的小程序码
    //       access_token:res.result
    //     })
    //     wx.request({
    //       url: 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=22_JKJztMLIEZlPPN7W8QeDETZ4oV2y7gGcqbZncX28wwHyG0PAJp5s6BT_czxG3N8byEwuGUbi5KGjZUPa9kD66WTPWziq__BG9Phk-2e4ln_pjlxduR4aRZWWMW8GcHGOYbybEZFp4llUF3L2RXVeAFAVBZ', //获取小程序B接口二维码
    //       method: "POST",
    //       responseType: 'arraybuffer', //这一行非常重要，重中之重
    //       data: {
    //         scene: '22a45fds',
    //         page: "pages/report/report",
    //         width: 280,
    //         is_hyaline: true
    //       },
    //       header: {
    //         'content-type': 'application/json;charset=utf-8'
    //       },
    //       success(res) {
    //         console.log('successful get QRcode:'+res.data);
    //         var base64 = wx.arrayBufferToBase64(res.data);
    //         that.setData({ 
    //           imgurl: "data:image/PNG;base64," + base64 
    //           })
    //       }

    //     })

    //   },
    //   fail: function (res) {
    //   },
    //   complete: function (res) { },
    // })


      // wx.request({
      //   url: 'https://api.weixin.qq.com/cgi-bin/token',
      //   data:{
      //     grant_type:'client_credential',
      //     appid:'wx4537dd85987be83b',
      //     secret: 'f10d099a99bb1004eeb493037e25a391'
      //   },
      //   success: function(res) {
      //    // console.log(res)
      //     that.setData({
      //       access_token: res.data.access_token
      //     })
      //     wx.request({
      //       url: 'https://api.weixin.qq.com/wxa/getwxacode',
      //       method:'POST',
      //       header: {
      //         'content-type': 'application/json'
      //       },
      //       data: {
      //         access_token: res.data.access_token,
      //         path:'pages/report/report'
      //       },
      //       success: function(res){
      //         console.log(res)
      //       }
      //     })
      //   }
      // })
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