from flask import Flask, render_template

app = Flask(__name__)

news_data = {
    'sports': [
        'Team India wins the T20 World Cup!',
        'Olympics 2024 preparations underway.',
        'Ronaldo scores hat-trick in final match.'
    ],
    'technology': [
        'AI breakthroughs continue to amaze in 2025.',
        'SpaceX launches next-gen satellite.',
        'Quantum computing closer to mainstream.'
    ],
    'entertainment': [
        'New Marvel movie breaks box office records.',
        'Grammy Awards 2025 winners announced.',
        'Popular series returns for final season.'
    ]
}

@app.route('/news/<category>')
def show_news(category):
    news_list = news_data.get(category.lower(), [])
    return render_template('news.html', category=category.capitalize(), news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)
