Page({

  /**
   * 页面的初始数据
   */
  data: {
    first_section:'深蹲',
    second_section:'箭步蹲',
    third_section:'腿举',
    fourth_section:'腿屈伸',
    fifth_section:'腿弯举',
    sixth_section:'提踵',
    seventh_section:'相扑硬拉',
    eighth_section:'臀推',
    ninth_section:'直腿硬拉',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
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
  beibu: function() {
    this.setData({
      first_section:'硬拉',
      second_section:'高位下拉',
      third_section:'引体向上',
      fourth_section:'耸肩',
      fifth_section:'杠铃划船',
      sixth_section:'哑铃划船',
      seventh_section:'仰卧上拉',
      eighth_section:'器械划船',
      ninth_section:'T杠划船',
    })
  },
  xiongbu: function () {
    this.setData({
      first_section:'俯卧撑',
      second_section:'杠铃卧推',
      third_section:'哑铃卧推',
      fourth_section:'器械推胸',
      fifth_section:'滑轮夹胸',
      sixth_section:'蝴蝶机夹胸',
      seventh_section:'哑铃飞鸟',
      eighth_section:'仰卧上拉',
      ninth_section:'双杠臂屈撑',
    })
  },
  jianbu: function () {
    this.setData({
      first_section:'杠铃推举',
      second_section:'提铃上举',
      third_section:'哑铃推举',
      fourth_section:'侧平举',
      fifth_section:'前平举',
      sixth_section:'俯身侧平举',
      seventh_section:'直立划船',
      eighth_section:'绳索面拉',
      ninth_section:'反身飞鸟',
    })
  },
  fubu: function () {
    this.setData({
      first_section:'哑铃弯举',
      second_section:'杠铃弯举',
      third_section:'滑轮弯举',
      fourth_section:'背后屈臂撑',
      fifth_section:'双杠屈臂撑',
      sixth_section:'滑轮下压',
      seventh_section:'窄距卧推',
      eighth_section:'杠铃臂屈伸',
      ninth_section:'哑铃臂屈伸',
    })
  },
  shoubi: function () {
    this.setData({
      first_section:'垂悬举腿',
      second_section:'仰卧举腿',
      third_section:'反向卷腹',
      fourth_section:'卷腹',
      fifth_section:'滑轮体前屈',
      sixth_section:'俄罗斯转体',
      seventh_section:'侧卷腹',
      eighth_section:'站姿体侧屈',
      ninth_section:'滑轮转体',
    })
  },

})