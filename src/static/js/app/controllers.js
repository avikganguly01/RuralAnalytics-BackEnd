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
             } else if(typeof $chartType === 'undefined' || $chartType.length == 0) {
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
        $scope.tree = null;
        Restangular.one("dtree").get().then(function(result){$scope.tree = result; $scope.call(); });

        $scope.call = function() {
            var m = [20, 120, 20, 120],
            w = 1280 - m[1] - m[3],
            h = 800 - m[0] - m[2],
            i = 0,
            rect_width = 80,
            rect_height = 20,
            max_link_width = 20,
            min_link_width = 1.5,
            char_to_pxl = 6,
            root;
            var json = $scope.tree;
            console.log(json);

            var tree = d3.layout.tree()
            .size([h, w]);

            var diagonal = d3.svg.diagonal()
            .projection(function(d) { return [d.x, d.y]; });

            var vis = d3.select("#body").append("svg:svg")
            .attr("width", w + m[1] + m[3])
            .attr("height", h + m[0] + m[2] + 1000)
            .append("svg:g")
            .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

            // global scale for link width
            var link_stoke_scale = d3.scale.linear();

            var color_map = d3.scale.category10();

            // stroke style of link - either color or function
            var stroke_callback = "#ccc";

            root = json;
            root.x0 = 0;
            root.y0 = 0;

            var n_samples = root.samples;


            link_stoke_scale = d3.scale.linear()
                                     .domain([0, n_samples])
                                     .range([min_link_width, max_link_width]);

            function toggleAll(d) {
            if (d && d.children) {
              d.children.forEach(toggleAll);
              toggle(d);
            }
            }

            // Initialize the display to show a few nodes.
            root.children.forEach(toggleAll);

            update(root);

            function update(source) {
            var duration = d3.event && d3.event.altKey ? 5000 : 500;

            // Compute the new tree layout.
            var nodes = tree.nodes(root).reverse();

            // Normalize for fixed-depth.
            nodes.forEach(function(d) { d.y = d.depth * 180; });

            // Update the nodes�
            var node = vis.selectAll("g.node")
              .data(nodes, function(d) { return d.id || (d.id = ++i); });

            // Enter any new nodes at the parent's previous position.
            var nodeEnter = node.enter().append("svg:g")
              .attr("class", "node")
              .attr("transform", function(d) { return "translate(" + source.x0 + "," + source.y0 + ")"; })
              .on("click", function(d) { toggle(d); update(d); });

            nodeEnter.append("svg:rect")
              .attr("x", function(d) {
                var label = node_label(d);
                var text_len = label.length * char_to_pxl;
                var width = d3.max([rect_width, text_len])
                return -width / 2;
              })
              .attr("width", 1e-6)
              .attr("height", 1e-6)
              .attr("rx", function(d) { return d.type === "split" ? 2 : 0;})
              .attr("ry", function(d) { return d.type === "split" ? 2 : 0;})
              .style("stroke", function(d) { return d.type === "split" ? "steelblue" : "olivedrab";})
              .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

            nodeEnter.append("svg:text")
              .attr("dy", "12px")
              .attr("text-anchor", "middle")
              .text(node_label)
              .style("fill-opacity", 1e-6);

            // Transition nodes to their new position.
            var nodeUpdate = node.transition()
              .duration(duration)
              .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

            nodeUpdate.select("rect")
              .attr("width", function(d) {
                var label = node_label(d);
                var text_len = label.length * char_to_pxl;
                var width = d3.max([rect_width, text_len])
                return width;
              })
              .attr("height", rect_height)
              .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

            nodeUpdate.select("text")
              .style("fill-opacity", 1);

            // Transition exiting nodes to the parent's new position.
            var nodeExit = node.exit().transition()
              .duration(duration)
              .attr("transform", function(d) { return "translate(" + source.x + "," + source.y + ")"; })
              .remove();

            nodeExit.select("rect")
              .attr("width", 1e-6)
              .attr("height", 1e-6);

            nodeExit.select("text")
              .style("fill-opacity", 1e-6);

            // Update the links
            var link = vis.selectAll("path.link")
              .data(tree.links(nodes), function(d) { return d.target.id; });

            // Enter any new links at the parent's previous position.
            link.enter().insert("svg:path", "g")
              .attr("class", "link")
              .attr("d", function(d) {
                var o = {x: source.x0, y: source.y0};
                return diagonal({source: o, target: o});
              })
              .transition()
              .duration(duration)
              .attr("d", diagonal)
              .style("stroke-width", function(d) {return link_stoke_scale(d.target.samples);})
              .style("stroke", stroke_callback);

            // Transition links to their new position.
            link.transition()
              .duration(duration)
              .attr("d", diagonal)
              .style("stroke-width", function(d) {return link_stoke_scale(d.target.samples);})
              .style("stroke", stroke_callback);

            // Transition exiting nodes to the parent's new position.
            link.exit().transition()
              .duration(duration)
              .attr("d", function(d) {
                var o = {x: source.x, y: source.y};
                return diagonal({source: o, target: o});
              })
              .remove();

            // Stash the old positions for transition.
            nodes.forEach(function(d) {
            d.x0 = d.x;
            d.y0 = d.y;
            });
            }

            // Toggle children.
            function toggle(d) {
            if (d.children) {
            d._children = d.children;
            d.children = null;
            } else {
            d.children = d._children;
            d._children = null;
            }
            }

            // Node labels
            function node_label(d) {
            if (d.type === "leaf") {
            // leaf
            var formatter = d3.format(".2f");
            var vals = [];
            d.value.forEach(function(v) {
                vals.push(formatter(v));
            });
            return "[" + vals.join(", ") + "]";
            } else {
            // split node
            return d.label;
            }
            }

            /**
            * Mixes colors according to the relative frequency of classes.
            */
            function mix_colors(d) {
            var value = d.target.value;
            var sum = d3.sum(value);
            var col = d3.rgb(0, 0, 0);
            value.forEach(function(val, i) {
            var label_color = d3.rgb(color_map(i));
            var mix_coef = val / sum;
            col.r += mix_coef * label_color.r;
            col.g += mix_coef * label_color.g;
            col.b += mix_coef * label_color.b;
            });
            return col;
            }


            /**
            * A linear interpolator for value[0].
            *
            * Useful for link coloring in regression trees.
            */
            function mean_interpolation(root) {

            var max = 1e-9,
              min = 1e9;

            function recurse(node) {
            if (node.value[0] > max) {
              max = node.value[0];
            }

            if (node.value[0] < min) {
              min = node.value[0];
            }

            if (node.children) {
              node.children.forEach(recurse);
            }
            }
            recurse(root);

            var scale = d3.scale.linear().domain([min, max])
                                       .range(["#2166AC","#B2182B"]);

            function interpolator(d) {
            return scale(d.target.value[0]);
            }

            return interpolator;
            }
        };
  }]);

