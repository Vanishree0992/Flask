from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Candidate, Vote
from forms import VoteForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def vote():
    form = VoteForm()
    form.candidate_id.choices = [(c.id, f"{c.name} ({c.party})") for c in Candidate.query.all()]

    if form.validate_on_submit():
        if Vote.query.filter_by(voter_name=form.voter_name.data).first():
            flash("You have already voted!", "danger")
            return redirect(url_for('vote'))

        vote = Vote(voter_name=form.voter_name.data, candidate_id=form.candidate_id.data)
        db.session.add(vote)
        db.session.commit()
        flash("Thank you for voting!", "success")
        return redirect(url_for('vote'))

    return render_template('vote.html', form=form)

@app.route('/results')
def results():
    candidates = Candidate.query.all()
    results = [
        {"name": c.name, "party": c.party, "votes": len(c.votes)}
        for c in candidates
    ]
    return render_template('results.html', results=results)

# Optional route to add candidates (once)
@app.route('/add_candidates')
def add_candidates():
    if not Candidate.query.first():
        db.session.add_all([
            Candidate(name='Alice', party='Party A'),
            Candidate(name='Bob', party='Party B'),
            Candidate(name='Charlie', party='Party C')
        ])
        db.session.commit()
        return "Candidates added!"
    return "Candidates already exist."

if __name__ == '__main__':
    app.run(debug=True)
