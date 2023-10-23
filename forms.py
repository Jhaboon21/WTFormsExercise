from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField("Type of Species", 
                          choices=[("cat", "Cat"), ("dog", "Dog"), ("bird", "Bird"), ("hamster", "Hamster")])
    
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Enter Age", validators=[Optional()])
    
    notes = StringField("Additional Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing existing pets."""

    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments", validators=[Optional()],
    )

    available = BooleanField("Available?")