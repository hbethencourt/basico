from django import template
from pprint import pprint

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):        
    if field:
        class_old = field.field.widget.attrs.get('class', None)
        class_new = class_old + ' ' + css if class_old else css        
        return field.as_widget(attrs={"class": class_new})
    else:
        print('{} - {}'.format(field,css))
        return field


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_attr (obj,atributo):
    return getattr(obj,atributo)

@register.filter
def get_tipo (x):
    return type(x)



class AssignNode(template.Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def render(self, context):
        context[self.name] = self.value.resolve(context, True)
        return ''

@register.tag(name="variable")
def do_assign(parser, token):
    """
    ejemplo: 
        {% variable var1 "HOLA" %}
        {{var1}}

    Assign an expression to a variable in the current context.
    
    Syntax::
        {% assign [name] [value] %}
    Example::
        {% assign list entry.get_related %}
        
    """
    #bits = token.contents.split()
    bits = token.split_contents()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes two arguments" % bits[0])
    value = parser.compile_filter(bits[2])
    return AssignNode(bits[1], value)

  