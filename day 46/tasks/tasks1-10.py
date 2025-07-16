# 1. Short note on Flask
# Flask is a lightweight, open-source Python web framework. It follows the WSGI standard and the Werkzeug toolkit. It provides the essentials to build a web app, while letting developers add only what they need.

# 2. Flask vs Django — 5 differences
# Feature	Flask	Django
# Framework type	Microframework	Full-stack framework
# Project structure	Minimal, developer defines it	Comes with a defined project layout
# Admin interface	No built-in admin	Has a powerful built-in admin panel
# Flexibility	Very flexible, more control	Convention-over-configuration, less flexible
# Learning curve	Easier for beginners	Steeper due to many built-in features

# 3. 3 pros & 3 cons of Flask
# Pros:

# Lightweight and simple to get started

# Flexible — you choose your tools

# Great for small to medium applications

#  Cons:

# No built-in admin or authentication

# Can require more boilerplate for bigger apps

# More chances of inconsistent structure in larger teams

# 4. Best-suited projects
# Flask is ideal for:

# Prototyping or MVPs (e.g., a startup’s first version)

# REST APIs (e.g., backend for a mobile app)

# Small-to-medium web apps (e.g., blog, personal site)

# Example: A simple ToDo app, or a blog with basic authentication.

# 5. Project setup complexity
# Flask: Minimal setup, create a .py file, define routes — up and running.

# Django: Runs django-admin startproject, sets up multiple files/folders. More boilerplate.

# 6. Role of WSGI
# WSGI (Web Server Gateway Interface) is a standard for Python web apps to communicate with web servers. Flask uses Werkzeug, a WSGI toolkit. When you run app.run(), Flask uses WSGI to handle HTTP requests/responses.

# 7. 5 companies/platforms using Flask
# Netflix — internal tools

# Reddit — some microservices

# Lyft — APIs and internal dashboards

# Pinterest — for parts of the stack

# AirBnB — internal tools and microservices

# 8. Mind map
# pgsql
# Copy
# Edit
#            
#                  Web Frameworks 
#           
#                /              \
#           Flask             Django
#            |                  |
#    Microframework       Full-stack
#            |                  |
#  Flexible, minimal     Batteries-included
#            |                  |
#  Build APIs, MVPs       Admin, ORM, Auth
# 9. Reasons Flask is beginner-friendly
# Minimal setup — one file can run the app.

# Simple routing — easy to understand @app.route().

# Flexible — less “magic”.

# Excellent documentation.

# Large supportive community.

# 10. Sample use-case: TODO app
# A TODO app is simple: user adds, updates, deletes tasks. Flask is ideal because:

# You don’t need a heavy ORM like Django’s.

# Minimal routes: /add, /delete, /list

# You can serve an API or HTML easily.

# Faster to prototype and learn.

