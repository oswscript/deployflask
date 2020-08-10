from wtforms import Form, Field
from wtforms import StringField, PasswordField
#import webapp.helpers.custom_validations
from wtforms import validators

""" CUSTOM VALIDATIONS """
from wtforms import validators

#character limit
def valid_limit(form,field):
    
    if len(field.data) > 0 and len(field.data) < 3:

        raise validators.ValidationError("The "+field.name.title()+" must be at least 3 characters")

    elif len(field.data) > 10:

        raise validators.ValidationError("The "+field.name.title()+" must have a maximum of 10 characters")

def valid_no_empty(form,field):

    if(len(field.data) == 0):

        raise validators.ValidationError(field.name.title()+" field is required")
    
class UpdateUserForm(Form):

    #input name
    fullname = StringField('Fullname',
    [
        valid_no_empty,
    ],
    render_kw={"placeholder": "Fullname"}
    )

    #input username
    username = StringField('Username',
    [
        valid_limit,
        valid_no_empty
    ],
    
    render_kw={"placeholder": "Username"}
    )

    #input email
    email = StringField('Email',
    [
        valid_no_empty
    ],
    
    render_kw={"placeholder": "Email"}
    )
