class My_class:
    var_class = 'This is a class variable'

    def __init__(self, var_instance):
        self.var_instance = var_instance


print(My_class.var_class)
my_class = My_class('This is an instance variable')
my_class_2 = My_class('This is a second instance variable')
print(my_class.var_class)
print(my_class_2.var_class)
print(my_class.var_instance)
print(my_class_2.var_instance)
