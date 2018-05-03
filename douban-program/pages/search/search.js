var API_URL='https://api.douban.com/v2/movie/search'

Page({
  data:{
    movies:[]
  },
  search:function(e){
    if(!e.detail.value){
      return;
    }
   // console.log(e.detail.value);     输出结果是你想得到的内容
   //searchcontent=str(e.detail.value)   str()未定义
   //console.log(searchcontent)
  // var search_content=e.detail.value
    wx.showToast({
      title: '加载中..',
      icon:'loading',
      duration:10000
    });
    var that=this;

    wx.request({
      url: API_URL + '?q=' + e.detail.value,
      data:{},
      header:{
        'content-type': 'application/json'
      },
      success: function (res) {
        wx.hideToast();
        var data = res.data;
       // console.log(data);
        that.setData({
          
          movies:res.data.subjects

        });
      }
    })
  }
})
