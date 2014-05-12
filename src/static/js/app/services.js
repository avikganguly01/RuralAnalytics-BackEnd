'use strict';

angular.module('myApp.services', [])
  .service('sampleService', ['Restangular', function SomeOtherVariableService (Restangular) {
    'use strict';

     return {
        getSomeOtherVariable: function(someParameter, someOtherParameter){
            return Restagular.one('someVariable').get({
            	someParameter: someParameter,
              	someOtherParameter: someOtherParameter
            });
        }
    };
  }]);