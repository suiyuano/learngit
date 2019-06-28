const cloud = require('wx-server-sdk')
// const axios = require('axios')
// const got = require('got')
// var rp = require('request-promise');
// let appid = 'wx4537dd85987be83b'
// let secret = 'f10d099a99bb1004eeb493037e25a391'
// let msgCheckUrl = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=' //请求接口的链接
// let tokenUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret //API入口凭证

cloud.init()
exports.main = async (event, context) => {
  return {
    sum: event.a + event.b
  }
}
// 云函数入口函数

// exports.main = async (event, context) => {
//   try {
//     const result = await cloud.openapi.wxacode.get({
//       path:event.path,
//       width: 430
//     })
//     console.log(result)
//     return result
//   } catch (err) {
//     console.log(err)
//     return err
//   }
// }


// exports.main = async (event, context) => {
//   let tokenResponse = await got(tokenUrl)
//   let token = JSON.parse(tokenResponse.body).access_token
//   let checkResponse = await got(msgCheckUrl + token, {
//     path: 'pages/report/report',
//     scenr:'a=1'
//   })
//   return checkResponse.body;
// }


// exports.main = async (event, context) => {
//   console.log(event)
//   try {
//     const resultValue = await rp('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx4537dd85987be83b&secret=f10d099a99bb1004eeb493037e25a391')
//     const token = JSON.parse(resultValue).access_token;
//     console.log('------ TOKEN:', token);


//     axios({
//       url: 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=22_JKJztMLIEZlPPN7W8QeDETZ4oV2y7gGcqbZncX28wwHyG0PAJp5s6BT_czxG3N8byEwuGUbi5KGjZUPa9kD66WTPWziq__BG9Phk-2e4ln_pjlxduR4aRZWWMW8GcHGOYbybEZFp4llUF3L2RXVeAFAVBZ', //获取小程序B接口二维码
//       method: "POST",
//       responseType: 'arraybuffer', //这一行非常重要，重中之重
//       data: {
//         scene: '22a45fds',
//         page: "pages/report/report",
//         width: 280,
//         is_hyaline: true
//       },
//       header: {
//         'content-type': 'application/json;charset=utf-8'
//       },
//       success(res) {
//         console.log('successful get QRcode:' + res.data);
//         var base64 = wx.arrayBufferToBase64(res.data);
//         that.setData({
//           imgurl: "data:image/PNG;base64," + base64
//         })
//       }

//     })


//     // return ({
//     //   access_token:token
//     // })
//   //   const response = await axios({
//   //     method: 'post',
//   //     url: 'https://api.weixin.qq.com/wxa/getwxacodeunlimit',
//   //     responseType: 'stream',
//   //     params: {
//   //       access_token: token,
//   //     },
//   //     data: {
//   //       page: event.page,
//   //       width: 300,
//   //       scene: "id=" + event.id,
//   //     },
//   //   });

// //   //   return await cloud.uploadFile({
// //   //     cloudPath: 'xcxcodeimages/' + Date.now() + '.png',
// //   //     fileContent: response.data,
//   //   });
//   } catch (err) {
//     console.log('>>>>>> ERROR:', err)
//   }
// }


// const cloud = require('wx-server-sdk')
// cloud.init()
// exports.main = async (event, context) => {
//   try {
//     const result = await cloud.openapi.wxacode.get({
//       path: 'page/report/report',
//       width: 430
//     })
//     console.log(result)
//     return result
//   } catch (err) {
//     console.log(err)
//     return err
//   }
// }