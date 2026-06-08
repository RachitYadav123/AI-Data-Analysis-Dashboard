{% extends "base.html" %}
{% block title %}Account{% endblock %}
{% block content %}
<h2>Account</h2>
<p>{{ current_user.name }} · {{ current_user.email }}</p>
<h4>Datasets</h4>
<ul class="list-group">
  {% for d in datasets %}
    <li class="list-group-item d-flex justify-content-between">
      <span>{{ d.original_filename }}</span>
      <span>{{ '{:,}'.format(d.row_count) }} rows · {{ d.column_count }} cols</span>
    </li>
  {% else %}
    <li class="list-group-item">No datasets yet.</li>
  {% endfor %}
</ul>
{% endblock %}
