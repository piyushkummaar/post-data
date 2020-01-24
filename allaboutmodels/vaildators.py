from django.core.exceptions import ValidationError

'''
Custom in vaildator on the models
'''

def email_vaildator(value):
    if '@' in value:
        return value
    else:
        raise ValidationError('Not a vaild email.')
    
'''
clenner way
'''
def domain_vaildator(value):
    if '.com' not in value:
        raise ValidationError('Not a vaild email.')
    return value
    
