# FT-Data-ranker-7b
FT-Data-ranker-7b赛道第四名方案
# 主要思路
比赛期间尝试了很多方法，包括但不限于基于困惑度过滤、去重、基于信息熵的过滤、基于关键词匹配的清洗、对文档质量进行排序。后来发现，大道至简，对结果提升效果明显的有两个做法有两个，一个调整中英文的比例，二是限制output的长度。其它的数据处理的设置与官方baseline的完全一致。
# 中英文比例的调整
经过一系列试验，最终发现英文token占总token数的80%效果最好，各比例的实验结果如下图所示
![image](https://github.com/zxmwd2/FT-Data-ranker-7b/assets/74773596/9b3e9a16-19d5-4409-a4cc-0c458a3d0b18)

# 对output长度的限度
经过探索发现，限制超短output长度的文本，对提升摘要任务得分效果明显。分别分析中英文数据Output长度的分布后，做了不同分位点的截断实验，具体的实验结果如下
![image](https://github.com/zxmwd2/FT-Data-ranker-7b/assets/74773596/cf54bb53-224a-4e18-9df8-8e7fd957b835)

