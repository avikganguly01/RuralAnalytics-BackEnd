'use strict';

angular.module('myApp.controllers', []).

   controller('ReportController', ['$scope', '$location', 'Restangular', function($scope, $location, Restangular) {
	$scope.categories = Restangular.all("categories").getList().$object;
	$scope.districts = Restangular.all("districts").getList().$object;
	$scope.years = Restangular.all("years").getList().$object;

	$scope.parameters = null;
    $scope.subparameters = null;
    $scope.taluks = null;

	$scope.selectedYear = null;
	$scope.selectedCategory = null;
	$scope.selectedSubparameter = null;
    $scope.selectedDistrict = null;
    $scope.selectedTaluk = null;
    $scope.selectedParameter = null;


	$scope.$watch('selectedCategory', function(newValue){
	   if(newValue != null) {
	       $scope.parameters = newValue.parameters;
        }
    });

    $scope.$watch('selectedParameter', function(newValue){
	   if(newValue != null) {
	       $scope.subparameters = newValue.subparameters;
        }
    });

    $scope.$watch('selectedDistrict', function(newValue){
	   if(newValue != null) {
	       $scope.taluks = newValue.taluks;
        }
    });

    $scope.getValues = function($categoryId, $parameterId, $subparameterId, $districtId, $talukId, $yearId) {
        $categoryId = (typeof $categoryId === "undefined") ? 0 : $categoryId;
        $parameterId = (typeof $parameterId === "undefined") ? 0 : $parameterId;
        $subparameterId = (typeof $subparameterId === "undefined") ? 0 : $subparameterId;
        $districtId = (typeof $districtId === "undefined") ? 0 : $districtId;
        $talukId = (typeof $talukId === "undefined") ? 0 : $talukId;
        $yearId = (typeof $yearId === "undefined") ? 0 : $yearId;
	    $location.path('/viewreport/' + $categoryId + '/' + $parameterId + '/' + $subparameterId + '/' + $districtId + '/' + $talukId + '/' + $yearId);
    };
  }]).

   controller('CategoryMenuController', ['$scope', '$location', 'Restangular', function($scope, $location, Restangular) {
	$scope.categories = Restangular.all("categories").getList().$object;
	$scope.getValuesWithParameterId = function($categoryId, $parameterId) {
	    $location.path('/viewreport/' + $categoryId + '/' + $parameterId + '/0/0/0/0');
    };
  }]).

   controller('ViewReportController', ['$scope', '$routeParams', 'Restangular', function($scope, $routeParams, Restangular) {
   $scope.categoryId = $routeParams.categoryId;
   $scope.parameterId = $routeParams.parameterId;
   $scope.subparameterId = $routeParams.subparameterId;
   $scope.districtId = $routeParams.districtId;
   $scope.talukId = $routeParams.talukId;
   $scope.yearId = $routeParams.yearId;
   $scope.values =  Restangular.all("values?categoryId=" + $scope.categoryId + "&parameterId=" + $scope.parameterId +
    "&subparameterId=" + $scope.subparameterId + "&districtId=" + $scope.districtId + "&talukId=" + $scope.talukId +
    "&yearId=" + $scope.yearId).getList().$object;
  }]);

