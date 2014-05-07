'use strict';

angular.module('myApp.controllers', []).

   controller('FakeController', ['$scope', 'Restangular', function($scope, Restangular) {
	$scope.projects = Restangular.one("import").get();
  }]).

   controller('CategoryMenuController', ['$scope', 'Restangular', function($scope, Restangular) {
	$scope.categories = Restangular.all("categories").getList().$object;
	$scope.getValuesWithParameterId = function(parameterId) {
	    $scope.subparameters = Restangular.one("parameters", parameterId).get().$object;
        console.log($scope.subparameters);
    };
/*	[
        {id : 7, name : 'Philippines', parameters : [{"id": 1, "name": "Hoblies"},{"id": 2, "name": "Revenue Circles"}] },
        {id : 8, name : 'Canada', parameters : [{"id": 1, "name": "Hoblies"},{"id": 2, "name": "Revenue Circles"}] },
        {id : 9, name : 'China', parameters : [{"id": 1, "name": "Hoblies"},{"id": 2, "name": "Revenue Circles"}] }
         ]; */
  }]);