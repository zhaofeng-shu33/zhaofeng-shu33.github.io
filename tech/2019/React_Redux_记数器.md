# React Redux 记数器
2019/02/05

```shell
npm init react-app counter
cd counter
npm install
```
将 `src/index.js`改为
```JavaScript
import React from 'react';
import { createStore } from 'redux'
import { connect, Provider } from 'react-redux'
import ReactDOM from 'react-dom';
// action creator
const CountAction= {
    increment : {type: 'INCREMENT'},
    decrement : {type: 'DECREMENT'}
}
// reducer
function counter(state = 0, action) {
  switch (action.type) {
    case CountAction.increment.type:
      return state + 1
    case CountAction.decrement.type:
      return state - 1
    default:
      return state
  }
}
let store = createStore(counter)

// presentational component
const counterCreator = ({ number, onClick }) => 
   (
      <div>
        <div>{number}</div>
          <button onClick={() =>{onClick('increment')}}>
            Increase
          </button>
          <button onClick={() =>{onClick('decrement')}}>
            Decrease
          </button>
      </div>
    )

const mapStateToProps = state => {
    return {
        number: state
    }
}
const mapDispatchToProps = (dispatch) => { 
    return {
        onClick: clickType => {
            dispatch(CountAction[clickType])
        }
    }
}
// container
const Counter = connect(mapStateToProps, mapDispatchToProps)(counterCreator)

ReactDOM.render(
    <Provider store={store}>
        <Counter />
    </Provider>,
    document.getElementById('root')
)
```
运行 `npm start` 效果如下：
![](https://img2018.cnblogs.com/blog/1503439/201902/1503439-20190205193212308-1130294714.png)