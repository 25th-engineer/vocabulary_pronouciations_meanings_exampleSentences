# 英语单词注音、释义与例句SQL与TSV文件
[原README文件](./README_old.md)。
<p> 
文件夹<b><i>old_SQL_TSV</i></b>下的<b>SQL_fiduplicated_SQL_filesles</b>、<b>duplicated_TSV_files</b>、<b>deduplicated_SQL_files</b>、与<b>deduplicated_TSV_files</b>压缩包（单个文件只有4个文件未超过100 MB限制，只能传压缩包了）里面分别包含了3个<b>.sql</b>或<b>.tsv</b>文件，由<b style="background-color:#FF0000;">PL/SQL</b>生成，包含了<b>150708</b>（有重复，实际为<b>144790</b>个）个单词的释义、注音（少部分单词无注音）与例句（<b><i>例句若有，一般都不止一句</i></b>），单词的注音与释义主要来自<i><a href="https://cn.bing.com/dict/">Bing词典</a></i>。
</p>

<p> 
下表说明了各个数据表所含记录数与数据项性质。
</p>

|文件名|备注|记录数|
|-|-|-|
|duplicated_Word_Meanings_Pronounciations|含重复记录的单词、注音、释义表|150708|
|duplicated_Word_Example_Sentences|含重复记录的单词、例句表|99756|
|duplicated_word_pronounciations_meanings_example_sentences|含重复记录的单词、注音、释义、例句表|150708|
|deduplicated_Word_Meanings_Pronounciations|去重的单词、注音、释义表|144790|
|deduplicated_Word_Example_Sentences|去重的单词、例句表|99756|
|deduplicated_word_pronounciations_meanings_example_sentences|去重的单词、注音、释义、例句表|144790|
<br>

<p>
不重复的单词数：144790个，有些单词仅有释义没有注音；具有例句的单词数：99756个。因为单个文件都比较大没有上传文本文件，即使上传成功直接在网页打开浏览也比较困难（更别说还有墙的限制了），因此下面这7张截图展示了3个表（均已去重，注音未单独成字段）的部分数据。
</p>
<br>
<br>

![picture 1](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114048578-830175588.png)
<br>
<br>

![picture 2](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114102632-662284431.png)
<br>
<br>

![picture 3](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114114447-1745385117.png)
<br>
<br>

![picture 4](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114157257-172852155.png)
<br>
<br>

![picture 5](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114208418-1291746403.png)
<br>
<br>

![picture 6](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114217082-1975801726.png)
<br>
<br>

