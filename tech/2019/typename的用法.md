# typename的用法
2019/02/13

```C++
template <class T>
void foo() {
    typename T::iterator * iter;
}
class ContainsAType{
    public:	
	class iterator {
	};
};
int main(){
	foo<ContainsAType>();
}
```
在有依赖的类型中，`typename` 关键字表明定义的是一个类型，如不使用编辑器会报错。