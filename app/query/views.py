from app.query import query_bp
from flask import request, abort, make_response, jsonify
from flask_restful import fields, marshal
from app.models import *
#先引入后面分析、可视化等可能用到的库
import tushare as ts
import pandas as pd
from pyecharts import kline
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False


#设置token
token='d6d118074a6897b9bf319308e0bcabe1b78dcd3ed39785b60a84bf18'
pro = ts.pro_api(token)


# 查询行情详细信息——显示个股的行情信息
@query_bp.route('/market/getMarketDetail')
def getMarketDetail():
    # 获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
    basic = pro.stock_basic(list_status='L')
    # 查看前五行数据
    # basic.head(5)

    # 获取平安银行日行情数据
    pa = pro.daily(ts_code='000001.SZ', start_date='20180101',
                   end_date='20190106')
    # pa.head()

    # K线图可视化
    pa.index = pd.to_datetime(pa.trade_date)
    pa = pa.sort_index()
    v1 = list(pa.loc[:, ['open', 'close', 'low', 'high']].values)
    t = pa.index
    v0 = list(t.strftime('%Y%m%d'))
    kline = Kline("平安银行K线图", title_text_size=15)
    kline.add("", v0, v1, is_datazoom_show=True,
              mark_line=["average"],
              mark_point=["max", "min"],
              mark_point_symbolsize=60,
              mark_line_valuedim=['highest', 'lowest'])
    # kline.render("上证指数图.html")
    kline
    return "获得市场详细信息"
