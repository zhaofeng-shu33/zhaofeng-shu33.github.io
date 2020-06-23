# ggplot2 梯度作图
2019/01/31

`ggplot2`是R语言的绘图包

```R
library('ggplot2')
df <- data.frame(var=c("a","b","c","d","e","f","g","h","i","j"), nums=c(1:10))
# fill group should be within [0,1]
plot2 <- ggplot(df, aes(x=var, y=nums, fill= df$nums/10)) + geom_col() + scale_fill_gradient(low="red", high="green") + guides(fill = guide_colourbar(barwidth = 2, barheight = 10))
print(plot2)
```

效果图：
![](https://img2018.cnblogs.com/blog/1503439/201901/1503439-20190131235721815-1557311910.png)

参考：
[ggplot2](https://ggplot2.tidyverse.org/reference/guide_colourbar.html)