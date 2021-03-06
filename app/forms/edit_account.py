from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional
from app.util.fields import FSUIDField

class EditAccount(FlaskForm):
    """EditAccount

    This form lets change their info they submitted when they
    registered, such as add an FSUID.

    """

    first_name = StringField('First Name', validators=[
        DataRequired()
    ])

    last_name = StringField('Last Name', validators=[
        DataRequired()
    ])

    fsuid = FSUIDField('FSUID', validators=[
        Optional(strip_whitespace=True)
    ])

    submit = SubmitField('Update')
