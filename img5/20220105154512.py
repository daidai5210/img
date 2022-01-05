import requests
import re


class douyinUtil:
    cookie = 'douyin.com; _ga=GA1.2.1355671542.1640830055; ttcid=6c422157d4be4c3281b90620ceab472510; ttwid=1|u0FZ41CtN3LH-7RUHhX0mJkekMoOZQoh-RNp90bGrIM|1640830072|12ee092f465f4020a39e32316bbac1798571b2b93bf6a280cd832259b6c20471; MONITOR_DEVICE_ID=e7fd790b-a16e-44e3-8c42-458e52a70ec4; MONITOR_WEB_ID=c33e26b3-ff6b-4e42-a37b-37407449e1b8; _tea_utm_cache_6383=undefined; MONITOR_WEB_ID=bbba86e0-4023-483e-9b24-4592919fdb13; _tea_utm_cache_1300=undefined; passport_csrf_token_default=7df9f3fd95e17c4a7e1bcc06719f9c15; passport_csrf_token=7df9f3fd95e17c4a7e1bcc06719f9c15; odin_tt=e788ccf35d48908e2deb1d9cbac532fca4c301c0d5d3360db97e61254c7e4ff0ce6784cb782f954c39b9e4981fb0bbfcd9ce778732237cd655136982d798a28a; THEME_STAY_TIME=299655; IS_HIDE_THEME_CHANGE=1; __ac_nonce=061d4da3d00042842398a; __ac_signature=_02B4Z6wo00f01tKSnlgAAIDDWdkFu-P.GmrStprAANV92ZJwcROJ3ahLg4ppRUkxBsM7IajbMTIeGBkAWH4MHu.VeR.g57Z.c-c7gnlOcOdxymKuxXSeVyK0BR3tMWa.CctievO-swtLPaT65f; douyin.com; AB_LOGIN_GUIDE_TIMESTAMP=1641339452405; s_v_web_id=verify_ky0r4rit_dPDzspBR_VDny_4qwA_9uhy_TZrqFHPDyNIZ; msToken=cUecsx7sLl1IK31DPkn3-K1t5ss4SAEPqE2Jrd1unQEqj0oFk-hLpjB8MLLJgmfM8hPpecw1rGIngpGrGW1JFRz42KGhoxcUDYpuWKYpUbMqYLjnDuWY7g==; theme=light; home_can_add_dy_2_desktop=1; msToken=EWuYIH-uNjSimnO0Muwi8a540V_0ogfRd3u-1_GG5HdJz5Ej-uXTDyPCzEj8TGZU9U7zQ_mxuWoZEdQSPAjFDGRihjWxpL5dJJ_fBl72-7No-U89i4V5CQ==; tt_scid=a3eOwXhVsYiBIGxdF-kwXoNkZyki8uYEw9IYgi8OZyxtROtUreBcMEVNWgwB8egx0b7a; pwa_guide_count=3'
    req = requests.Session()
    req.headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

    # 解析分享链接拿ID
    def getID(self, data):
        id = 0
        if (data.find('www') != -1):
            id = re.findall('/video/([0-9]+)', data)[0]
        else:
            url = re.findall('.*?(https://v.douyin.com/.*?/)', data)[0]
            id = re.findall('/video/(.*?)/', self.req.get(url, allow_redirects=False).text)[0]
        return id

    # 通过id拿无水印视频地址
    def getVideo(self, id):
        url = 'https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + id
        playwm = self.req.get(url).json()['item_list'][0]['video']['play_addr']['url_list'][0]
        play = playwm.replace('playwm', 'play')
        return play


# 下载单个视频
if __name__ == '__main__':
    douyin = douyinUtil()
    id = douyin.getID(input('请输入分享链接:'))
    douyin.getVideo(id)
