'use strict';

angular.module('myApp', ['ngRoute', 'restangular', 'angularFileUpload', 'myApp.services', 'myApp.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/reporting', {templateUrl: 'views/reporting.html', controller: 'ReportController'});
    $routeProvider.when('/viewreport/:categoryId/:parameterId/:subparameterId/:districtId/:talukId/:yearId', {templateUrl: 'views/viewreport.html', controller: 'ViewReportController'});
    $routeProvider.when('/infographics', {templateUrl: 'views/infographics.html', controller: 'InfographicsController'});
    $routeProvider.when('/trees', {templateUrl: 'views/tree.html', controller: 'TreeController'});
	$routeProvider.otherwise({redirectTo: '/reporting'});
  }]).
  config(['RestangularProvider', function(RestangularProvider) {
      RestangularProvider.setBaseUrl('../ra');
	  RestangularProvider.setDefaultHeaders({ 'Accept': 'text/html,application/json;q=0.9,*/*;q=0.8' });
      RestangularProvider.setRestangularFields({
        id: '_id.$oid'
      });
      
      RestangularProvider.setRequestInterceptor(function(elem, operation, what) {
        if (operation === 'put') {
          elem._id = undefined;
          return elem;
        }
        return elem;
      });
  }]);;