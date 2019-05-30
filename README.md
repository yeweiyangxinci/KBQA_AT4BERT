# KBQA_AT4BERT
   本项目是2019年国科大知识图谱课后大作业，代码能力有限，不足之处请多多指教。
   
### 原理说明
  本项目是基于知识库上做问答，首先使用带注意力机制的对抗迁移学习做中文命名实体识别[(Cao EMNLP2019)]( http://aclweb.org/anthology/D18-1017)，然后再通过别名词典得到近义词，根据这些近义词查询Mysql数据库，得到一些三元组，这些三元组组中包括一些属性。我们先对属性与原问题进行直接字符串匹配进行查询，如不能直接匹配再使用bert做相似度计算进行属性映射，最后进行排序得到结果。整个实验原理参考[论文](http://www.doc88.com/p-9095635489643.html)，我把其中的模型进行了替换。
 
### 代码参考
  实体识别：[https://github.com/CPF-NLPR/AT4ChineseNER](https://github.com/CPF-NLPR/AT4ChineseNER)<br/>
  基于Bert做问答: [https://github.com/WenRichard/KBQA-BERT](https://github.com/WenRichard/KBQA-BERT)

### 环境配置
   ```
   python 3.6.0
   tensorFlow_gpu 1.10.0
   XAMPP版本为3.3.2
   MySQL 5.3.0
   GPU TiTan XP
   ```

### 代码目录结构
   因为git上传大小限制，其中某些模型目录我忽略了<br/>
   ```
   bert文件夹是官方下载的
   
   data文件夹存放原始数据和处理好的数据
      DB_Data: clean_triple.csv 录入数据库的三元组信息，是由triple_clean.py文件生成
      NER_Data: 里面数据是由construct_dataset.py生成
      Sim_Data: 里面数据是由construct_dataset_attribute.py生成
      NLPCC2016KBQA：是原始数据
      npy：保存的中间文件数据
      load_dbdata.py: 将数据导入mysql
      其他的都是文件输入数据
   
   ner_ckpt: 存放实体识别的模型，我已经训练好了
   
   ModelParams: 存放bert中文预训练模型chinese_L-12_H768_A-12，太大了，我上传时忽略了
   
   output: 存在相似度模型
   
   基于AT的实体识别：
      Nlpcc_model.py 
      base_model.py
      preprocess_nlpcc2016.py
      train_nlpcc2016.py
      test_nlpcc2016.py
      
   基于句子相似度的计算：
      args.py
      run_similarity.py
   
   最终KBQA模块
      kbqa_test.py
   ```
 ### 使用说明
   ```
   我的模型和数据都放在里面了，修改了mysql连接信息load_dbdata.py导入数据可以直接运行，运行kbqa_test.py即可
   
   如果想要运行自己的数据和模型，按照下面步骤：
      step1: 构建自己的实体识别模型，我的是Nlpcc2016_model.py, 运行prepocess_nlpcc2016.py
            再运行train_nlpcc2016.py训练模型，最后运行test_nlpcc2016.py生成测试集识别结果/images/AT4.png
      step2: 运行run_similarity训练bert模型
      step3: 最后运行kbqa_test.py生成最后结果
   ```
  ### 运行结果
   ||QA fully based on Bert|QA based on Bert,AT|
   |:---|:---|:---|
   |recall|9303|8639|
   |correct|8029|7566|
   |ambiguity|613|532|
   |accuracy|86.305|87.579%|
   
   ### 结果分析
   两个实验在数据集大致相等的情况下，我的实验比Bert实验准确率更高，但是总体召回率较低。我分析原因有两个方面，一方面使用对抗网络的中的LSTM比bert当中    transFormer特征提取能力要差一点，这一点，可以通过实验验证，但是使用对抗网络的实体识别准确率更高。所以后续问答实验中的准确率较高，这一点可以通过      ambiguity (属性匹配正确但是答案不正确)值较低得到验证。另外一个方面就是我训练实体识别模型还不够完善，loss是0.07停止训练，没有达到最低值。
   
   ### 未来展望
   关于相似度计算中，还可以使用其他方法来做，比如在第一步非语义匹配当中，我们是直接使用子串匹配，像比如TF-idF,BM25等等，是否会更好，有待于实验验证。    在语义计算当中，是否可以使用GCN来完成，也可以设计实验来做。
  
