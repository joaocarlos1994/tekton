var registerModulo = angular.module('registerModulo', ['rest']);

registerModulo.directive('registerform', function () {
    return{
        restrict: 'E',
        replace: true,
        templateUrl: 'static/register/html/register_form.html',
        scope: {
            register: '=',
            nomeLabel:'@',
            sobreNomeLabel: '@',
            enderecoLabel: '@',
            emailLabel: '@'
        },
        controller: function ($scope, RegisterApi) {
            $scope.salvandoFlag = false;
            $scope.salvar = function () {
                $scope.salvandoFlag = true;
                $scope.errors = {};
                var promessa = RegisterApi.salvar($scope.register);
                promessa.success(function (register) {

                    $scope.register.nome = '';
                    $scope.register.sobreNome = '';
                    $scope.register.endereco = '';
                    $scope.register.email = '';

                    $scope.salvandoFlag = false;

                })
                promessa.error(function (errors) {
                    $scope.errors = errors;
                    $scope.salvandoFlag = false;
                });


            }

        }
    };
});


registerModulo.directive('registerlinha', function () {
    return{
        restrict: 'E',
        replace: true,
        templateUrl: 'static/register/html/register_linha.html',
        scope: {
            register: '='
        },
        controller: function ($scope, RegisterApi) {

        }
    };
});
