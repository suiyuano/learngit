//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    address:null,
    user_id:null,
    count:1,
    userInfo: {},
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    latitude: 23.099994,
    longitude: 113.324520,
    markers: [{
      id: 1,
    }],
    covers: [{
    }, {
    }]
  },
  
  regionchange(e) {
    console.log(e.type)
  },
  markertap(e) {
    console.log(e.markerId)
  },
  controltap(e) {
    console.log(e.controlId)
  },


  
  onLoad: function () {
    var that=this
    wx.login({
      
      success: function (res) {
        var here=that
       // console.log(here.data.user_id)
        if (res.code) {
          //发起网络请求
          wx.request({
            url: 'http://118.25.214.51:8080/api/login',
            method: 'GET',
            data: {
              code: res.code
            },
            
            success: function (result) {
              
             // console.log(result.data.openid+'hhhhhhhhh')
             // console.log(here.data.user_id)
              here.setData({
                user_id: result.data.openid
              }) 
             // console.log(here.data.user_id)
              wx.request({
                url: 'http://118.25.214.51:8080/api/postcount',
                data: {
                  user_id: here.data.user_id
                },
                success: function (result) {
                  //console.log(result.data.count);
                  var data = result.data;
                  //console.log(data);
                  that.setData({
                    count: data.count
                  });

                }
              })
            }
          })
        } else {
          console.log('登录失败！' + res.errMsg)
        }
      }
    });
   /* wx.request({
      url: 'http://118.25.214.51:8080/api/postcount',
      data:{
        user_id:app.globalData.user_id
      },
      success: function(result){
        //console.log(result.data.count);
        var data=result.data;
        //console.log(data);
        that.setData({
          count: data.count
        });
       
      }
    })*/

    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
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
  },

  onReady: function (e) {
    var that=this
    this.mapCtx = wx.createMapContext('myMap');
    this.mapCtx.moveToLocation();
    this.mapCtx.getCenterLocation({
      
      success: function (res) {
        console.log(res.longitude+'一')
        console.log(res.latitude+'一')
        that.setData({
          longitude: res.longitude,
          latitude: res.latitude
        })
      }
    })
  },

  getnowLocation: function () {
    var that=this
    this.mapCtx = wx.createMapContext('myMap');
    this.mapCtx.moveToLocation();
    type: 'wgs84',
    this.mapCtx.getCenterLocation({
      success: function (res) {
        console.log(res.longitude+'二')
        console.log(res.latitude+'二')
        var getAddressUrl = "https://apis.map.qq.com/ws/geocoder/v1/?location=" + res.latitude + "," + res.longitude + "&key=O44BZ-DLB6P-A3FDW-VAYGQ-HVPG5-MRBBX&get_poi=1";
        wx.request({
          url: getAddressUrl,
          success: function (ops) {
            //console.log(JSON.stringify(ops))
            that.setData({
              address: ops.data.result.address
            })
            console.log(that.data.address)
            wx.showModal({
              title: '您当前的位置：',
              content: ops.data.result.address,
            })
          }

        })
      }


    });
    
 
    this.mapCtx.getCenterLocation({
      success: function (res) {
        console.log(res.longitude+'三')
        console.log(res.latitude+'三')

       

        /*var QQMapWX = require('../..//qqmap-wx-jssdk.js');

        // 实例化API核心类
        var demo = new QQMapWX({
          key: 'O44BZ-DLB6P-A3FDW-VAYGQ-HVPG5-MRBBX' // 必填
        });

        // 调用接口
        demo.reverseGeocoder({
          location: {
            latitude: res.longitude,
            longitude: res.latitude
          },
          success: function (res) {
            console.log(res);
          },
          fail: function (res) {
            console.log(res);
          },
          complete: function (res) {
            console.log(res);
          }
        })*/
        
        /*var latitude = res.latitude
        var longitude = res.longitude
        wx.openLocation({
          latitude: latitude,
          longitude: longitude,
          scale: 28
        })*/
      }
    })
   /* wx.request({
      url: 'http://map.qq.com/api/js?v=2.exp',
      success: function(){
              }
    })
    wx.request({
      url: 'http:// 118.25.214.51:8080/api/login',
      success: function(result){
        console.log(result.user_id)
      }
    })*/
  },
  translateMarker: function () {
    this.mapCtx.translateMarker({
      markerId: 1,
      autoRotate: true,
      duration: 1000,
      destination: {
        latitude: 23.10229,
        longitude: 113.3345211,
      },
      animationEnd() {
        console.log('animation end')
      }
    })
  },
  includePoints: function () {
    this.mapCtx.includePoints({
      padding: [10],
      points: [{
        latitude: 23.10229,
        longitude: 113.3345211,
      }, {
        latitude: 23.00229,
        longitude: 113.3345211,
      }]
    })
  },
  navigateto_upload: function() {
    wx.navigateTo({
      url: '../upload/upload'+"?address="+this.data.address+'&user_id='+this.data.user_id
    })
  }
})
