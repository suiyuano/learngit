var API_URL = 'http://t.yushu.im/v2/movie/top250'

Page({
  data: {
    movies:[],
    title:'加载中..'
  },
  onLoad:function(){
    var that=this;
    wx.showToast({
      title: '加载中...',
      icon:"Loading...",
      duration:10000
    });
    wx.request({
      url: API_URL,
      data:{},
      header:{
        'content-type': 'application/json'
      },
      success:function(res){
        wx.hideToast();
        var data=res.data;
        console.log(data);
        that.setData({
          title:'豆瓣电影Top250',
          movies: data.subjects

        })
      }
    })
  }
 
})
