{% extends "base_spec.coffee" %}
{% block target_type_plural %}filter{% endblock %}
{% block target_type %}filter{% endblock %}
{% block item_instantiation %}
        inject ($filter) =>
            @filter = $filter('{{name}}'); 
{% endblock item_instantiation %}

