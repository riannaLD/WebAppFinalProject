
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ElfForm(FlaskForm):
    description = StringField("Elf Information", validators=[DataRequired()])
    submit = SubmitField("Add Elf")