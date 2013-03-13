module = angular.module "{{module}}"

class {{name}}

    constructor: () ->

factory = () ->
    new {{name}}() 


factory.$inject = []
module.factory '{{name}}', factory