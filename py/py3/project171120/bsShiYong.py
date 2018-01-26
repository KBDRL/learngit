# -*- coding:utf-8 -*-"
from bs4 import  BeautifulSoup as bs
from urllib import parse
html_doc = """
<html xmlns="http://www.w3.org/1999/xhtml"><head>
    <title>玄幻小说_好看的全本玄幻小说_玄幻小说排行榜完本_全本书屋</title>
    <meta name="keywords" content="好看的全本玄幻小说,玄幻小说排行榜完本">
<meta name="description" content="全本书屋是书友最值得收藏的玄幻小说阅读网,网站收录了当前最好看的全本玄幻小说,免费提供高质量的玄幻小说排行榜完本作品,是广大玄幻小说爱好者必备的小说阅读网。
">
    <link type="text/css" rel="stylesheet" href="/css/g.css">
    <link type="text/css" rel="stylesheet" href="/css/category.css">
    <script src="https://hm.baidu.com/hm.js?8ed59c79ed5a528066e1f1dda31e672c"></script><script src="/js/h.js" type="text/javascript"></script>
</head>
<body>

<!-- head begin -->
<div id="topbar">
	<div id="logo"><a href="/"><img src="/images/logo.gif" width="286" height="70" alt="全本书屋"></a></div>
	<div id="top_right">
	<p class="aides">全本书屋：定位于网络小说爱好者，本站专业提供全本小说在线阅读与TXT全集小说下载。</p>
	<form id="form1" name="form1" method="get" target="_blank" action="/so/default.aspx">
  <select name="type" class="selType">
    <option value="1">小说名</option>
    <option value="2">作者名</option>
  </select>

  <input type="text" name="key" class="inputKey">

  <input name="Submit" class="searchBut" type="submit" id="Submit" value="搜索">

</form>
</div>
<div id="loginmenu">
<a href="/login.aspx" class="g_login">登录</a>
<a href="/register.aspx" class="g_reg">免费注册</a>
</div>
</div>

<div id="menu">
<a href="/">首页</a>
<a href="/category/2_1_1.aspx" class="focus">玄幻小说</a>
<a href="/category/3_1_1.aspx">修真小说</a>
<a href="/category/4_1_1.aspx">都市小说</a>
<a href="/category/5_1_1.aspx">言情小说</a>
<a href="/category/6_1_1.aspx">历史军事</a>
<a href="/category/7_1_1.aspx">网游竞技</a>
<a href="/category/8_1_1.aspx">科幻小说</a>
<a href="/category/9_1_1.aspx">恐怖小说</a>
<div id="membershujia"><a href="/member/reader/Bookshelf.aspx" class="focus">我的书架</a></div>
</div>
<script language="javascript" type="text/javascript">
var urls = document.getElementById("menu").getElementsByTagName("a");var url = window.location.toString();var blhas=true;for(i=0;i<urls.length;i++){if(urls[i].href == url){blhas=false;urls[i].className = "focus";break;}}if(blhas){urls[0].className = "focus";}
function drop_onclick(){document.getElementById("headSel").style.display = "";}function drop_mouseout(){document.getElementById("headSel").style.display = "none";}
function dosearchtype(st,obj){dosearchtypetxt(st,obj.innerHTML);}
function dosearchtypetxt(st,txt){document.getElementById("headSlected").innerHTML = txt;document.getElementById("searchType").value = st;document.getElementById("headSel").style.display = "none";}
</script>
<script src="/js/jquery.js" type="text/javascript"></script>
<script src="/js/l.js" type="text/javascript"></script>
<!-- head end -->
<div class="gtop"><script src="/js/et/gtop.js" type="text/javascript"></script></div>
<div class="bookstoretwo aclearfix">

<div class="twoleft">
    <div class="storelistbt">
        <div class="storelistbt2">1/31页 </div>
        <div style="font-weight:lighter" class="storelistbt1"><a style="margin-top:5px" href="/category/2_1_1.aspx" class="text active">图文方式</a> &nbsp;<a style="margin-top:5px;" href="/category/2_0_1.aspx" class="img_text">文字方式</a></div>
    </div>
    <div class="picul"><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4807.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4807/201710230705328007.jpg"></a>
<strong><a target="_blank" href="/book/4807.aspx" class="bookname">造化炼体决</a></strong> 
<p>作者：零下5度01</p>
<p>大千世界，无奇不有，光怪陆离，浩瀚无尽，种族林立，唯有强者可攀上巅峰，俯视天下。
乱世之中，群雄并起，百家争鸣，万族林立，强者之路，唯大毅力者可掌造化，与天争道。
修行之道：通后天、返先天，凝聚顶三花、聚五气归元，通天灵、御神魂，窃阴阳生死、夺天地造化，参天道、释命格，与天争命。
天生异变，双日横空，一个奇特的生命带着天地本源，自曜日中诞生……
破生死玄关、凝不败之躯，聚天地造化、铸不朽金身!</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4807.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4807.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4801.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4801/201710200708549911.jpg"></a>
<strong><a target="_blank" href="/book/4801.aspx" class="bookname">绝世剑姬</a></strong> 
<p>作者：斩鬼</p>
<p>再次睁眼之时，世界已然天翻地覆。
前一世的神秘镇宅古剑，在这一世终于寒光耀世，诸多光怪陆离之事纷至沓来。
通天路，白骨阶，登临万古，成绝世大帝！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4801.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4801.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4798.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4798/201710180945345952.jpg"></a>
<strong><a target="_blank" href="/book/4798.aspx" class="bookname">八荒剑神</a></strong> 
<p>作者：云泪天雨</p>
<p>星辰演化大道，日月繁衍规则。强者无敌于世，夺天地之造化。
  叶晨风身负神秘金色血液，融合噬神之脑，继承恒古不朽意志，一念万骨枯，一剑沧海平，一人一剑横扫天地八荒，气凌万古苍穹，成就八荒剑神！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4798.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4798.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4786.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4786/201710120908269123.jpeg"></a>
<strong><a target="_blank" href="/book/4786.aspx" class="bookname">超魔构筑师</a></strong> 
<p>作者：刻羽</p>
<p>老子，是魔法哲学的开创者？
孔子，是法术体系的奠基人？
韩非，是奥术规则的测绘师？
墨子，是炼金术和魔锻术的先驱？
“冰霜鞭挞者”大禹？“巨龙垂钓者”姜尚？“雷暴撕裂者”李元霸？
还有，蛰居自己灵魂中的“推衍者”，又是什么？</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4786.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4786.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4779.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4779/201710070827158085.jpg"></a>
<strong><a target="_blank" href="/book/4779.aspx" class="bookname">神荒龙帝</a></strong> 
<p>作者：妖月夜</p>
<p>一滴龙血，可压碎山河，一根龙骨，可撕裂苍穹，一双龙眸，可看穿古今！在这里，有女帝君临天下！有古兽只手遮天！ 有大魔祸乱天地，也有人族先贤镇压八荒！少年凌飞身怀龙骨，崛起于微末，闯神荒，探帝墓，开启了一条与亿万神魔争锋的无敌 之路！ 整个天地……因他而变 ！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4779.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4779.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4778.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4778/201710070705424687.jpg"></a>
<strong><a target="_blank" href="/book/4778.aspx" class="bookname">绝世皇帝</a></strong> 
<p>作者：盛夏微暗</p>
<p>林谦，地球的国战游戏达人，标准的人民币战士！发生意外后，重生到异界。
  然而，在这异界之中，除了修炼天赋好点，却没有特殊的一技之长。
  炼丹他炸炉，炼器成废铁，更别提阵法这些其他生活技能，一窍不通。
  不过林谦却偶然发现，他前世在游戏里称霸服务器的庞大帝国，不仅跟着穿越。
  原本只是一堆数据的无敌武将、军团长，以亿为单位的帝国大军，拥有了生命，活了过来，对他誓死效忠！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4778.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4778.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4769.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4769/201710010605574928.jpg"></a>
<strong><a target="_blank" href="/book/4769.aspx" class="bookname">真武神王</a></strong> 
<p>作者：邵小白</p>
<p>大千宇宙，位面无数，强者如云，少年天才林阳被族中赐婚，未婚妻却是一名人尽可夫的婊子，就当林阳备受屈辱之时，一座无名小塔却悄然间来到他的身边，自此林阳握神塔，踏诸天！林阳：万千世界，终有一天会被我踩在脚下！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4769.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4769.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4766.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4766/201709290741032172.jpg"></a>
<strong><a target="_blank" href="/book/4766.aspx" class="bookname">刀剑神皇</a></strong> 
<p>作者：乱世狂刀</p>
<p>一口冰剑，一柄炎刀，一个屹立绝巅的不朽神皇传说！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4766.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4766.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4763.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4763/201709280720306645.jpg"></a>
<strong><a target="_blank" href="/book/4763.aspx" class="bookname">魔域</a></strong> 
<p>作者：乱世狂刀</p>
<p>一朝英雄拔剑起，又是苍生十年劫。但那世间最风流的繁华，却又怎么抵得上你眉间一点朱砂。</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4763.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4763.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4759.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4759/201709260543494239.jpg"></a>
<strong><a target="_blank" href="/book/4759.aspx" class="bookname">星魂战神</a></strong> 
<p>作者：灵隐狐</p>
<p>寻常武者以大荒猛兽为星魂；天才以狻猊、穷奇等神兽为星魂；绝顶天骄以麒麟、青龙、鲲鹏为星魂，修炼到巅峰层次，可以拥有神兽的全部力量、全部神通！
穆炎的星魂，是一块顽石……
石破惊天时，万古神猿现！
修变化神通、炼火眼金睛、持巨棒神兵；踩真龙、斩麒麟、灭青鸾；搅乱万界、踏破天庭……
扭转天地，成就最强星魂！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4759.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4759.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4757.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4757/201709250731075011.jpg"></a>
<strong><a target="_blank" href="/book/4757.aspx" class="bookname">灭世魔帝</a></strong> 
<p>作者：沉默的糕点</p>
<p>穿越异世成冒牌城主，拥有五百里领地，一个国色天香的姐姐。
还要振兴一个风雨飘摇的家族，作为一个大三男生，兰陵感觉到压力山大。
身怀妖星的他，竟可以直接吞噬别人修为占为己有，而他穿越异世的唯一使命竟是：毁灭世界！
从天水城主，到女王丈夫，灭世魔帝，最终他成为了举世之王！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4757.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4757.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4752.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4752/201709220714127776.jpg"></a>
<strong><a target="_blank" href="/book/4752.aspx" class="bookname">执掌乾坤</a></strong> 
<p>作者：乌山云雨</p>
<p>刚刚收到录取通知书的林楠，还没来得及实现祸害大学校花的美梦，便被一根神秘的金针带到一个以武为尊的世界……
挥手日月沉，剑出天地动；谈笑间，败尽天下高手——执掌乾坤！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4752.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4752.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4746.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4746/201709190633563244.jpg"></a>
<strong><a target="_blank" href="/book/4746.aspx" class="bookname">绝世邪君</a></strong> 
<p>作者：晓浅</p>
<p>魔域纵横，孤独为王！
落魄世家弟子秦石，受尽凌辱，饱尝人间冷暖！
为洗刷屈辱，他不惜堕入魔道，弃身成魔，屠尽仙神！
诸魔乱天，群雄并起！
且看，在这个仙魔争锋的世界里，一个心性本善，为寻正义而求魔道，终成一代天道魔皇。
“虽然我不喜欢杀戮，但我也不讨厌杀戮。”秦石语。
“欲看魔的世界，我是如何争锋，尽在绝世邪君。”</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4746.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4746.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4722.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4722/201709070703319399.jpg"></a>
<strong><a target="_blank" href="/book/4722.aspx" class="bookname">吞噬神域</a></strong> 
<p>作者：南归</p>
<p>李天泽穿越异世，觉醒了吞噬神脉，绝世战技、逆天血脉、上古神器、功法传承……天地万物无所不吞！“不好意思，诸位所珍视的一切，我都不客气的笑纳了！”</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4722.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4722.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4719.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4719/201709050757341543.jpg"></a>
<strong><a target="_blank" href="/book/4719.aspx" class="bookname">苍穹之主</a></strong> 
<p>作者：风圣大鹏</p>
<p>大千世界，诸天星斗，尽在吾手。妖魔鬼怪，阴阳万法，一念生灭。“天道不公，祸乱横行。人间王朝，弱肉强食。我不求成仙成神，只求有朝一日掌控苍穹，做一个公平。”矿工林昊。</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4719.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4719.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4716.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4716/201709040619579193.jpg"></a>
<strong><a target="_blank" href="/book/4716.aspx" class="bookname">穿越当皇帝</a></strong> 
<p>作者：天皇圣祖</p>
<p>携最强龙帝系统，穿越做皇帝。
后宫佳丽三千，天下权柄在握。
笑看诸天万界，吊打各种不服。
睡最美的女人，杀最强的男人。
开创暴爽皇帝流，敬请赏阅。</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4716.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4716.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4713.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4713/201709020751206503.jpeg"></a>
<strong><a target="_blank" href="/book/4713.aspx" class="bookname">剑灵</a></strong> 
<p>作者：坏宝</p>
<p>天域之中，百族争霸，灵族，魔族，魂族等顶尖种族称霸其中，而万年前，人族天帝陨落，人族从此式微……
万年之后，天剑大陆上，一颗来历神秘的剑型晶体，一个看似出身小家族，却被人为堵塞经脉的少年，两者奇妙相遇，少年从此展现过人天赋。先修剑意，再悟剑道，成就剑魂，直至修成无上剑灵。
从此，人族天域再称雄！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4713.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4713.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4711.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4711/201709010753467441.jpg"></a>
<strong><a target="_blank" href="/book/4711.aspx" class="bookname">道神</a></strong> 
<p>作者：凌乱的小道</p>
<p>剑道天才，转世重生，覆灭王朝，横扫四方！
修帝经，肉身无双，徒手抗神兵，一剑光寒千万界！
为兄弟，两肋插刀，火海刀山，肝胆相照！
为红颜，征战天下，血染八荒，至死不渝！
血雨腥风，扬眉淡笑，指剑问群雄，谁敢与我一战？
雄鹰下山，猛虎冲天，谁主沉浮，唯我道神！你命由我不由天，灭你只在挥手间！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4711.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4711.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4695.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4695/201708240729198320.jpg"></a>
<strong><a target="_blank" href="/book/4695.aspx" class="bookname">皇道</a></strong> 
<p>作者：雾外江山</p>
<p>皇道天帝，霸绝乾坤！
灭诸神，斩至尊！
修最强功法，得最靓女神！
神国废墟掠重宝，绝色天香伴君行！
穿梭时空，英雄谁属？
唯我皇道至尊！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4695.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4695.aspx">TXT下载</a></p>
</li>
</ul>
</div><div class="storelistbt5">
<ul><li class="storelistbt5a">
<a target="_blank" href="/book/4691.aspx">
<img src="http://pic.quanshuwu.com/files/book/2/4691/201708220644515616.jpg"></a>
<strong><a target="_blank" href="/book/4691.aspx" class="bookname">超级掠夺系统</a></strong> 
<p>作者：时也</p>
<p>穿越获得超级掠夺系统，顺昌的牛逼人生就此开启！掠夺系统，掠天掠地，掠夺万物！天才是什么？是用来踩的！天赋修为是什么？是用来抢的！宝贝丹药，极品美女，全都统统到我碗里来！</p>
</li>
<li style="margin-top:10px" class="storelistbt5b">
<p><a target="_blank" href="/book/4691.aspx"> 阅读本书</a></p>
<p><a href="/ebook/4691.aspx">TXT下载</a></p>
</li>
</ul>
</div><div id="storelistbottom" class="yema"><b class="pageBarCurrentStyle">1</b> <a href="/category/2_1_2.aspx">2</a> <a href="/category/2_1_3.aspx">3</a> <a href="/category/2_1_4.aspx">4</a> <a href="/category/2_1_5.aspx">5</a> <a href="/category/2_1_6.aspx">6</a> <a href="/category/2_1_7.aspx">7</a> <a href="/category/2_1_8.aspx">8</a> <a href="/category/2_1_9.aspx">9</a> <a href="/category/2_1_10.aspx">10</a> <a href="/category/2_1_2.aspx">下页</a> <a href="/category/2_1_31.aspx">末页</a> 	&nbsp;&nbsp;共 620条 &nbsp;&nbsp; 1页/31页</div></div>
</div>

<script src="/js/ping.js" type="text/javascript"></script>
</div>
	
    

<div class="bb"></div>
<div id="footer">
<p>本网站收录的全本小说(包括<a href="/category/4_1_1.aspx">全本都市小说</a>、<a href="/category/2_1_1.aspx">全本玄幻小说</a>、<a href="/category/7_1_1.aspx">全本网游小说</a>等作品、评论均属其个人行为，不代表本站立场，请读者<a href="/">阅读全本小说</a>时加以甄别<br>

本站所有的全本小说均由网友收集自互联网络，只为让网友更加方便地阅读到好看的全本小说，如有侵权请与管理员联系 <br>

Copyright© 2017 www.quanshuwu.com All Rights Reserved 版权所有
</p>

<div>
<script type="text/javascript" src="/js/et/tj.js"></script>
</div>

</div>
</body></html>
"""
#baseurl='http://www.quanshuwu.com/category/2_1_1.aspx' 这是要爬取的网站
soup=bs(html_doc,"lxml")
list=soup.find_all('strong')
#print(list)
needlist=[]
for a in list:
    title=a.get_text()
    print(title)
    hrefl=soup.find_all(class_='bookname')
#print(hrefl)
    for b in hrefl:
       href_v=b["href"]
       baseurl='http://www.quanshuwu.com'
       href_val=[baseurl+href_v]
       print(href_val)
       if[title,href_val] not in needlist:
            needlist.append([title,href_val])
            print(needlist)
with open('title,txt','w',encoding='utf8') as f:
    for href in href_val:
      f.write(title)


