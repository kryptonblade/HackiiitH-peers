# from flask import Flask, render_template
# import requests
# import random

# app = Flask(__name__)

# def get_codeforces_problemset():
#     base_url = "https://codeforces.com/api/problemset.problems"

#     try:
#         response = requests.get(base_url)
#         response.raise_for_status()  # Raise an error for bad responses

#         data = response.json()
#         problems = data.get("result", {}).get("problems", [])

#         return problems

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None

# def get_random_problems(problemset, count=5, difficulty="easy"):
#     difficulty_ranges = {
#         "easy": (800, 1500),
#         "medium": (1200, 2000),
#         "hard": (1900, 2900)
#     }

#     rating_range = difficulty_ranges.get(difficulty, (0, 0))
    
#     filtered_problems = [problem for problem in problemset if rating_range[0] <= problem.get('rating', 0) <= rating_range[1]]
#     selected_problems = random.sample(filtered_problems, min(count, len(filtered_problems)))
#     return selected_problems

# @app.route('/')
# def index():
#     # Fetch the entire Codeforces problemset
#     problemset = get_codeforces_problemset()

#     if problemset:
#         # Get random problems based on user input
#         user_difficulty_input = input("Enter difficulty (easy, medium, hard): ").lower()
#         random_problems = get_random_problems(problemset, count=5, difficulty=user_difficulty_input)

#         # Render the HTML template with the problems
#         return render_template('index.html', problems=random_problems)
#     else:
#         return "Failed to fetch the Codeforces problemset."

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template
# import requests
# import random

# app = Flask(__name__)

# def get_codeforces_problemset():
#     base_url = "https://codeforces.com/api/problemset.problems"

#     try:
#         response = requests.get(base_url)
#         response.raise_for_status()  # Raise an error for bad responses

#         data = response.json()
#         problems = data.get("result", {}).get("problems", [])

#         return problems

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None

# def get_random_problems(problemset, count=5, difficulty="easy"):
#     difficulty_ranges = {
#         "easy": (800, 1500),
#         "medium": (1200, 2000),
#         "hard": (1900, 2900)
#     }

#     rating_range = difficulty_ranges.get(difficulty, (0, 0))
    
#     filtered_problems = [problem for problem in problemset if rating_range[0] <= problem.get('rating', 0) <= rating_range[1]]
#     selected_problems = random.sample(filtered_problems, min(count, len(filtered_problems)))
#     return selected_problems

# @app.route('/')
# def index():
#     # Fetch the entire Codeforces problemset
#     problemset = get_codeforces_problemset()

#     if problemset:
#         # Get random problems
#         random_problems = get_random_problems(problemset, count=5, difficulty="easy")

#         # Create a list of URLs for the problems
#         problem_urls = [f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}" for problem in random_problems]

#         # Render the HTML template with the list of URLs
#         return render_template('index.html', problem_urls=problem_urls)
#     else:
#         return "Failed to fetch the Codeforces problemset."

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import requests
# import random

# app = Flask(__name__)

# def get_codeforces_problemset():
#     base_url = "https://codeforces.com/api/problemset.problems"

#     try:
#         response = requests.get(base_url)
#         response.raise_for_status()  # Raise an error for bad responses

#         data = response.json()
#         problems = data.get("result", {}).get("problems", [])

#         return problems

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None

# def get_random_problems(problemset, count=5, difficulty="easy"):
#     difficulty_ranges = {
#         "easy": (800, 1500),
#         "medium": (1200, 2000),
#         "hard": (1900, 2900),
#         "Damn Hard":(2800,3500)
#     }

#     rating_range = difficulty_ranges.get(difficulty, (0, 0))
    
#     filtered_problems = [problem for problem in problemset if rating_range[0] <= problem.get('rating', 0) <= rating_range[1]]
#     selected_problems = random.sample(filtered_problems, min(count, len(filtered_problems)))
#     return selected_problems

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get difficulty from the form submission
#         user_difficulty_input = request.form.get('difficulty').lower()

#         # Fetch the entire Codeforces problemset
#         problemset = get_codeforces_problemset()

