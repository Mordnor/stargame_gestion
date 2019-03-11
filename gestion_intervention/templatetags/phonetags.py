from django import template

register = template.Library()

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

@register.filter(name='formatphone')
def formatphone(phonenumber):
    phonenumber = phonenumber.replace(" ","")
    phonenumber_split = list(chunks(phonenumber, 2))
    return " ".join(phonenumber_split)
