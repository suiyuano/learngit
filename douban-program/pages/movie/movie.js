var API_URL ='http://t.yushu.im/v2/movie/subject/';

Page({
  data:{
    movie:{},

  },
  onLoad:function(params){
    //console.log(params);
    var that=this
    wx.request({
      url: API_URL + params.id,
      data:{},
      header:{
        'content-type': 'application/json'
      },
      success:function(res){
        console.log(res.data)
       that.setData({
         movie:res.data
       })

      }
    })
  }
});