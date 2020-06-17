# 英语单词注音、释义与例句SQL与TSV文件
<p> 
<b>SQL_fiduplicated_SQL_filesles</b>、<b>duplicated_TSV_files</b>、<b>unduplicated_SQL_files</b>、与<b>unduplicated_TSV_files</b>压缩包（单个文件只有4个文件未超过100 MB限制，只能传压缩包了）里面分别包含了3个<b>.sql</b>或<b>.tsv</b>文件，由<b style="background-color:#FF0000;">PL/SQL</b>生成，包含了<b>150708</b>（有重复，实际为<b>144790</b>个）个单词的释义、注音（少部分单词无注音）与例句（<b><i>例句一般都不止一句</i></b>），单词的注音与释义主要来自<i><a href="https://cn.bing.com/dict/">Bing词典</a></i>，后期可能会考虑增加其他数据项。
</p>
<p> 
下表说明了各个数据表所含记录数与数据项性质。
</p>

|文件名|备注|记录数|
|-|-|-|
|duplicated_Word_Meanings_Pronounciations|含重复记录的单词、注音、释义表|150708|
|duplicated_Word_Example_Sentences|含重复记录的单词、例句表|99756|
|duplicated_word_pronounciations_meanings_example_sentences|含重复记录的单词、注音、释义、例句表|150708|
|unduplicated_Word_Meanings_Pronounciations|去重的单词、注音、释义表|144790|
|unduplicated_Word_Example_Sentences|去重的单词、例句表|99756|
|unduplicated_word_pronounciations_meanings_example_sentences|去重的单词、注音、释义、例句表|144790|
||||
<p>
不重复的单词数：144790个，有些单词仅有释义没有注音；具有例句的单词数：99756个。因为单个文件都比较大没有上传文本文件，即使上传成功直接在网页打开浏览也比较困难（更别说还有墙的限制了），因此下面这几张截图展示了3个表（均已去重）的部分数据。
<br>
<br>
<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/1.PNG"  alt="picture 1" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/2.PNG"  alt="picture 2" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/3.png"  alt="picture 3" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/4.png"  alt="picture 4" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/5.png"  alt="picture 5" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/6.png"  alt="picture 6" />
<br>
<br>

<img src="https://github.com/25thengineer/vocabulary_pronouciations_meanings_exampleSentences/blob/master/pictures/7.png"  alt="picture 7" />
<br>
<br>
</p>
<p>
希望可以給有需要的朋友一点帮助。
</p>
<p>
我在博客里面详细介绍了怎么使用爬虫获取单词注音、释义与例句以及将之导入<b style="background-color:#FF0000;">Oracle</b>数据库的过程，有兴趣的朋友可以参考如下3个博客（水平很菜，不喜勿喷）：

[收集英语单词及释义的前期准备工作](https://blog.csdn.net/u25th_engineer/article/details/105788009)

[初步处理爬取到的150708个单词的数据（原始网页文档格式，包含注音、释义与例句，等等）](https://blog.csdn.net/u25th_engineer/article/details/105828868)

[爬取并处理150708个英语单词的例句](https://blog.csdn.net/u25th_engineer/article/details/105901529)
</p>
<p>
想下载数据但访问GitHub比较慢的朋友可以下载我上传到CSDN的

[SQL文件压缩包](https://download.csdn.net/download/u25th_engineer/12391347)
与
[TSV文件压缩包](https://download.csdn.net/download/u25th_engineer/12391334)，没有CSDN下载积分的朋友也可以直接邮箱联系我（<a href="mailto:u25th_engineer@163.com?cc=2046195761@qq.com?bcc=592551037@qq.com?subject=SQL与TSV文件"> E-mail</a>）。
</p>