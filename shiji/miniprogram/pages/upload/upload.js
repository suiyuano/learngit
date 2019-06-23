const app = getApp()

Page({  
  /**
   * 页面的初始数据
   */
  data: {
    currentdate:'',
    step: 1,
    counterId: '',
    openid: '',
    count: null,
    queryResult: '',
    currenttime:'',

    bigImg: '../../img/addimg.png',//默认图片，设置为空也可以
    user_id:null,
    index:0,
    totalprice:0,
    mtype:null,
    address:0,
    array: ['冒菜', '火锅', '串串', '烧烤','日本料理','韩国料理','烤鱼','钵钵鸡','川菜','湘菜','苍蝇馆子'],
    objectArray: [
      {
        id: 0,
        name: '冒菜'
      },
      {
        id: 1,
        name: '火锅'
      },
      {
        id: 2,
        name: '串串'
      },
      {
        id: 3,
        name: '烧烤'
      },
      {
        id: 4,
        name: '日本料理'
      },
      {
        id: 5,
        name: '韩国料理'
      },
      {
        id: 6,
        name: '烤鱼'
      },
      {
        id: 7,
        name: '钵钵鸡'
      },
      {
        id: 8,
        name: '川菜'
      },
      {
        id: 9,
        name: '湘菜'
      },
      {
        id: 10,
        name: '苍蝇馆子'
      }
      
    ]
  },

  getNowDate:function (){
    var now = new Date();
    // var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    if(month < 10) {
      month = '0' + month;
    };
    if(day < 10) {
      day = '0' + day;
    };
    //  如果需要时分秒，就放开
    // var h = now.getHours();
    // var m = now.getMinutes();
    // var s = now.getSeconds();
    var formatDate = month + '-' + day;
    return formatDate;
  } ,


  getNowTime :function () {
  // 时间
  var newDate = new Date()
  console.log(newDate)
  var h = newDate.getHours();
  var m = newDate.getMinutes();
  var s = newDate.getSeconds();
  // if (h < 10) {
  //   h = '0' + h;
  // };
  // if (m < 10) {
  //   m = '0' + m;
  // };
  // if (s < 10) {
  //   s = '0' + s;
  // };
  var time = h +'时'+ m + '分' ;
  return time;
  },


  onAdd: function (e) {
    const db = wx.cloud.database()
    db.collection('counters').add({
      data: {
        //count: 1,
        //user_id: this.data.user_id,
        type: this.data.mtype,
        location: this.data.address,
        price: this.data.totalprice,
        currentdate:this.getNowDate(),
        currenttime:this.getNowTime()
      },
      success: res => {
        // 在返回结果中会包含新创建的记录的 _id
        this.setData({
          counterId: res._id,
          count: 1
        })
        wx.showToast({
          title: '新增记录成功',
          icon: 'success',
          duration: 1000
        })
        console.log('[数据库] [新增记录] 成功，记录 _id: ', res._id)
      },
      fail: err => {
        wx.showToast({
          icon: 'none',
          title: '新增记录失败'
        })
        console.error('[数据库] [新增记录] 失败：', err)
      }
    })
  },







  changeBigImg() {
    let that = this;
    //let openid = app.globalData.openid || wx.getStorageSync('openid');
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        wx.showLoading({
          title: '上传中',
        });
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        let filePath = res.tempFilePaths[0];
        const name = Math.random() * 1000000;
        const cloudPath = name + filePath.match(/\.[^.]+?$/)[0]
        wx.cloud.uploadFile({
          cloudPath,//云存储图片名字
          filePath,//临时路径
          success: res => {
            console.log('[上传图片] 成功：', res)
            that.setData({
              bigImg: res.fileID,//云存储图片路径,可以把这个路径存到集合，要用的时候再取出来
            });
            let fileID = res.fileID;
            //把图片存到users集合表
            const db = wx.cloud.database();
            db.collection("users").add({
              data: {
                bigImg: fileID
              },
              success: function () {
                wx.showToast({
                  title: '图片存储成功',
                  'icon': 'none',
                  duration: 3000
                })
              },
              // fail: function () {
              //   wx.showToast({
              //     title: '图片存储失败',
              //     'icon': 'none',
              //     duration: 3000
              //   })
              // }
            });
          },
          fail: e => {
            console.error('[上传图片] 失败：', e)
          },
          complete: () => {
            wx.hideLoading()
          }
        });
      }
    })
  },















  bindPickerChange: function (e) {
   // console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value,
     // mtype:this.data.array[this.data.index]
    })
   // console.log(this.data.mtype)
  },
  formSubmit: function (e) {
    //console.log('form发生了submit事件，携带数据为：', e.detail.value)
    this.setData({
      totalprice:e.detail.value.input,
      mtype:this.data.array[this.data.index]
    })
  },
  //   //console.log(this.data.totalprice)
  //   //console.log(this.data.mtype)
  //   console.log(this.data.user_id)
  //   console.log(this.data.mtype)
  //   console.log(this.data.address)
  //   console.log(this.data.totalprice)
  //   wx.request({
  //     url: 'http://118.25.214.51:8080/api/postdata',
  //     method:'GET',
  //    // header:{'content-type':'application/x-www-form-urlencoded'},
  //     data:{
  //       user_id:this.data.user_id,
  //       type:this.data.mtype,
  //       location:this.data.address,
  //       price:this.data.totalprice
  //     },
  //     success: function(result){
  //       //console.log(result)
  //       wx.showToast({
  //         title: '成功上传！',
  //         icon: 'success',
  //         duration: 1000
  //       })
  //     }
  //   })
  // },
  // formReset: function () {
  //   //console.log('form发生了reset事件')
  // },






















  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.showToast({
      title: '加载中..',
      icon: 'loading',
      duration: 2000
    });

   var date=this.getNowDate()//用于测试
   console.log('date'+date)

   var time=this.getNowTime()//用于测试
   console.log("time"+time)

   console.log(options.address)
   this.setData({
     address: options.address,
     user_id: options.user_id
   })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
   
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  },
 
})