module = angular.module("{{module}}")

{{name}} = (data) ->
    data

factory = () -> {{name}}
factory.$inject = []

module.filter "{{name}}", factory