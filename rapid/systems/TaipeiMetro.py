#!/usr/bin/env python
# encoding: utf-8

from rapid.libs.SystemTools import SystemTools

LINE_NODES = {}
LINE_NODES['文湖線'] = ['南港展覽館', '南港軟體園區', '東湖', '葫洲', '大湖公園', '內湖', '文德', '港墘', '西湖', '劍南路', '大直', '松山機場', '中山國中', '南京復興', '忠孝復興', '大安', '科技大樓', '六張犁', '麟光', '辛亥', '萬芳醫院', '萬芳社區', '木柵', '動物園']
LINE_NODES['淡水信義線'] = ['淡水', '紅樹林', '竹圍', '關渡', '忠義', '復興崗', '北投', '奇岩', '唭哩岸', '石牌', '明德', '芝山', '士林', '劍潭', '圓山', '民權西路', '雙連', '中山', '台北車站', '台大醫院', '中正紀念堂', '東門', '大安森林公園', '大安', '信義安和', '台北101／世貿', '象山']
LINE_NODES['新北投線'] = ['新北投', '北投']
LINE_NODES['松山新店線'] = ['松山', '南京三民', '台北小巨蛋', '南京復興', '松江南京', '中山', '北門', '西門', '小南門', '中正紀念堂', '古亭', '台電大樓', '公館', '萬隆', '景美', '大坪林', '七張', '新店區公所', '新店']
LINE_NODES['小碧潭'] = ['七張', '小碧潭']
LINE_NODES['中和新蘆線A'] = ['迴龍', '丹鳳', '輔大', '新莊', '頭前庄', '先嗇宮', '三重', '菜寮', '台北橋', '大橋頭', '民權西路', '中山國小', '行天宮', '松江南京', '忠孝新生', '東門', '古亭', '頂溪', '永安市場', '景安', '南勢角']
LINE_NODES['中和新蘆線B'] = ['蘆洲', '三民高中', '徐匯中學', '三和國中', '三重國小', '大橋頭']
LINE_NODES['板南線'] = ['南港展覽館', '南港', '昆陽', '後山埤', '永春', '市政府', '國父紀念館', '忠孝敦化', '忠孝復興', '忠孝新生', '善導寺', '台北車站', '西門', '龍山寺', '江子翠', '新埔', '板橋', '府中', '亞東醫院', '海山', '土城', '永寧']

class TaipeiMetro(SystemTools):
    def __init__(self):
        SystemTools.__init__(self, LINE_NODES)
