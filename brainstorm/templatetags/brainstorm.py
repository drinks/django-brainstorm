from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def user_can_post(context):
    user = context['request'].user
    subsite = context['subsite']
    return subsite.user_can_post(user)
