{% extends "base.html"%}
{% import "bootstrap/wtf.html "%}
{% block content %}
<form method="POST">
    {{ wtf.quick_form(form)}}
</form>