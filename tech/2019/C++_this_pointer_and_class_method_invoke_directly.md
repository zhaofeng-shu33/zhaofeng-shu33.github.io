# C++ this pointer and class method invoke directly
2019/08/23

Using C++ 11 `bind`
```C++
#include <iostream>
#include <functional>
class Simple
{
private:
    int m_id;
 
public:
    Simple(int id)
    {
        setID(id);
    }
 
    void setID(int id) { m_id = id; }
    int getID() { return m_id; }
};
int main(){
  Simple simple(1);
  std::function<void()> f1 = std::bind(&Simple::setID, &simple, 2);
  f1();
  std::cout << simple.getID() << std::endl;
}
```