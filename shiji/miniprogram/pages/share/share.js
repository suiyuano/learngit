// pages/share/share.js

// const app = getApp();

// const auth = require('../utils/auth.js');

/// 获取倍率
const raterpx = 750.0 / wx.getSystemInfoSync().windowWidth;

/// 获取canvas转化后的rpx
const rate = function (rpx) {
  return rpx / raterpx
};
Page({
  // data: {
  //   isCreate: false,
  //   isShow: false
  // },
  data: {
    imgurl:'../../img/wxcode.jpg',
    access_token: '',
    xcxCodeImageData:null,
    id:1
  },
  
  onLoad: function (){
    // var that=this

    // wx.cloud.callFunction({
    //   name: 'getQRcode',//调用的云函数名称
    //   data: {
    //     a: 1,
    //     b: 2,

    //     // path: 'pages/report/report'
    //     // id:that.data.id
    //   }
    // }).then(res => {
    //   console.log(res.result.sum) 
    //   // console.log('call getQRcode result:'+JSON.parse(res.result));
    // })


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


  // /// 创建海报
  // createPoster: function () {
  //   // auth.writePhotosAlbum(() => {
  //   app.showLoading('正在生成...')
  //   /// 绘制的内容
  //   const writing = {
  //     bigImage: '../img/wxcode.jpg',
  //     avatar: '../img/wxcode.jpg',
  //     code: '../img/wxcode.jpg',
  //     content: '快保存并分享吧！',
  //     name: '分享食记，记录美食！'
  //   };
  //   /// 绘制
  //   this.draw('poster', 622, 882, writing).then(res => {
  //     setTimeout(() => {
  //       app.hideLoading();
  //       this.setData({
  //         isCreate: true,
  //         isShow: true
  //       })
  //     }, 300)
  //   }, err => {
  //     setTimeout(() => {
  //       app.hideLoading();
  //       app.showToast('生成海报失败');
  //     }, 300)
  //   })
  //   // });
  // },

  // /// 隐藏
  // catchtap: function (callback) {
  //   this.setData({
  //     isShow: false
  //   })
  //   setTimeout(() => {
  //     this.setData({
  //       isCreate: false
  //     })
  //     if (callback && typeof callback == "function") {
  //       callback();
  //     }
  //   }, 400)
  // },

  // /// 绘制文本
  // drawText: function (options) {
  //   /// 获取总行数
  //   var allRow = Math.ceil(options.ctx.measureText(options.str).width / options.maxWidth);
  //   /// 限制行数
  //   var count = allRow >= options.maxLine ? options.maxLine : allRow,
  //     /// 当前字符串的截断点
  //     endPos = 0;
  //   /// 设置文字颜色
  //   options.ctx.setFillStyle(options.style ? options.style : '#353535');
  //   /// 设置字体大小
  //   options.ctx.setFontSize(options.fontSize ? options.fontSize : rate(20));
  //   /// 循环截断
  //   for (var j = 0; j < count; j++) {
  //     /// 当前剩余的字符串
  //     var nowStr = options.str.slice(endPos),
  //       /// 每一行当前宽度
  //       rowWid = 0,
  //       /// 每一行顶部距离
  //       y = options.y + (count == 1 ? 0 : j * options.height);
  //     /// 如果当前的字符串宽度大于最大宽度，然后开始截取
  //     if (options.ctx.measureText(nowStr).width > options.maxWidth) {
  //       for (var m = 0; m < nowStr.length; m++) {
  //         /// 计算当前字符串总宽度
  //         rowWid += options.ctx.measureText(nowStr[m]).width;
  //         if (rowWid > options.maxWidth) {
  //           /// 如果是最后一行
  //           if (j === options.maxLine - 1) {
  //             options.ctx.fillText(nowStr.slice(0, m - 1) + '...', options.x, y);
  //           } else {
  //             options.ctx.fillText(nowStr.slice(0, m), options.x, y);
  //           }
  //           /// 保留下次截断点
  //           endPos += m;
  //           break;
  //         }
  //       }
  //     } else { /// 如果当前的字符串宽度小于最大宽度就直接输出
  //       options.ctx.fillText(nowStr.slice(0), options.x, y);
  //     }
  //   }
  // },

  // /// 绘制海报 1、canvas对象 2、canvas宽 3、canvas高 4、绘制的内容
  // draw: function (canvas, cavW, cavH, writing) {

  //   return new Promise((resolve, reject) => {

  //     if (!writing || !canvas) {
  //       reject();
  //       return;
  //     }

  //     /// 创建context
  //     var ctx = wx.createCanvasContext(canvas);
  //     ctx.clearRect(0, 0, rate(cavW), rate(cavH));

  //     /// 获取大的背景图
  //     let promise1 = new Promise(function (resolve, reject) {
  //       wx.getImageInfo({
  //         src: writing.bigImage,
  //         success: function (res) {
  //           resolve(res.path);
  //         },
  //         fail: function (err) {
  //           reject(err);
  //         }
  //       })
  //     });

  //     /// 获取店铺头像图片
  //     let promise2 = new Promise(function (resolve, reject) {
  //       if (writing.avatar == '' || !writing.avatar) {
  //         resolve('');
  //         return;
  //       }
  //       wx.getImageInfo({
  //         src: writing.avatar,
  //         success: function (res) {
  //           resolve(res.path);
  //         },
  //         fail: function (fail) {
  //           resolve('');
  //         }
  //       })
  //     });

  //     /// 获取小程序码图片
  //     let promise3 = new Promise(function (resolve, reject) {
  //       wx.getImageInfo({
  //         src: writing.code,
  //         success: function (res) {
  //           resolve(res.path);
  //         },
  //         fail: function (err) {
  //           reject(err);
  //         }
  //       })
  //     });

  //     /// 同步回调
  //     Promise.all(
  //       [promise1, promise2, promise3]
  //     ).then(res => {

  //       /// 绘制底色
  //       ctx.setFillStyle('white');
  //       ctx.fillRect(0, 0, rate(cavW), rate(cavH));

  //       /// 绘制背景图
  //       ctx.drawImage(res[0], 0, 0, rate(622), rate(628));

  //       /// 直径
  //       const diameter = rate(54);
  //       /// 圆参数 
  //       const arc = {
  //         radii: diameter / 2,
  //         x: rate(40),
  //         y: rate(800)
  //       };

  //       /// 绘制文案内容   
  //       this.drawText({
  //         ctx: ctx,
  //         str: writing.content,
  //         maxLine: 3,
  //         maxWidth: rate(366),
  //         x: arc.x,
  //         y: rate(690),
  //         height: rate(36),
  //         fontSize: rate(26)
  //       })

  //       ctx.save();

  //       /// 绘制头像
  //       ctx.beginPath();
  //       ctx.arc(arc.x + arc.radii, arc.y + arc.radii, arc.radii, 0, Math.PI * 2, false)
  //       ctx.clip();
  //       ctx.drawImage(res[1], arc.x, arc.y, diameter, diameter);
  //       ctx.restore();

  //       /// 绘制店名   
  //       this.drawText({
  //         ctx: ctx,
  //         str: writing.name,
  //         maxLine: 1,
  //         maxWidth: rate(300),
  //         x: rate(112),
  //         y: rate(836),
  //         height: rate(36)
  //       })

  //       /// 绘制小程序码
  //       ctx.drawImage(res[2], rate(458), rate(670), rate(122), rate(122));
  //       /// 绘制小程序名称 
  //       ctx.fillText("程序名", rate(488), rate(836))

  //       /// 绘制  
  //       ctx.draw(false, () => {
  //         wx.canvasToTempFilePath({
  //           canvasId: 'poster',
  //           fileType: 'png',
  //           success: res => {
  //             this.setData({
  //               poster: res.tempFilePath
  //             })
  //             resolve();
  //           },
  //           fail: err => {
  //             reject();
  //           }
  //         })
  //       });
  //     }, err => {
  //       reject();
  //     })
  //   })
  // },

  // /// 保存图片
  // btnCreate: function (obj) {
  //   app.showLoading('正在保存...')
  //   wx.saveImageToPhotosAlbum({
  //     filePath: this.data.poster,
  //     success: res => {
  //       app.hideLoading();
  //       this.catchtap(() => {
  //         wx.showToast({
  //           title: '保存成功'
  //         })
  //       });
  //     },
  //     fail: err => {
  //       app.hideLoading();
  //       this.catchtap(() => {
  //         wx.showToast({
  //           title: '保存失败',
  //           icon: 'none'
  //         })
  //       });
  //     }
  //   });
  // },



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