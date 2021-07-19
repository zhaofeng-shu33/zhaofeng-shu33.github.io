# Winform 中使用 WPF Control（带资源）
2019/07/17

.Net 中 winform 中使用 WPF 控件已有较多的讨论，但若控件本身带有引用的资源，则情况变得复杂，笔者亲测可以在
全局的 Application 对象中动态增加资源的方法解决。

1. 由于WinForm 默认不含 Application 全局变量，需手动引入。
首先在exe 项目中增加 PresentationForm 的引用
```C#
using System.Windows
if (null == System.Windows.Application.Current)
{
    new System.Windows.Application();
}
 ```

 2. 在自定义的 UserControl 子类的构造函数 `InitializeComponent` 执行之前动态增加所需要的资源
 ```C#
 using System.Collections.ObjectModel;
 System.Uri resourceLocater = new System.Uri("/ACMonitorSystemUserControl;component/myresource.xaml", System.UriKind.Relative);
 ResourceDictionary rd = (ResourceDictionary)Application.LoadComponent(resourceLocater);
 Application.Current.Resources.MergedDictionaries.Add(rd);
 ```
这样做不需要在 xaml 文件里引用资源（xaml 引用方式不能在其他项目中使用该控件。）