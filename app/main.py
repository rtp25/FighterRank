from app.DB_Connection import DB_Connection
from app.Ranker import Ranker
from flask import Flask, url_for
from flask import render_template, redirect, request, flash
from app.forms import MMASearchForm


#from flask-table import Table, Col


# need to resolve the config vars for FLASK prior to each run
# remember to cd to the sub folder to run the main with flask run
# maybe think about over all design MVC?
# think about testing
# put on git maybe?
# expand weight classes?
# decorate front end a bit
# put on AWS along with the DATABASE?
# Also, could display that a " fighter does not exist" on the front end instead of on the console



app = Flask(__name__)

#@app.route('/')
#def Index():
    #return "You are gonna stick with this shit for a bit so make the most of it"


class MyObj(object):
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

@app.route('/home')
def home_too():
    return render_template('home.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/wc', methods=['GET', 'POST'])
def weightclasses():
    form = MMASearchForm(request.form)
    # if request.method == 'POST'
    search_str = form.data['search']
    if search_str == 'fw':
        # return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/fw')
    elif search_str == 'lw':
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')

    return render_template('weightclasses.html', form=form)
    #return render_template('singlefighter.html', form=form)

@app.route('/fw', methods=['GET', 'POST'])
def featherweight():
    form = MMASearchForm(request.form)

    search_str = form.data['search']
    if search_str == 'fw':
        return redirect('/fw')
    elif search_str == 'lw':
        # return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')

    my_objs = [
        MyObj(result4[0][0], result4[0][1]),
        MyObj(result4[1][0], result4[1][1]),
        MyObj(result4[2][0], result4[2][1]),
        MyObj(result4[3][0], result4[3][1]),
        MyObj(result4[4][0], result4[4][1]),
        MyObj(result4[5][0], result4[5][1]),
        MyObj(result4[6][0], result4[6][1]),
        MyObj(result4[7][0], result4[7][1]),
        MyObj(result4[8][0], result4[8][1]),
        MyObj(result4[9][0], result4[9][1])


    ]
    return render_template('weightclasses.html', my_objs=my_objs, form=form)


@app.route('/lw', methods=['GET', 'POST'])
def lightweight():
    form = MMASearchForm(request.form)

    search_str = form.data['search']
    if search_str == 'fw':
        # return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/fw')
    elif search_str == 'lw':
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')

    my_objs = [
        MyObj(result1[0][0], result1[0][1]),
        MyObj(result1[1][0], result1[1][1]),
        MyObj(result1[2][0], result1[2][1]),
        MyObj(result1[3][0], result1[3][1]),
        MyObj(result1[4][0], result1[4][1]),
        MyObj(result1[5][0], result1[5][1]),
        MyObj(result1[6][0], result1[6][1]),
        MyObj(result1[7][0], result1[7][1]),
        MyObj(result1[8][0], result1[8][1]),
        MyObj(result1[9][0], result1[9][1])

    ]
    return render_template('weightclasses.html', my_objs=my_objs, form=form)


@app.route('/ww', methods=['GET', 'POST'])
def welter_weight():
    form = MMASearchForm(request.form)

    search_str = form.data['search']
    if search_str == 'fw':
        # return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/fw')
    elif search_str == 'lw':
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')
    my_objs = [
        MyObj(result2[0][0], result2[0][1]),
        MyObj(result2[1][0], result2[1][1]),
        MyObj(result2[2][0], result2[2][1]),
        MyObj(result2[3][0], result2[3][1]),
        MyObj(result2[4][0], result2[4][1]),
        MyObj(result2[5][0], result2[5][1]),
        MyObj(result2[6][0], result2[6][1]),
        MyObj(result2[7][0], result2[7][1]),
        MyObj(result2[8][0], result2[8][1]),
        MyObj(result2[9][0], result2[9][1])

    ]
    return render_template('weightclasses.html', my_objs=my_objs, form=form)


@app.route('/mw', methods=['GET', 'POST'])
def middle_weight():
    form = MMASearchForm(request.form)

    search_str = form.data['search']
    if search_str == 'fw':
        # return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/fw')
    elif search_str == 'lw':
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')

    my_objs = [
        MyObj(result3[0][0], result3[0][1]),
        MyObj(result3[1][0], result3[1][1]),
        MyObj(result3[2][0], result3[2][1]),
        MyObj(result3[3][0], result3[3][1]),
        MyObj(result3[4][0], result3[4][1]),
        MyObj(result3[5][0], result3[5][1]),
        MyObj(result3[6][0], result3[6][1]),
        MyObj(result3[7][0], result3[7][1]),
        MyObj(result3[8][0], result3[8][1]),
        MyObj(result3[9][0], result3[9][1])

    ]
    return render_template('weightclasses.html', my_objs=my_objs, form=form)


# searches DB for a table based on search form parameter of wc
@app.route('/search', methods=['GET', 'POST'])
def search_wc():
    form = MMASearchForm(request.form)
    #if request.method == 'POST'
    search_str = form.data['search']
    if search_str == 'fw':
        #return redirect((url_for('search_results', query=form.search.data)))  # or what you want
        return redirect('/fw')
    elif search_str == 'lw':
        return redirect('/lw')
    elif search_str == 'ww':
        return redirect('/ww')
    elif search_str == 'mw':
        return redirect('/mw')

    return render_template('weightclasses.html', form=form)
    #return redirect('/')

# searches a fighter
@app.route('/fighter', methods=['GET', 'POST'])
def search_fighter():
    form = MMASearchForm(request.form)


    search_str = form.data['search']
    ranker5 = Ranker()
    result5 = ranker5.add_fighter_by_name(search_str)
    if result5 is not None:
        my_objs = [
        MyObj(result5[0][0], result5[0][1])

        ]

    else:
        my_objs = [
            MyObj("", "")

        ]

    return render_template('singlefighter.html',  my_objs=my_objs, form=form)


conn = DB_Connection()
ranker = Ranker()
ranker2 = Ranker()
ranker3 = Ranker()
ranker4 = Ranker()
ranker5 = Ranker()


result1 = ranker.rankFighters('lw')
result2 = ranker2.rankFighters('ww')
result3 = ranker3.rankFighters('mw')
result4 = ranker4.rankFighters('fw')

if __name__ == "__main__":
    app.run(debug=True)