1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.

Types   | integer | string | boolean
--------| ------- | ------ | -------
integer |  1      | -      | True
integer |  0      | -      | False
string  |  -      | "a"    | True
string  |  -      | ""     | False

2. Разобраться с различиями мжеду input() и raw_input(). Также в контексте разных версий python: 2 и 3.
    python2.x                    python3.x     
    raw_input()   --------------> input()               
    ```python
	    >>> x = input()
 	    1
   	    >>> y = input()
	    x + 6
   	    >>> y
	    7
    ```
    input()  -------------------> eval(input())
    ```python3
            >>> x = input()
            1
            >>> y = input()
            x + 6
            >>> y
            "x + 6"
    ```

3. Найти и прочитать PEP про изменение print между python2 и python3.
Перевод print в функцию позволяет разработчикам переопределять ее, а так же передавать как аргумент в другую функцию

