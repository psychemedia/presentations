from IPython.display import HTML


#TO DO - the nested table does not display?
#Also, the nested execution seems to take a long time to run?
#Profile it to see where I'm going wrong!
def obj_display(v, nest=False, style=True):
    def nested(v):
        if nest:
            return obj_display(v, style=False)
        return v
        
    """Generate a simple visualisation of an object's structure. """
    html = '''<style type='text/css'>
    .vartable {{
    border-style: solid !important;
    border-width: 2px  !important;
}}

.vartable td {{
    border-style: solid !important;
    border-width: 2px  !important;
    text-align: left;
}}
</style>''' if style else ''
    
    if isinstance(v, int) or isinstance(v, str):
        html = html+'''<table class='vartable'><tr><td>ID:<br/>{v_id}</td>
                    <td>TYPE:<br/>{v_typ}</td></tr>
                    <tr><td colspan=2>VALUE:<br/>{v_val}</td></tr></table>'''
        html = html.format(v_id = id(v), v_typ = type(v).__name__, v_val=v)
        
    elif isinstance(v, list) or isinstance(v, dict):
        html = html+'''<table class='vartable'><tr><td>ID:<br/>{v_id}</td>
                    <td>TYPE:<br/>{v_typ}</td></tr>
                    <tr><td colspan=2>VALUE:<br/>{v_val}</td></tr></table>'''
        if isinstance(v, dict):
            v_items = ''.join(['<td>[{i}]: <strong>{v}</strong></td>'.format(i=i, v=nested(v_item) ) for v_item, i in enumerate(v)])
        else:
            v_items = ''.join(['<td>[{i}]: <strong>{v}</strong></td>'.format(i=i, v= nested(v_item) ) for i, v_item in enumerate(v)])
        v_val='<table><tr>{v_items}</tr></table>'.format(v_items = v_items)
        html = html.format(v_id = id(v), v_typ = type(v).__name__, v_val=v_val)
    
    display(HTML(html))

