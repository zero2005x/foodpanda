from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def mul(v1, v2, v3):
    return v1 * v2 * v3

@register.simple_tag
def my_input(v1, v2):
    temp_html = """<div class="input-group mb-3"> 
        <span class="iput-gruop-text" id="%s">@</span>
            <input type="text" class="form-control" placeholder="%s" aria-label="UserName">
</div>"""%(v1,v2)
    return mark_safe(temp_html)