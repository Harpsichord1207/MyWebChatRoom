var myapp = angular.module("myapp", []);
myapp.controller("MsgCtrl", ["$http", "$timeout", function ($http, $timeout) {


    // Set Parameters Here
    this.msg = "";
    this.user = "";
    this.avatar_id = "1";
    this.content = [];
    var self = this;
    var socket = io.connect("http://" + document.domain + ":" + location.port);

    // Avatar functions
    this.get_avatar = function (id) {
      return "static/images/avatars/" + id + '.jpg';
    };
    this.change_avatar = function (id) {
        self.avatar_id = '' + id;
    };


    //Messages constrict and style
    this.check = function () {
        return self.msg.length > 200;
    };
    this.constrict = function () {
        return self.check() ? {"color": "red"} : {"color": "black"};
    };
    this.input_style = function (value) {
        var color = (value.length === 0 ? "crimson" : "darkcyan");
        return {"outline-color": color}
    };


    // Send and Receive Messages
    this.enter_keypress = function (e) {
        // console.log(e);
        var keycode = window.event?e.keyCode:e.which;
        if (keycode === 13) {
            self.click()
        }
    };

    this.click = function () {
        if (self.user.length * self.msg.length > 0) {
            self.user = self.user.slice(0, 10);
            socket.emit("message",{
                'msg': self.msg,
                'user': self.user,
                'avatar_id': self.avatar_id
            });
            self.msg = "";
        } else if (self.user.length === 0){
            document.querySelector("input").focus();
        } else {
            document.querySelector("textarea").focus();
        }
    };
    socket.on("res", function () {
        $http({
            method: "GET",
            url: "/api/get/"
        }).then(function (value) {
            // console.log(value.data);
            self.content.push(value.data);
        })
    });


    // Chat box style
    this.chat_style = function (status) {
        if (status === "self") {
            return {
                "background": "#0ace36"
            }
        } else {
            return {
                "background": "#92a1a4"
            }
        }
    };


    // Avatar Selector Style and Face tip
    this.show_avatar_selector = false;
    this.show_face_tip = false;
    this.show_element = function (para) {
      return para ? {"display": "block"} : {"display": "none"};
    };
    this.change_avatar_selector_style = function () {
        this.show_avatar_selector = !this.show_avatar_selector;
        this.show_element(this.show_avatar_selector);
    };
    this.change_face_tip_style = function () {
        this.show_face_tip = !this.show_face_tip;
        this.show_element(this.show_face_tip);
        if (this.show_face_tip){
            $timeout(function () {
            self.show_face_tip = false;
        }, 3000)
        }
    };
}]);


// To make the scroll-bar at the bottom
myapp.directive('repeatFinish', function () {
    return {
        restrict: "C",
        link: function (scope, element, attr) {
            if(scope.$last == true){
                // console.log("ng-Repeat Finished");
                var chat_area = document.querySelector(".content-area");
                chat_area.scrollTop = chat_area.scrollHeight;
            }
        }
    }
});