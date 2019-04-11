# 4.11
今天想扩展lemon库的preflow alg 算法支持用 flowMap 和 elevator 初始化，发现它的 second phase 过后 elevator
不是原来 generic algorithm 里面定义的，没法直接套用公式，尝试用 first phase 过后产生 maximal preflow 的 elevator 
初始化后面计算要用的elevator,目前还不清楚是否合法。如果行不通的话可能要放弃用lemon 库的preflow 了。
