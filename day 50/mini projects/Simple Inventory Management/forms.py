from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ItemForm(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Add Item")

class UpdateForm(FlaskForm):
    quantity = IntegerField("New Quantity", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Update")
