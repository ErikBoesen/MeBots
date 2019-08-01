from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User


class BotForm(FlaskForm):
    name = StringField('Bot name', validators=[DataRequired()])
    slug = StringField('Shortname', validators=[DataRequired()])
    name_customizable = BooleanField('Allow customizing name')
    avatar_url = StringField('Avatar URL')
    avatar_url_customizable = BooleanField('Allow customizing avatar')
    callback_url = StringField('Callback URL', validators=[DataRequired()])
    description = TextAreaField('Description')

    submit = SubmitField('Submit')


class InstanceForm(FlaskForm):
    group_id = SelectField('Group')
    name = StringField('Bot name')
    avatar_url = StringField('Bot avatar')

    submit = SubmitField('Add bot')
