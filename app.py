from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)


def get_repos_list():
    response = requests.get('https://api.github.com/orgs/allegro/repos')

    j = json.loads(response.content)

    repos = []

    for repo in j:
        repos.append({'name': repo['name'], 'stars': repo['stargazers_count']})

    return repos


def get_sum_stars():
    response = requests.get('https://api.github.com/orgs/allegro/repos')

    j = json.loads(response.content)
    stars = 0
    for repo in j:
        stars += repo['stargazers_count']
    return stars


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/repos/list')
def list_repos():
    return jsonify(get_repos_list())


@app.route('/repos/stars/sum')
def stars_sum():
    return get_sum_stars().__str__()


if __name__ == '__main__':
    app.run()
