from django.utils.text import slugify
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

INVALID_SLUG = ['create']

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a django project and it assumes instance has a model
    with a slug field and a title character field
    """

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists or slug in INVALID_SLUG:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                    )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