![picture 7](https://img2020.cnblogs.com/blog/830478/202006/830478-20200617114256019-77732933.png)
<br>
<br>

---
___
***

<p>在上述的几个表中，注音（若有）与释义合为一个字段，不利于后续应用，遂将注音单独列为一个字段，释义为另一字段。<b style="background-color:#FF0000;">Python</b>处理生成的<b>.tsv</b>文件分别为：<b>1_with_pronunciations</b>、<b>2_without_pronunciations</b>、<b>3_combined_version_sorted_by_consecutive_IDs</b>、<b>4_combined_version_sorted_by_nonconsecutive_IDs</b>与<b>5_combined_version_sorted_by_alphabet</b>，<b style="background-color:#FF0000;">MySQL Workbench</b>生成的<b>.sql</b>文件分别为：<b>English_Vocabulary_consecutive_IDs</b>和<b>English_Vocabulary_nonconsecutive_IDs</b>，<i><u>这两个<b>.sql</b>文件均可直接导入<b>MySQL</b>数据库</u></i>。<br>
新文件均放置于文件夹<b><i>new_SQL_TSV</i></b>中，每个文件的具体内容参见下面的表格。
</p>

|文件名|备注|记录数|
|-|-|-|
|1_with_pronunciations|去重的含注音单词及其释义与例句表（TSV，注音单独成字段）|91854|
|2_without_pronunciations|去重的无注音单词及其释义与例句表（TSV）|52936|
|3_combined_version_sorted_by_consecutive_IDs|去重的按连续ID排序的单词、注音、释义、例句表（TSV，注音单独成字段）|144790|
|4_combined_version_sorted_by_nonconsecutive_IDs|去重的按不连续ID排序的单词、注音、释义、例句表（TSV，注音单独成字段）|144790|
|5_combined_version_sorted_by_alphabet|去重的按连续单词字典序排序的单词、注音、释义、例句表（TSV，注音单独成字段）|144790|
|English_Vocabulary_consecutive_IDs|去重的按连续ID排序的单词、注音、释义、例句表（MySQL，可直接加载导入数据库，注音单独成字段）|144790|
|English_Vocabulary_nonconsecutive_IDs|去重的按不连续ID排序的单词、注音、释义、例句表（MySQL，可直接加载导入数据库，注音单独成字段）|144790|
<br>
<p><b>PS</b>：所谓“连续ID”指的是ID字段的所有数据项都是从1开始连续递增，而“不连续ID”指的是ID字段的某些数据项并非连续递增。
</p>

<p>
以下的4张图展示的表内容均已将注音与释义分割。
</p>

![picture 8](https://img2022.cnblogs.com/blog/830478/202205/830478-20220529153132312-2035110738.png)
<br>
<br>

![picture 9](https://img2022.cnblogs.com/blog/830478/202205/830478-20220529153157107-1314931506.png)
<br>
<br>

![picture 10](https://img2022.cnblogs.com/blog/830478/202205/830478-20220529153210699-2066869754.png)
<br>
<br>

![picture 11](https://img2022.cnblogs.com/blog/830478/202205/830478-20220529153225053-1941985835.png)
<br>
<br>

<p>
MySQL数据表的字段组成如下表所示。
</p>

| **Field**         | **Type**      | **Null** | **Key** | **Default**       | **Extra**   |                                  
|-------------------|---------------|----------|---------|-------------------|------------------------------------------------|
| id                | int unsigned  | NO       | PRI     | NULL              | auto_increment                                 |
| word              | varchar(50)   | NO       |         | NULL              |                                                |
| pronunciation     | varchar(100)  | YES      |         | NULL              |                                                | 
| meaning           | varchar(500)  | NO       |         | NULL              |                                                |
| EXAMPLE_SENTENCES | varchar(2500) | YES      |         | NULL              |                                                |
| create_time       | datetime      | YES      |         | CURRENT_TIMESTAMP | DEFAULT_GENERATED                              |
| update_time       | datetime      | YES      |         | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP  |

<p>
下面的文本展示了了数据表导出文件的前20行。
</p>

```
id,word,pronunciation,meaning,EXAMPLE_SENTENCES,create_time,update_time
1,vroomed,美[vrum]，英[vruːm]，,"n. 弗鲁； v. 〈口〉发弗鲁声； 网络释义： 弗鲁姆；弗罗姆；期望理论；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
2,christenings,美['krɪs(ə)nɪŋ]，英['krɪs(ə)nɪŋ]，,"n. 施洗礼仪式；命名仪式； v. “christen”的现在分词； 网络释义： 受洗记录；","When he saw the door of a church hung in black, he entered: he sought out funerals as other men seek christenings.<br>他一看见天主堂门口布置成黑色，总走进去。他探访丧礼，正如别人探访洗礼。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
3,pylons,美['paɪ.lɑn]，英['paɪlən]，,"n. 【航】(飞机场的)标塔；标杆；硬式飞艇的螺桨架；支架； 网络释义： 水晶塔；塔门；架线塔；","On the whole, the sequence of midspan to pylons seems to be more favorable with respect to the wind stability.<br>从总体抗风稳定性而言，主梁采用从中跨跨中向两侧桥塔对称拼装的施工顺序则比较有利。<br>I get my gun, and if I can blow out one of these pylons, all of you run as fast as you can for the Sekiton storage bunker!<br>我去拿枪，要是我能轰掉一个铁塔，你们就跑向那个塞基顿地堡仓库，越快越好！<br>Sometimes it would be pylons, sometimes states, but it was always something that demanded his undivided attention.<br>他谈论这些东西时，兴致勃勃，有时候谈论架线塔，有时候谈论美国的洲，但是总是需要他全神贯注的东西。<br>On top of that you've got the masts, that's another 280ft, so it's 1, 120ft from the bottom of the valley to the top of the pylons.<br>其上的桅杆又有280英尺，故从河谷底部到桥的最高部共1120英尺。<br>A few modified survivors continue to perform to this day in a very different role, racing around the pylons at the Reno Air Races.<br>一些修改幸存者继续履行这一天在一个非常不同的作用，各地的赛车在里诺塔空气比赛。<br>Liam Fox, the Conservative defence secretary, says he is opposing the building of electric pylons in his own rural constituency.<br>保守党国防部长LiamFox说，他反对在他自己的乡村选区建设电塔。<br>The latest generation of electricity pylons are, in the eyes of some, at least, things of beauty in their own right.<br>在一些人眼里，这最新一代的电力高压线塔至少可体现出一种美来。<br>It is also necessary to integrate infrastructure needs of the cities, like pylons, sewage plants, etc. into peripheral landscapes.<br>同时将架线塔、污水处理厂等城市基础建设的需求整合到城郊景观中也是必要的。<br>They work excellent against grouped up units as well as stationary defenses and hitting strategic locations like choke points and pylons.<br>他们在对付成队的单位和固定防御都很有效，打击战略位置像是路口和神族水晶塔。<br>Electricity is transmitted from the power station to your home . it travels through large cables supported by pylons or buried underground.<br>电力从发电站经由输电塔或地下的电缆，输送到我们家里去。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
4,fumarole,,"n. 【地】(火山区的)喷气坑； 网络释义： 喷气孔；火山喷气孔；火山喷孔；","A fumarole is a vent, usually volcanic, from which gases and vapors are emitted; it is characteristic of a late stage of volcanic activity.<br>翻译成中文为：喷气孔通常为火山喷气出口，从这个孔中火山气体和蒸汽喷射出来，为火山晚期阶段的特征。<br>It is sometimes described by the composition of its gases, e. g. chlorine fumarole.<br>有时喷气孔可以根据其气体的组成进行描述，如：氯气喷气孔。<br>A vacuum pump, housed in a rusty ammo box, captured a fumarole's plume.<br>一个生锈盒子里装着一台真空泵，用来捕获喷气孔冒出的烟羽。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
5,fasciated,美['fæʃɪeɪtɪd]，英['fæʃɪeɪtɪd]，,"adj. 扁化的；带状的；带化的如鸡冠花等；成束的； 网络释义： 束住的；用带子束住的；","Bracts narrowly fasciated, nearly equaling sepals, glabrous or abaxially pilose.<br>2 (1) Leaflets of radical leaves fasciated oblong to fasciated lanceolate, base subcordate or rounded to broadly cuneate.<br>胚根的小叶把扁化的长圆形留给扁化披针形，基部近心形或圆形到宽楔形。<br>Bract 3-parted with segments fasciated;<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
6,horehound,美['hoʊrˌhaʊnd]，英['hɔːhaʊnd]，,"n. 普通夏至草 (Marrubium vulgare)；夏至流浸膏； 网络释义： 苦薄荷；天然苦薄荷；苦汁薄荷；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
7,acquiesced,美[.ækwi'es]，英[.ækwi'es]，,"v. 默许； 网络释义： 默认；默许了；承诺；","Lowering his head and biting his lip, he acquiesced the other man's plea to bed with him.<br>低着头，咬着唇，他勉强应允了男人的求欢。<br>Grace acquiesced, went in and sat down close to the door.<br>格雷斯默默地同意了，走进了房间，在靠近门边的地方坐下来。<br>She acquiesced, however, and he took her name and address.<br>但她还是同意了，他就记下了她的名字和地址。<br>Henceforward he was more or less a husk . And he half acquiesced , as so many men do , yielding their place to their children .<br>从此他多少成了个没用的空壳，他只得象好多男人一样有点儿认命了，让位给了孩子们。<br>Well, I acquiesced in the bottom of my heart, I wish you future is unbounded.<br>Some of the industries that are now complaining so strongly about import competition have acquiesced to cost structures.<br>现在如此强烈地抱怨进口竞争的一些工业，已经默认了成本结构。<br>I am anxious very much, but I or classics do not live of the husband beg for leniency repeatedly, acquiesced in his aggression eventually.<br>我很担忧，但我还是经不住丈夫的再三求情，终于默许了他的进攻。<br>Though I wasn't enthusiastic about Tom's plan to go fishing, I acquiesced in it because there seemed nothing else to do.<br>虽然我不怎么热衷于汤姆钓鱼的计划，但我还是同意了，因为似乎没什么别的事可做。<br>NOTE: Secrecy creates a very restrictive atmosphere and it should be requested or acquiesced to only under special circumstances.<br>注意：保密创造一种非常有限的谈判气氛，因此只有在特殊的情况下才能要求默许这种谈判方式。<br>Cummer is ground forcedly via removing me to tangle to death, acquiesced.<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
8,implication,美[.ɪmplɪ'keɪʃ(ə)n]，英[.ɪmplɪ'keɪʃ(ə)n]，,"n. 含意；可能的影响（或作用、结果）；暗指；（被）牵连； 网络释义： 暗示；含义；蕴涵；","The implication of governance conception emerged that referred to a new change notion of administration reform in public sector.<br>概念的出现，意味著政府部门从事改革思维的一种演变。<br>She said very little but a great deal by implication.<br>One implication of such a process may be that the overpayment of a top executive has higher costs than have previously been realized.<br>这样一个过程意味着，高层管理人员薪水过高所付出的代价可能要比先前所认识到的更高。<br>The implication or allegation by opposing counsel would be that this constituted a wink and a nod to the interrogators.<br>控方律师会指控或者暗示这构成了一个对发问者眨眼或是点头的形势。<br>What is the social cost of that -- not to mention the implication for the next generation of mortgage brokers?<br>什么是社会成本？更不用说抵押贷款经纪人的下一代受到的影响？<br>If I had not adopted the mysterious implication, that meant I was deficient in the perception of life.<br>如果我未曾接受神秘的暗示，说明我缺少生命的悟性。<br>I decided to remove myself from my computer and the implication that I might be on the verge of a good idea.<br>我决定让自己远离电脑，不再让自己被“下一刻我就会有好想法”的想法牵绊。<br>He made a polite implication that he was going to leave.<br>Klinger warns: "It's easy to take the policy implication too far and start trying to pick and choose where to settle in the product space. "<br>科林格提醒道：“人们很容易把政策含意理解得过远，开始尝试在产品空间中挑选栖身之地。”<br>Autumn mood to let the viewer understand the implication of the truth of life: "smile, the face of life" !<br>秋色的心情能够让观赏者明白生活所蕴涵的真理：“微笑着面对生活”！<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
9,grimoires,,"网络释义： 魔法之书；中世纪巫术之书；魔典；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
10,subreptitious,,"网络释义： 隐瞒事实的；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
11,demipique,,"网络释义： 低鞍头战鞍；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
12,scamper,美['skæmpər]，英['skæmpə(r)]，,"n. 奔跑；匆匆忙忙旅行[浏览,涉猎]； v. 欢快地奔走；蹦蹦跳跳； 网络释义： 疾走；奔跳；奔驰法；","And, discerning the scarlet letter on her breast, would scamper Off with a strange, contagious fear.<br>待到看清她胸前的红字，便怀着一种害怕受到传染的奇异的恐惧，迅速逃开了。<br>And sometimes, when oliver walked softly into a room, the mice would scamper across the floor, and run back terrified to their holes.<br>有时候，奥立弗轻手轻脚走进一间屋子，会看见老鼠在地板上窜来窜去，惊慌不迭地跑回洞里。<br>Bundles of candles were procured, and straightway there was a general scamper up the hill.<br>一捆捆蜡烛拿了出来，大家立即欢快地开始爬山。<br>"You shall see, " replied the Ogre, and in an instant he became a mouse and began to scamper about the floor.<br>“让你见识一下”怪物说道，瞬间，他就变成了一只老鼠，还在地上快速地跑着。<br>Outweighed and out-numbered, the foxes scamper away, leaving the carcass to be stripped clean by the condors .<br>美餐一顿之后，灰狐狸蹦蹦跳跳的跑开了，尸体则被兀鹰啄食干净。<br>During the intermission, cameramen and eager fans raced after speakers, several of whom chose to scamper into the bathroom for cover.<br>在会议的间隙，摄影师，热情的粉丝追逐着嘉宾，他们中一些人不得不选择奔跑的方式进入盥洗室。<br>Stray dogs scamper through the nursery and toddlers are being weighed in the corner while food is passed around.<br>发放食物时，流浪狗也会欢蹦乱跳的穿过托儿所。<br>The message is in family philtrum get about, immediately scamper opened boiler, all kin think method to search.<br>消息在全家人中传开，顿时炸开了锅，所有亲戚都想尽办法去找。<br>How to scamper its way, if don't use some means, also be not crushed sole of foot by this stem servant girl to go.<br>怎么可以顺其自然，要是不使出点手段来，还不被这一干丫鬟踩到脚底下去了。<br>Indeed, our galaxy is so huge that dozens of lesser galaxies scamper about it, like moons orbiting a giant planet.<br>我们的银河系实在庞大，吸引着数十个较小的星系环绕着它奔跑，恰似环绕巨大行星旋转的卫星。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
13,duellist,美[d'juəlɪst]，英[d'ju:əlɪst]，,"n. 决斗者；斗争者；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
14,zeppelin,美['zep(ə)lɪn]，英['zepəlɪn]，,"n. 齐伯林飞船； 网络释义： 齐柏林；齐柏林飞艇；齐柏林飞船；","Spanish police Friday said they had foiled a plot to use a zeppelin airship to help a prisoner break out of a jail on the Canary Islands.<br>西班牙警方3日表示，他们挫败了一起企图利用遥控齐柏林飞艇帮助囚犯从加那利群岛的一所监狱越狱的阴谋。<br>I thought this was all allegorical until I saw you crawl from that flaming zeppelin wreckage unscathed.<br>当我看到你毫发无损的从那个熊熊燃烧的遇难飞艇里爬出来的时候我认为这一切都是有寓意的。<br>The structure also demands a single door with a clear opening of 100 meter by 100 meter to let the zeppelin go in and out.<br>结构还要求一个单独的一百乘以一百的可供飞船进出的入口；<br>Some academics believe the Zeppelin is real but it has also been suggested the aircraft is an early example of animation puppetry.<br>一些学者相信这个齐柏林飞艇是真的，但是它也显示这个飞行器只是早期电影动画道具的一个样本。<br>The only new air unit is the Airship, a sub-spotting, navy-busting zeppelin that should definitely help keep your coasts clear.<br>唯一的新空军是空艇，像齐柏林飞艇那样可以控制海岸，侦查潜艇。<br>Korean giant Samsung Construction and Trading commissioned the designer to elaborate upon the concept as a luxury zeppelin.<br>韩国企业巨头三星公司委托设计师详尽地描绘了其作为一个豪华飞艇的概念。<br>When the 100-meter sprinters were introduced, the audience exploded with an applause that would make a Led Zeppelin concert seem civil.<br>100米短跑运动员们进入赛场时，观众席上爆发出雷鸣般的掌声。这掌声使LedZeppelin音乐会也逊色几分。<br>Its relationship with Spencer Gifts led to the chain carrying Led Zeppelin's Mothership compilation album.<br>它与SpencerGifts的关系使得该零售连锁商承销了LedZeppelin乐队的精选辑《Mothership》。<br>Led Zeppelin broke up in the early '80s.<br>The game includes innovative and controversial ads: a zeppelin flies overhead promoting the Yu Ting brand of contraceptives.<br>这款游戏包含一些有创意和有争议的广告：对避孕药品牌毓婷的过度宣传。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
15,brochures,美[broʊ'ʃʊr]，英['brəʊʃə(r)]，,"n. 假钉本； 网络释义： 小册子；手册；招生简章；","Folks who used to provide goods and services to me started to hire me to do their marketing, advertising and brochures,  Cordes says.<br>过去那些为我提供货物和服务的人们开始聘请我为他们做市场营销、广告和宣传册。<br>It was a terrible mess with hundreds of brochures all over the path in front of me!<br>这是一个可怕的烂摊子的小册子数百各地在我前面的道路！<br>The man sat down and started trying to pick all of the brochures up.<br>该名男子坐了下来，并开始尝试挑选的小册子都放弃了。<br>If she's got any marketing talent at all, she'd know pretty darn quick when Hurd's attention changed from her brochures to her brassieres.<br>如果她有点营销天赋的话，当赫德的兴趣从她的宣传册转移到她的内衣时，她就知道该做些什么了。<br>No doubt most of them boarded the buses; with farm brochures in hand to leave determined that they, too, would one day own Arabian horses.<br>毫无疑问，其中大部分登上巴士，与农场宣传册在手，他们决定离开，也有一天会自己的阿拉伯马。<br>I would appreciate any corporate brochures or marketing materials with which you could provide me.<br>如果您能将一些可以公布的公司简介或市场销售资料提供给我，将不胜感激。<br>Travel brochures can only give limited information, so ask the travel agent as many questions as you can think of -- it's your money.<br>旅游指南只能给你有限的信息，所以应该尽量询问旅行社相关的问题--毕竟是你在花钱。<br>When he first met with prospective clients, he never used PowerPoint presentations nor prepared brochures to leave behind after he left.<br>当他第一次见客户的时候，他既没有使用PPT做演示，也没有准备产品手册留给客户。<br>Look through brochures, magazines and maps and gather a few that look interesting an that you think your whole family would enjoy.<br>查阅小册子，杂志，和地图，收集一些有趣的可以令家人开心的旅游信息。<br>PUT aside the cruise brochures and let the garden retain that natural look for a few more years.<br>先将海上巡游的宣传册放一放，让花园的自然面貌多保持几年吧！<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
16,slather,美['slæðər]，英['slæðə(r)]，,"v. 大量耗用；挥霍； n. 〈美俚〉大量； 网络释义： 厚厚地涂；大量使用；大量地用；","Slather on your sunscreen at least 20 minutes before you head out for your run. Your skin needs time to absorb the lotion.<br>在你出发之前至少20分钟就涂抹防晒霜，因为你的皮肤需要一定的时间去吸收它。<br>Yogurt and Waffles. Slather Greek yogurt on whole-wheat frozen toaster waffles and top with blueberries for a delicious twist.<br>酸奶和维夫饼干。将希腊酸奶的全麦烤华夫饼干涂上冷冻与美味的蓝莓。<br>It's no longer enough to simply slather some creamy concoction on dry skin.<br>抗衰老已不再只是简单往干燥皮肤上擦面霜了。<br>Mike: Let's not buy that ubiquitous barbeque sauce that people always slather all over their meat.<br>我们不要买人们经常会在肉上涂满的那种普通的沙茶酱。<br>Slather yourself with body lotion . This feels good and also, if you're having trouble sleeping because you're hot , it cools you down.<br>涂身体润肤乳。这能带来好的感觉而且如果因为太热而睡不着它能降温。<br>Toast whole wheat bread, slather with almond butter or peanut butter, and then sprinkle flaxseeds on top.<br>用全麦吐司面包，涂上奶油杏仁或花生酱，然后洒上亚麻籽。<br>Noon - Slather on the sunscreen and go for a swim in the ocean.<br>中午--抹上厚厚的一层防晒霜，在海中畅游一番吧。<br>"I slather it on my face, hands and feet on flights. It is a very hard-working cream. "<br>“乘飞机的时候，我把它厚厚地抹在脸上、手上和脚上。这是一种很管用的护肤霜。”<br>Slather mixture onto damp hair and gently massage into hair from roots to ends.<br>将混合物涂抹在湿头发上，轻轻地按摩，让其从发根到发梢充分滋润。<br>Slather yourself with sunscreen before you leave home.<br>在你出家门之前在身上涂一层厚厚的防晒霜。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
17,appalachians,英[ˌæpəˈleitʃɪənz]，,"n. 阿帕拉契山脉； 网络释义： 阿巴拉契亚山脉；伽亚山脉；阿巴拉契亚族；","I was raised among earnest hard-working Appalachians whose prime directive was not to put other people to any trouble.<br>我生长在艰苦的阿巴拉契亚山地区，祖训是不要给别人添麻烦。<br>I cannot find anywhere though: how will the Karst topography along hillsides of the Appalachians behave during the New Madrid release?<br>虽然我到处都找不到：在新马德里断层带释放压力期间，沿着阿巴拉契亚山区山坡的卡斯特地形会怎么样？<br>The British Proclamation of 1763 ordered a halt to the westward movement at the Appalachians, but the decree was widely disregarded.<br>英国的1763年公告命令在阿巴拉契亚山脉停止西进运动，但是这个法令被广泛无视。<br>The animation shows a series of thunderstorms coalescing as the fast-moving front travels from the Appalachians toward the Mid-Atlantic.<br>该动画展现了一连串的雷暴聚结由阿帕拉契山脉向大西洋中部快速移动。<br>Down the east coast of the us is a range of mountains , the appalachians.<br>沿美国的东海岸有一条山脉，叫阿包拉契亚山脉。<br>The Appalachians run slightly from the northeast to southwest and the Rocky mountains run slightly from the northwest to southeast.<br>阿巴拉契亚山脉的走向是从东北到西南，落基山脉则是从西北到东南。<br>The rivers flowing west from the Appalachians are fed not only by melting snow in spring, but also by rain throughout the year.<br>从阿巴拉契亚山向西奔流的江河中，不仅流淌着春季冰雪消融时的雪水，而且全年都有雨水汇入。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
18,arsenide,美[ɑ:'senaɪd]，英[ɑ:'senaɪd]，,"n. 砷化物； 网络释义： 砷盐；","Gallium arsenide, silicon, and germanium are all examples of semiconductors, the type of material used in virtually all modern electronics.<br>镓砷化物，硅，和锗元素都属于半导体，而如今半导体在所有的现代电子元件中都会用到。<br>Lattice defects in a compound semiconductor, gallium-arsenide are evaluated by two-dimensional nutation nuclear magnetic resonance.<br>晶格缺陷的化合物半导体，镓砷化评价二维章动核磁共振。<br>This protects the rigid gallium arsenide components from strain, but the system as a whole is flexible and stretchable.<br>这样就可以避免张力对于砷化镓元件损伤，但整个系统却表现出一种柔性。<br>Toproducetheelectron beam, a laser will fire at a target made of gallium arsenide, knocking off billions of electronswitheach pulse.<br>产生电子射束的方法，是利用一道雷射轰击用砷化镓制成的标靶，每个脉冲会打出几十亿个电子。<br>Silicon, germanium and gallium arsenide are popular materials used in ICs and semi-conduct devices, while silicon is the most popular one.<br>集成电路和各种半导体器件制造中所用的材料，目前主要是硅、锗和砷化镓等单晶体，其中又以硅为最多。<br>Use in manufacturing of glass, enamels and lead crystals, raw material for arsenic alloys, arsenide semiconductors, wood preservative.<br>Gallium arsenide metal semiconductor field effect transistor .<br>Single crystal gallium arsenide is a new semiconductor material has developed after germanium and silicon.<br>单晶砷化镓材料是继锗、单晶硅之后发展起来的新一代半导体材料。<br>Each panel contains small lenses that concentrate sunlight by 400 times onto strips containing gallium arsenide photovoltaic cells.<br>每块板上包含的把可以太阳光浓缩400倍的小晶体，主要成分是砷化镓光电池。<br>The crystal layer on early LEDs was gallium arsenide or gallium phosphide, which lent that reddish color.<br>早期LED的液晶层是砷化镓或者磷化镓做的，所以发出红光。<br>
","2022-05-29 11:29:56","2022-05-29 11:42:01"
19,moops,,"网络释义： 怪物世界保卫战；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
20,bungay,,"un. 邦加(英格兰东南部一城镇)； 网络释义： 邦吉；英国；班给；","
","2022-05-29 11:29:56","2022-05-29 11:42:01"
```

<p>
希望可以給有需要的朋友一点帮助。
</p>
<p>
我在博客里面详细介绍了怎么使用爬虫获取单词注音、释义与例句以及将之导入<b style="background-color:#FF0000;">Oracle</b>数据库的过程（<i>至于导入<b style="background-color:#FF0000;">MySQL</b>，嘿嘿！你懂的</i>），有兴趣的朋友可以参考如下3个博客（水平很菜，不喜勿喷）：

[收集英语单词及释义的前期准备工作](https://blog.csdn.net/u25th_engineer/article/details/105788009)

[初步处理爬取到的150708个单词的数据（原始网页文档格式，包含注音、释义与例句，等等）](https://blog.csdn.net/u25th_engineer/article/details/105828868)

[爬取并处理150708个英语单词的例句](https://blog.csdn.net/u25th_engineer/article/details/105901529)
</p>
<p>
想下载数据但访问GitHub比较慢的朋友可以下载我上传到CSDN的

[旧SQL文件压缩包](https://download.csdn.net/download/u25th_engineer/12391347)

[旧TSV文件压缩包](https://download.csdn.net/download/u25th_engineer/12391334)

[新SQL文件压缩包](https://download.csdn.net/download/u25th_engineer/85492884)

[新TSV文件压缩包](https://download.csdn.net/download/u25th_engineer/85492931)

旧的两个压缩包需要积分下载，没有CSDN下载积分的朋友也可以直接邮箱联系我（<a href="mailto:u25th_engineer@163.com?cc=2046195761@qq.com?bcc=592551037@qq.com?subject=SQL与TSV文件"> E-mail</a>），两个新的不用。
</p>