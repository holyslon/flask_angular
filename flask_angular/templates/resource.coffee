module = angular.module("{{module}}")

{{name}} = ($resource) ->
    $resource "{{path_to_resource}}"

module.factory "{{name}}", {{name}}