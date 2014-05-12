'use strict';

angular.module('myApp.controllers', []).

   controller('ReportController', ['$scope', '$filter',  'Restangular', function($scope, $filter, Restangular) {
	$scope.categories = Restangular.all("categories").getList().$object;
	$scope.districts = Restangular.all("districts").getList().$object;
	$scope.years = Restangular.all("years").getList().$object;

	$scope.orderByField = 'taluk';
    $scope.reverseSort = false;

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

    $scope.showTableHeader = false;
    $scope.values = null;
    $scope.getValues = function($categoryId, $parameterId, $subparameterId, $districtId, $talukId, $yearId) {
        $categoryId = (typeof $categoryId === "undefined") ? 0 : $categoryId;
        $parameterId = (typeof $parameterId === "undefined") ? 0 : $parameterId;
        $subparameterId = (typeof $subparameterId === "undefined") ? 0 : $subparameterId;
        $districtId = (typeof $districtId === "undefined") ? 0 : $districtId;
        $talukId = (typeof $talukId === "undefined") ? 0 : $talukId;
        $yearId = (typeof $yearId === "undefined") ? 0 : $yearId;
	    $scope.values =  Restangular.all("values?categoryId=" + $categoryId + "&parameterId=" + $parameterId +
            "&subparameterId=" + $subparameterId + "&districtId=" + $districtId + "&talukId=" + $talukId +
            "&yearId=" + $yearId).getList().$object;
        $scope.showTableHeader = true;
        };

  }]).

   controller('CategoryMenuController', ['$scope', '$location', 'Restangular', function($scope, $location, Restangular) {
	$scope.categories = Restangular.all("categories").getList().$object;
	$scope.getValuesWithParameterId = function($categoryId, $parameterId) {
	    $location.path('/viewreport/' + $categoryId + '/' + $parameterId + '/0/0/0/0');
    };
  }]).

   controller('ViewReportController', ['$scope', '$routeParams', 'Restangular', function($scope, $routeParams, Restangular) {
   $scope.orderByField = 'taluk';
   $scope.reverseSort = false;

   $scope.categoryId = $routeParams.categoryId;
   $scope.parameterId = $routeParams.parameterId;
   $scope.subparameterId = $routeParams.subparameterId;
   $scope.districtId = $routeParams.districtId;
   $scope.talukId = $routeParams.talukId;
   $scope.yearId = $routeParams.yearId;
   $scope.values =  Restangular.all("values?categoryId=" + $scope.categoryId + "&parameterId=" + $scope.parameterId +
    "&subparameterId=" + $scope.subparameterId + "&districtId=" + $scope.districtId + "&talukId=" + $scope.talukId +
    "&yearId=" + $scope.yearId).getList().$object;
  }]).

   controller('InfographicsController', ['$scope', 'Restangular', function($scope, Restangular) {

       $scope.categories = Restangular.all("categories").getList().$object;
       $scope.districts = Restangular.all("districts").getList().$object;

       $scope.parameters = null;
       $scope.subparameters = null;

       $scope.selectedCategory = null;
       $scope.selectedParameter = null;
	   $scope.selectedSubparameter = null;
       $scope.selectedDistrict = null;

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

       $scope.values2010 = null;
       $scope.values2011 = null;
       $scope.values2012 = null;
       $scope.getValues = function($subparameterId, $districtId, $chartType) {
           $subparameterId = (typeof $subparameterId === "undefined") ? 0 : $subparameterId;
           $districtId = (typeof $districtId === "undefined") ? 0 : $districtId;
	       Restangular.all("values?categoryId=0&parameterId=0&subparameterId=" + $subparameterId +
	        "&districtId=" + $districtId + "&talukId=0&yearId=1").getList().then(function(result){$scope.values2010 = result; $scope.call(1, $scope.values2010, $chartType); });
	       Restangular.all("values?categoryId=0&parameterId=0&subparameterId=" + $subparameterId +
	        "&districtId=" + $districtId + "&talukId=0&yearId=2").getList().then(function(result){$scope.values2011 = result; $scope.call(2, $scope.values2011, $chartType); });
	       Restangular.all("values?categoryId=0&parameterId=0&subparameterId=" + $subparameterId +
	        "&districtId=" + $districtId + "&talukId=0&yearId=3").getList().then(function(result){$scope.values2012 = result; $scope.call(3, $scope.values2012, $chartType); });
        };


       $scope.call = function($divId, $data, $chartType) {
             d3.select('#chart' + $divId).select("svg").remove();
             var dict = [];
             for (var i = 0, len = $data.length; i < len; i++) {
                        dict.push({"label" : $data[i].taluk, "value" : $data[i].value});
             }

             if($chartType==="bar") {

                nv.addGraph(function() {
                 var chart = nv.models.discreteBarChart()
                    .x(function(d) { return d.label })
                    .y(function(d) { return d.value })
                    .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
                    .tooltips(true)        //Don't show tooltips
                    .showValues(true)       //...instead, show the bar value right on top of each bar.
                    .transitionDuration(350)
                 ;
                d3.select('#chart' + $divId)
                .append('svg')
                .datum(barData())
                .call(chart);

                nv.utils.windowResize(chart.update);

                return chart;
                });
             } else if($chartType==="donut") {

                nv.addGraph(function() {
                    var chart = nv.models.pieChart()
                    .x(function(d) { return d.label })
                    .y(function(d) { return d.value })
                    .showLabels(true)     //Display pie labels
                    .labelThreshold(.10)  //Configure the minimum slice size for labels to show up
                    .labelType("percent") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
                    .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
                    .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
                    ;

                    d3.select('#chart' + $divId)
                    .append('svg')
                    .datum(pieData())
                    .transition().duration(350)
                    .call(chart);

                    nv.utils.windowResize(chart.update);

                return chart;
                });
             } else if(typeof $chartType === 'undefined') {
                nv.addGraph(function() {
                     var chart = nv.models.pieChart()
                    .x(function(d) { return d.label })
                    .y(function(d) { return d.value })
                    .showLabels(true);

                     d3.select('#chart' + $divId)
                     .append('svg')
                     .datum(pieData())
                     .transition().duration(350)
                     .call(chart);

                     nv.utils.windowResize(chart.update);

                return chart;
                });
             }

            function barData() {
            return  [
            {
                key: "Cumulative Return",
                values: dict
            }
            ]
            }

            function pieData() {
            return  dict
            }
       };
  }]).controller('TreeController', ['$scope', 'Restangular', function($scope, Restangular) {

  }]);

