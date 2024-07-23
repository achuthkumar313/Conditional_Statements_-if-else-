# Conditional statements (if-else) using Jinja tags in Django:

1. Basic if Statement:
* Use the {% if %} tag to check a condition.
* If the condition is true, the content within the {% if %} and {% endif %} tags will be rendered.
  Example:
  HTML
  {% if user.authenticated %}
    Hi, {{ user.username }}
  {% endif %}

2. if-else Statement:
* Use {% else %} to display alternative content if the initial condition is false.
  Example:
  HTML
  {% if user.authenticated %}
    Hi, {{ user.username }}
  {% else %}
    Please log in to continue.
  {% endif %}


Remember:
* Indentation matters in Jinja templates.
* Always close if statements with {% endif %}.
* Use Jinja test operators appropriately within conditions.
