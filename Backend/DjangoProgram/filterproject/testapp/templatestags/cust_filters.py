from django import template
register=template.Library()
#register is variable name  templates is the module name .Library() is the class name with paranthesis

def first_five_upper(value):
    result= value[:5].upper()
    return result 

register.filter('ffu',first_five_upper)

def first_n_upper(value,n):
    result = value[:n].upper()
    return result

register.filter('fnu',first_n_upper)



