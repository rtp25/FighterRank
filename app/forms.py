from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class MMASearchForm(Form):
    search = StringField('Name', [DataRequired()])
    submit = SubmitField('Submit',
                         render_kw={'class': 'btn btn-success btn-block'})


class MMACreateFighterForm(Form):
    weightClass = StringField('Weightclass', [DataRequired()])
    name = StringField('Name', [DataRequired()])
    wins = StringField('Wins', [DataRequired()])
    losses = StringField('Losses', [DataRequired()])
    koWins = StringField('KOs', [DataRequired()])
    subWins = StringField('Subs', [DataRequired()])
    decWins = StringField('Decs', [DataRequired()])
    strAccur = StringField('StrAccur', [DataRequired()])
    grpAccur = StringField('GrpAccur', [DataRequired()])
    submit = SubmitField('Submit',
                         render_kw={'class': 'btn btn-success btn-block'})
