# 浏览器DOM事件触发
2019/02/04

除用户人为交互触发事件外，用js脚本触发事件的一般流程为
1. 创建事件 `var e = Event('event_name', {key: value, ...})`
2. 分发事件到 `event.target`
3. 触发事件处理函数 `EventHandler`

# 示例
```HTML
<select >
    <option value="all" selected>all</option>
    <option value="active">active</option>
    <option value="completed">completed</option>
</select>
<script>
    let select = document.getElementsByTagName('select')[0];
    select.onchange = handleChange;
    function handleChange(e){
        console.log('changed');
    }
</script>
```
如上脚本中的 change 事件脚本触发的方式如下：
```JavaScript
var e = Event('change', {bubbles: true});
select.options[1].dispatchEvent(e);
```