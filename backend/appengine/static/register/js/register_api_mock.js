var rest = angular.module('rest', [])
        rest.factory('RegisterApi', function($rootScope){
            return {
                salvar: function(register){
                    var obj={}
                    obj.success = function(fcnSucesso){
                        obj.fcnSucesso = fcnSucesso;
                    };
                    obj.error = function(fcnErro){
                        obj.fcnErro = fcnErro;
                    };

                    setTimeout(function(){
                    register.id = 1;
                    obj.fcnSucesso(register)
                        $rootScope.$digest();
                    }, 1000);

                    return obj;
                }
            };
        });
