## len()
- len()是去調用__len__()方法，但是卻比直接使用__len__()更快。
- 因為當物件有定義__getattribute__()方法時，就會讓查詢__len__()變得效率低。

## reversed()
- 會呼叫__reversed__()。如果不存在此方法，就會去尋找__len__與__getitem__。
