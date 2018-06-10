Page({

  /**
   * 页面的初始数据
   */
  data: {
    askfronttrain1:null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
   /* wx.request({
      url: 'http://118.24.184.17:8880/static/weapp/picture/ask-front-train-1.png',
      success: function(res){
        console.log(res)
      }
    })*/
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
  training_1: function(){
    wx.navigateTo({
      url: './training/page1/page1',
    })
  },
  training_2: function () {
    wx.navigateTo({
      url: './training/page2/page2',
    })
  },
  training_3: function () {
    wx.navigateTo({
      url: './training/page3/page3',
    })
  },
  training_4: function () {
    wx.navigateTo({
      url: './training/page4/page4',
    })
  },
  diet_1: function () {
    wx.navigateTo({
      url: './diet/page1/page1',
    })
  },
  diet_2: function () {
    wx.navigateTo({
      url: './diet/page2/page2',
    })
  },
  diet_3: function () {
    wx.navigateTo({
      url: './diet/page3/page3',
    })
  },
  diet_4: function () {
    wx.navigateTo({
      url: './diet/page4/page4',
    })
  },
  others_1: function () {
    wx.navigateTo({
      url: './others/page1/page1',
    })
  },
  others_2: function () {
    wx.navigateTo({
      url: './others/page2/page2',
    })
  },
  others_3: function () {
    wx.navigateTo({
      url: './others/page3/page3',
    })
  },
  others_4: function () {
    wx.navigateTo({
      url: './others/page4/page4',
    })
  },
})