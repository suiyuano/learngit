// 云函数入口文件
const cloud = require('wx-server-sdk')
const db = cloud.database()
cloud.init()

// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()

  return await db.collection('counters').where({
    _openid: wxContext.OPENID,
  })
    .get({
      success: function (res) {
        // res.data 是包含以上定义的两条记录的数组
        console.log(res.data)
      }
    })

  // result=wx.cloud.callFunction({
  //   name: 'getTotal',
  //   data: {

  //   }
  // })
  // console.log("云函数getHprice："+result)
  // return {
  //   test:1,
  //   result:event.result,
  //   openid: wxContext.OPENID,
  //   appid: wxContext.APPID,
  //   // Hprice:max(result.price)
  // }
}