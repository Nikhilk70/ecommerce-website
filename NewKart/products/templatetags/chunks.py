from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(List_data,chunk_size):
    if not List_data:
        return []
    chunk=[]
    i=0
    for i, item in enumerate(List_data):
        chunk.append(item)
        if (i + 1) % chunk_size == 0:
            yield chunk
            chunk=[]
    if chunk:
        yield chunk