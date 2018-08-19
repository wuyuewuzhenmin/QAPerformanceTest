/**
 * Created by wuzhenmin on 2018/8/3.
 */
Page({
  data: {
    toastHidden: true,
    toastText:"",
    focus: false,
    nameInput: "",
    passWdInput: ""
  },
  toastChange: function(e) {
    this.setData({
      toastHidden:true
    })
  },
  loginButtonTap: function(e) {
    if(this.data.nameInput.length == 0 || this.data.passWdInput.length == 0){
      this.setData({
        toastText:'用户名和密码不能为空！',
        toastHidden:false
      })
    }else{
      console.log("登录")
    }

  },
  nameBindKeyInput: function(e) {
    this.setData({
      nameInput: e.detail.value
    })
  },
  passWdBindKeyInput: function(e) {
    this.setData({
      passWdInput: e.detail.value
    })
  },
  bindHideKeyboard: function(e) {
    if (e.detail.value === "123") {
      //收起键盘
      wx.hideKeyboard()
    }
  }
})