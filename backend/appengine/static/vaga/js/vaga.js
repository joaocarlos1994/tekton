var vagaModulo=angular.module('vagaModulo',[]);

vagaModulo.directive('vagaform', function(){
    return{
        restrict: 'E',
        replace: true,
        templateUrl: 'static/vaga/html/vaga_form.html'
    };
});