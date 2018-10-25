use LDA to cluster tv programs in family 

This is to find family interests of tv programs


when use lda-gibbs-couple, when use tv program, tv time, tv channels as 3dimesion vector. And we set their hyper-parameter phi as 0.2,0.1,0.2, alpha as 0.2, and k as 15,8,15, max iteration 100, we get the following results:
programs clusters:

Topic 0th:
动画大放映 0.052966
新大头儿子和小头爸爸 0.049453
熊出没之熊熊乐园 0.035458
小公主苏菲亚 0.035037
新成龙历险记 0.032150
熊出没之秋日团团转 0.028903
汪汪队立大功 0.027987
猪猪侠之超星萌宠 0.027672
海底小纵队 0.027048
午间泡泡堂 0.026987
动画淘淘乐 0.022523
棉花糖和云朵妈妈 0.021675
熊出没之丛林总动员 0.018602
粉红猪小妹 0.018172
熊出没之夏日连连看 0.018171
猪猪侠之光明守卫者 0.017140
哪鹅 0.016058
巴啦啦小魔仙之飞越彩灵堡 0.014658
猪猪侠 0.014481
熊出没之奇幻空间 0.013810

Topic 1th:
人间至味是清欢 0.092818
中国新歌声第二季 0.067363
浪花一朵朵 0.059936
中餐厅 0.051082
快乐大本营 0.047273
爱情公寓四 0.043687
盲约 0.040498
我们来了第二季 0.037886
爱情公寓三 0.033355
奔跑吧兄弟第三季 0.033019
美人心计 0.031817
漂亮的李慧珍 0.031100
一起来看流星雨 0.029466
奔跑吧兄弟第四季 0.028339
奔跑吧 0.027810
中华文明之美 0.020823
楚乔传 0.020687
秋收起义 0.020378
奔跑吧兄弟第一季 0.019427
天天向上 0.019039

Topic 2th:
精彩音乐汇 0.120317
男生女生向前冲 0.065979
影视留声机 0.056637
短剧连环炮 0.030442
微微一笑很倾城 0.028403
勇敢的心 0.026466
粤唱粤好戏 0.022621
星光璀璨 0.019869
花千骨 0.019796
花红花火 0.019109
你是我的姐妹 0.018920
中国音乐电视 0.018615
反恐特战队 0.017815
全球中文音乐榜上榜 0.016662
一起音乐吧 0.016327
城事特搜 0.013894
每日新闻报 0.013796
你的爱我无力拒绝 0.013611
海峡新干线 0.013457
三生三世十里桃花 0.013347

Topic 3th:
新水浒传 0.019495
金牌调解 0.018603
英雄使命 0.013290
青年霍元甲之冲出江湖 0.012966
铁血使命 0.012511
北平无战事 0.012311
苍狼 0.011441
欢乐集结号 0.010854
卧底归来 0.010688
宜昌保卫战 0.010537
东方战场 0.010189
炮神 0.009794
福根进城 0.009156
铁血红安 0.009045
满仓进城 0.008769
说天下 0.008671
战火兵魂 0.008651
四川新闻 0.008645
大刀记 0.008492
谢谢你来了 0.008198

Topic 4th:
新闻直播间 0.573218
共同关注 0.156768
新闻30分 0.088602
朝闻天下 0.065361
法治在线 0.041106
大国外交 0.020718
法治中国 0.012881
军情时间到 0.010737
新闻周刊 0.009663
金砖国家工商论坛特别报道 0.009268
每周质量报告 0.006705
新闻调查 0.004696
全民健身日全程大直播 0.000004
爱上川菜 0.000003
美丽海岛环境预报 0.000003
少年中国国际青少年文化艺术节 0.000002
全运会火炬传递启动仪式特别节目 0.000002
你是我的姐妹 0.000002
铁掌旋风腿 0.000002
真声音 0.000002


Topic 5th:
西游记[六小龄童] 0.138140
大国外交 0.094557
远方的家 0.070504
法治中国 0.059207
亮剑 0.042301
回家吃饭 0.037053
生财有道 0.035695
舌尖上的中国第二季 0.034374
消费主张 0.032685
环球财经连线 0.031713
雍正王朝 0.030535
国宝档案 0.028704
CCTV-2第一时间 0.024715
走遍中国 0.022154
康熙王朝 0.021090
经济半小时 0.020017
交易时间（CCTV-2） 0.019682
是真的吗 0.018917
魅力中国城 0.018652
精品财经纪录 0.016744

We can see that the similar content programs are clustered togeter.


tv time clusters:

Topic 0th:
	Mon_15   0.041375
	Mon_16   0.039954
	Tue_15   0.036954
	Wed_15   0.036622
	Wed_14   0.035746
	Thu_15   0.035631
	Thu_14   0.035308
	Mon_14   0.034619
	Fri_15   0.034428
	Tue_16   0.033944
	Tue_14   0.033768
	Thu_16   0.033422
	Wed_16   0.033380
	Fri_14   0.032398
	Fri_16   0.031547
	Sat_15   0.027156
	Sat_14   0.025734
	Wed_13   0.025711
	Tue_13   0.024948
	Mon_13   0.024934

Topic 1th:
	Sun_19   0.170070
	Sat_19   0.161031
	Wed_19   0.132431
	Thu_19   0.132255
	Mon_19   0.131779
	Fri_19   0.131609
	Tue_19   0.131600

