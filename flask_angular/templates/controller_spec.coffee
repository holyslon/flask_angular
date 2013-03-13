{% extends "base_spec.coffee" %}
{% block target_type_plural %}controller{% endblock %}
{% block target_type %}controller{% endblock %}
{% block item_instantiation %}
        angular.mock.inject ($location, $rootScope, $controller) =>
            @scope = $rootScope.$new();
            @location = $location
            @ctrl = $controller("{{name}}", { $scope: @scope });  
{% endblock item_instantiation %}
