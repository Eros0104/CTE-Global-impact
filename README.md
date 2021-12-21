<h1 align="center">:globe_with_meridians: Global Impact - Computional Thinking for Engineering</h1>

<p align="center">A little project, developed for logic classes, that renders a report for the construction of a railroad. :station:</p>

## :computer: Prerequisites

Before starting, you will have to install the following tools:

- [Git](https://git-scm.com)
- [Python](https://www.python.org/)
- Besides it's nice to have an editor to work with the code like [VSCode](https://code.visualstudio.com/)

## :game_die: Getting started

```bash
# cloning the project

git clone https://github.com/Eros0104/CTE-Global-impact

# access the project directory

cd CTE-Global-impact

# run project

python main.py

# the rendered HTML report will automatically be opened by the browser

```

## :nail_care: Customization

In the following directory, you will find this file:

```
data/routes.json
```

You can add or remove objects in the JSON array that is in the file, following this model:

```json
{
    "cityA": "Rio de Janeiro",
    "cityB": "Sao Paulo",
    "distance": 432,
    "anualPassengers": 7308000
}
```

cityA - City where the railroad starts/ends

cityB - City where the railroad starts/ends

distance - Railroad distance in kilometers

anualPassengers - Anual users of the railroad
