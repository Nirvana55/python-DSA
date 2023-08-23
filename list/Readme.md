List:

List are a linear data structure type in python. They are a versatile data structure that can be used for a variety of tasks. They are often used to store collections of data, such as lists of numbers, lists of strings, or lists of objects. In the memory allocation it has a pointer to track its element. When a element is appended pre allocation is done in order to increase its size and improve its performance.

it is denoted like: variable_name -> [1,"2",3,4] or list(1,2,3,4)

It has some pros and cons:

-> pros:

1. It is easily modified and accept every data types.
2. It also accepts nested data.

-> cons:

1. It is slow during arithmetic operations on their elements.
2. They use more disk space because of preallocation.
   (The actual amount of memory that a list consumes depends on the number and size of the elements in the list).

# things to keep in the mind when modify list:

-> never modify the list when iterating
-> why ? cause when you do that the loop will just continue and the iterator wont know abt it and keep on do the task that is assigned
-> which can cause a issue.
-> link for full description: https://stackoverflow.com/questions/10812272/modifying-a-list-while-iterating-over-it-why-not
