describe "{{name}} {% block target_type_plural %}{% endblock %} tests", ->

    beforeEach =>
        angular.mock.module "{{module}}", ($provide) =>
            return
        {% block item_instantiation %}
        angular.mock.inject ($injector) =>
            @{% block target_type %}{% endblock target_type %} = $injector.get('{{name}}');
        {% endblock item_instantiation %}
    it "Should first test for {{name}}", ()=>
        expect(true).toBe(false)