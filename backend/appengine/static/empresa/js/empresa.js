var empresaModulo=angular.module('empresaModulo',[]);

empresaModulo.directive('empresaform', function(){
    return{
        restrict: 'E',
        replace: true,
        templateUrl: 'static/empresa/html/empresa_form.html'
    };
});