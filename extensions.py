{% extends "base.html" %}
{% block title %}Register{% endblock %}
{% block content %}
<div class="auth-card">
  <h2>Create account</h2>
  <form method="post">
    <label>Name</label>
    <input class="form-control" type="text" name="name" required>
    <label class="mt-3">Email</label>
    <input class="form-control" type="email" name="email" required>
    <label class="mt-3">Password</label>
    <input class="form-control" type="password" name="password" minlength="8" required>
    <button class="btn btn-primary w-100 mt-3" type="submit">Create account</button>
  </form>
</div>
{% endblock %}
