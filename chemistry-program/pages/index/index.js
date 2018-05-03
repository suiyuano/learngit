var index_api_url= 'http://t.yushu.im/v2/movie/top250'
var search_api_url=''

Page({
  data: {
    movies: [],
    //title: '加载中..'
  },
  onLoad: function () {
    var that = this;
    wx.showToast({
      //title: '加载中...',
      icon: "Loading...",
      duration: 10000
    });
    wx.request({
      url: index_api_url,
      data: {},
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        wx.hideToast();
        var data = res.data;
        console.log(data);
        that.setData({
         // title: '创意化学精品视频',
          movies: data.subjects

        })
      }
    })
  },
  search: function (e) {
    if (!e.detail.value) {
      return;
    }
    // console.log(e.detail.value);     输出结果是你想得到的内容
    //searchcontent=str(e.detail.value)   str()未定义
    //console.log(searchcontent)
    // var search_content=e.detail.value
    wx.showToast({
      title: '加载中..',
      icon: 'loading',
      duration: 10000
    });
    var that = this;

    wx.request({
      url: search_api_url + '?q=' + e.detail.value,
      data: {},
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        wx.hideToast();
        var data = res.data;
        // console.log(data);
        that.setData({

          movies: res.data.subjects

        });
      }
    })
  }

})
