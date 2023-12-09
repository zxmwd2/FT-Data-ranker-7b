# FT-Data-ranker-7b
FT-Data-ranker-7b赛道第四名方案
# 主要思路
比赛期间尝试了很多方法，后来发现，大道至简，对结果提升效果明显的有两个做法有两个，一个调整中英文的比例，二是限制output的长度。其它的数据处理的设置与官方baseline的完全一致。
# 中英文比例的调整
经过一系列试验，最终发现英文token占总token数的80%效果最好，各比例的实验结果如下图所示
![image](https://github.com/zxmwd2/FT-Data-ranker-7b/assets/74773596/9a5b5198-a298-4cef-a316-9b95012f5369)
# 对output长度的限度
经过探索发现，限制超短output长度的文本，对提升摘要任务得分效果明显。分别分析中英文数据Output长度的分布后，做了不同分位点的截断实验，具体的实验结果如下
![image](https://github.com/zxmwd2/FT-Data-ranker-7b/assets/74773596/a1edcd10-4087-49d9-be00-ad9e2ec58001)
