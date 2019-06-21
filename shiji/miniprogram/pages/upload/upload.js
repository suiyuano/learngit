Page({

  /**
   * 页面的初始数据
   */
  data: {
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
    //console.log(this.data.totalprice)
    //console.log(this.data.mtype)
    console.log(this.data.user_id)
    console.log(this.data.mtype)
    console.log(this.data.address)
    console.log(this.data.totalprice)
    wx.request({
      url: 'http://118.25.214.51:8080/api/postdata',
      method:'GET',
     // header:{'content-type':'application/x-www-form-urlencoded'},
      data:{
        user_id:this.data.user_id,
        type:this.data.mtype,
        location:this.data.address,
        price:this.data.totalprice
      },
      success: function(result){
        //console.log(result)
        wx.showToast({
          title: '成功上传！',
          icon: 'success',
          duration: 1000
        })
      }
    })
  },
  formReset: function () {
    //console.log('form发生了reset事件')
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.showToast({
      title: '加载中..',
      icon: 'loading',
      duration: 2000
    });
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