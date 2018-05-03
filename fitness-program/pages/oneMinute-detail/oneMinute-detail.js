// pages/oneMinute-detail/oneMinute-detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },
  onTapPulleydown: function () {
    wx.navigateTo({
      url: '../oneMinute-detail/Pulleydown/Pulleydown'
    })
  },
  onTapBarbellcurl: function () {
    wx.navigateTo({
      url: '../oneMinute-detail/barbellcurl/barbellcurl'
    })
  },
  onTapFlexionbrace11: function () {
    wx.navigateTo({
      url: '../oneMinute-detail/Flexionbrace11/Flexionbrace11'
    })
  },
  onTapBending12: function () {
    wx.navigateTo({
      url: '../oneMinute-detail/bending12/bending12'
    })
  }
})