#         if problemset:
#             # Get random problems based on user input
#             random_problems = get_random_problems(problemset, count=5, difficulty=user_difficulty_input)

#             # Create a list of URLs for the problems
#             problem_urls = [f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}" for problem in random_problems]

#             # Render the HTML template with the list of URLs
#             return render_template('index.html', problem_urls=problem_urls)
#         else:
#             return "Failed to fetch the Codeforces problemset."

#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import requests
# import random

# app = Flask(__name__)

# def get_codeforces_problemset():
#     base_url = "https://codeforces.com/api/problemset.problems"

#     try:
#         response = requests.get(base_url)
#         response.raise_for_status()  # Raise an error for bad responses

#         data = response.json()
#         problems = data.get("result", {}).get("problems", [])

#         return problems

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None

# def get_random_problems(problemset, count=5, difficulty="easy"):
#     difficulty_ranges = {
#         "easy": (800, 1500),
#         "medium": (1200, 2000),
#         "hard": (1900, 2900)
#     }

#     rating_range = difficulty_ranges.get(difficulty, (0, 0))
    
#     filtered_problems = [problem for problem in problemset if rating_range[0] <= problem.get('rating', 0) <= rating_range[1]]
#     selected_problems = random.sample(filtered_problems, min(count, len(filtered_problems)))
#     return selected_problems

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get difficulty from the form submission
#         user_difficulty_input = request.form.get('difficulty').lower()

#         # Fetch the entire Codeforces problemset
#         problemset = get_codeforces_problemset()

#         if problemset:
#             # Get random problems based on user input
#             random_problems = get_random_problems(problemset, count=5, difficulty=user_difficulty_input)

#             # Create a list of dictionaries with name and rating
#             problems_info = [{'name': f"{problem['name']} ({problem['rating']})", 'url': f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"} for problem in random_problems]

#             # Render the HTML template with the list of problem information
#             return render_template('index.html', problems_info=problems_info)
#         else:
#             return "Failed to fetch the Codeforces problemset."

#     return render_template('form.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, session
import requests
import random
import time

app = Flask(__name__)

problems_info = []
timestamp = 0

def get_codeforces_problemset():
    base_url = "https://codeforces.com/api/problemset.problems"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()
        problems = data.get("result", {}).get("problems", [])

        return problems

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_random_problems(problemset, count=5, difficulty="easy"):
    difficulty_ranges = {
        "easy": (800, 1500),
        "medium": (1200, 2000),
        "hard": (1900, 2900),
        "Damn Hard":(2800,3500)
    }

    rating_range = difficulty_ranges.get(difficulty, (0, 0))

    filtered_problems = [problem for problem in problemset if rating_range[0] <= problem.get('rating', 0) <= rating_range[1]]
    selected_problems = random.sample(filtered_problems, min(count, len(filtered_problems)))
    return selected_problems

@app.route('/', methods=['GET', 'POST'])
def index():
    global problems_info
    global timestamp

    if request.method == 'POST':
        # Get difficulty from the form submission
        user_difficulty_input = request.form.get('difficulty').lower()

        # Fetch the entire Codeforces problemset
        problemset = get_codeforces_problemset()

        if problemset:
            # Check if the timestamp is still valid
            current_time = time.time()

            if current_time - timestamp > 60 * 5:  # Refresh every 5 minutes
                # Get random problems based on user input
                random_problems = get_random_problems(problemset, count=5, difficulty=user_difficulty_input)

                # Create a list of dictionaries with name and rating
                problems_info = [{'name': f"{problem['name']} ({problem['rating']})", 'url': f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"} for problem in random_problems]

                # Update the timestamp
                timestamp = current_time
            else:
                # If the timestamp is still valid, use the existing problems_info
                pass

            # Render the HTML template with the list of problem information
            return render_template('index.html', problems_info=problems_info)
        else:
            return "Failed to fetch the Codeforces problemset."

    # If problems_info is not empty, render the index page
    if problems_info:
        return render_template('index.html', problems_info=problems_info)

    # If problems_info is empty, render the form
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
