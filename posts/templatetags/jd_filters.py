from django import template

register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios):
    try:
        num_comentario = int(num_comentarios)

        if num_comentario == 0:
            return 'Nenhum comentário'
        elif num_comentario == 1:
            return f'{num_comentario} comentário'
        else:
            return f'{num_comentario} comentários'
    except:
        return f'{num_comentario} comentário(s)'
