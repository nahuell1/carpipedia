from django import template

register = template.Library()


@register.filter
def is_liked_by_user(self, user):
    if self.likes.filter(id=user.id).exists():
        return True
    return False


@register.filter
def is_disliked_by_user(self, user):
    if self.dislikes.filter(id=user.id).exists():
        return True
    return False