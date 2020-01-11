from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class MMASearchForm(Form):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('Submit',
                         render_kw={'class': 'btn btn-success btn-block'})