Topic 2th:
	Mon_12   0.071537
	Tue_12   0.069243
	Wed_12   0.069169
	Fri_12   0.069069
	Sat_12   0.068899
	Thu_12   0.068573
	Sun_12   0.061439
	Mon_11   0.035032
	Wed_11   0.034887
	Fri_11   0.034716
	Thu_11   0.034141
	Tue_11   0.033878
	Sat_11   0.033021
	Sun_11   0.030669
	Mon_13   0.027679
	Fri_13   0.027048
	Wed_13   0.026917
	Thu_13   0.026744
	Tue_13   0.026606
	Sun_13   0.024182

Topic 3th:
	Sun_12   0.054680
	Sun_11   0.053373
	Sun_13   0.051994
	Sun_16   0.051431
	Sun_15   0.049148
	Sun_17   0.047348
	Sun_10   0.047199
	Sun_14   0.045567
	Sat_16   0.042282
	Sat_12   0.041970
	Sat_13   0.040375
	Sat_17   0.040047
	Sat_15   0.038044
	Sat_14   0.037414
	Sat_11   0.036211
	Sat_10   0.032921
	Sat_20   0.032118
	Sun_09   0.032052
	Sun_18   0.028557
	Sat_18   0.027578

Topic 4th:
	Sat_20   0.084386
	Sun_20   0.076416
	Fri_20   0.072485
	Tue_20   0.069938
	Wed_20   0.069240
	Thu_20   0.068218
	Mon_20   0.067935
	Tue_21   0.054739
	Sun_21   0.054314
	Mon_21   0.054077
	Thu_21   0.052750
	Wed_21   0.052237
	Sat_21   0.052227
	Fri_21   0.048221
	Sun_19   0.016192
	Sat_19   0.013882
	Fri_19   0.013447
	Tue_19   0.013217
	Thu_19   0.013007
	Wed_19   0.012361

Topic 5th:
	Sat_09   0.037866
	Sat_08   0.037158
	Mon_09   0.036763
	Wed_09   0.036716
	Tue_09   0.035347
	Mon_08   0.035308
	Sun_08   0.035241
	Thu_09   0.035224
	Wed_08   0.035189
	Mon_10   0.035185
	Fri_09   0.035054
	Sun_09   0.034587
	Wed_10   0.034486
	Tue_08   0.033671
	Tue_10   0.033499
	Thu_08   0.033327
	Thu_10   0.032940
	Sat_10   0.032442
	Fri_08   0.032359
	Fri_10   0.031619

Topic 6th:
	Sat_22   0.074032
	Sun_22   0.072983
	Fri_22   0.063041
	Sun_21   0.059148
	Tue_22   0.058845
	Mon_22   0.058016
	Wed_22   0.057653
	Thu_22   0.056668
	Sat_21   0.055104
	Fri_21   0.047547
	Mon_21   0.042653
	Tue_21   0.042308
	Wed_21   0.040410
	Thu_21   0.039459
	Sat_23   0.032299
	Sun_23   0.028255
	Fri_23   0.026568
	Tue_23   0.021044
	Mon_23   0.020802
	Wed_23   0.020488

Topic 7th:
	Sun_18   0.096233
	Tue_18   0.094014
	Sat_18   0.093662
	Mon_18   0.090554
	Wed_18   0.090253
	Thu_18   0.089569
	Fri_18   0.088402
	Fri_17   0.044037
	Tue_17   0.043719
	Sun_17   0.043557
	Thu_17   0.043391
	Wed_17   0.043389
	Mon_17   0.042328
	Sat_17   0.041019

The time spans are weekday 8,9,10, weekday 11,12,13, weekday 13,14, 15,16 , weekday 17, 18, weekday 19, weekday 19,20, 21, weekday 21, 22, 23 and the weekend(sat and sun all the hours)



tv channel clusters:

Topic 0th:
四川卫视 0.212419
重庆卫视 0.160802
河北卫视 0.137206
山西卫视 0.103897
云南卫视 0.096726
贵州卫视 0.085253
甘肃卫视 0.051946
西藏卫视 0.042522
旅游卫视 0.034617
吉林卫视 0.015938
陕西卫视 0.013946
宁夏卫视 0.011504

Topic 1th:
湖南卫视 0.572018
浙江卫视 0.427977

Topic 2th:
辽宁卫视 0.170389
江西卫视 0.167173
广西卫视 0.114945
河南卫视 0.108780
青海卫视 0.089966
内蒙古卫视 0.072561
吉林卫视 0.064340
陕西卫视 0.056497
中国教育电视台一套 0.047518
新疆卫视 0.046887
宁夏卫视 0.043993

Topic 3th:
CCTV-音乐 0.360940
广东卫视 0.292275
广东南方卫视 0.196997
东南卫视 0.129165
厦门卫视 0.020611

Topic 4th:
CCTV-3 0.508136
CCTV-2 0.335261
CCTV-11 0.156598

Topic 5th:
CCTV-4 0.636849
CCTV-5 0.363148

Topic 6th:
山东卫视 0.643393
天津卫视 0.201790
湖北卫视 0.154808

Topic 7th:
东方卫视 0.636777
北京卫视 0.360763

Topic 8th:
CCTV-6 0.964069
CHC动作电影 0.024032
CHC家庭影院 0.011885

Topic 9th:
CCTV-1-综合 0.999994

Topic 10th:
CCTV-10 0.283012
CCTV-7 0.270168
CCTV-12 0.232188
CCTV-纪录 0.214627

And we also can see that the similar content tv channels are together.