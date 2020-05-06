
'''
Generate HTML
'''


def tag(element, data='', **kw):
    ''' Construct html elements
    '''
    attrs = ' '.join(('{}="{}"'.format(k, v) for k, v in kw.items()))
    if attrs:
        format_str = '<{element} {attrs}>{data}</{element}>'
        return format_str.format(element=element, attrs=attrs, data=data)

    format_str = '<{element}>{data}</{element}>'
    return format_str.format(element=element, data=data)
