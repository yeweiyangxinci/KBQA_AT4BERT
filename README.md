# KBQA_AT4BERT
   本项目是2019年国科大知识图谱课后大作业，代码能力有限，不足之处请多多指教。
### 原理说明
  本项目是基于知识库上做问答，首先使用带注意力机制的对抗迁移学习做中文命名实体识别[(Cao EMNLP2019)]( http://aclweb.org/anthology/D18-1017)，然后再通过别名词典得到近义词，根据这些近义词查询Mysql数据库，得到一些三元组，这些三元组组中包括一些属性。我们先对属性与原问题进行直接字符串匹配进行查询，如不能直接匹配再使用bert做相似度计算进行属性映射，最后进行排序得到结果。整个实验原理参考[论文](http://www.doc88.com/p-9095635489643.html)，我把其中的模型进行了替换。
### 代码参考
  实体识别：[https://github.com/CPF-NLPR/AT4ChineseNER](https://github.com/CPF-NLPR/AT4ChineseNER)<br/>
  基于Bert做问答: [https://github.com/WenRichard/KBQA-BERT](https://github.com/WenRichard/KBQA-BERT)

  
