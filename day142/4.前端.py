"""
前端
"""

# 1. 响应式布局
"""
    @media属性
"""

# 2. bootstrap常用属性


# 3. this到底谁？
"""
    name = 'alex'
    function func(){
        console.log(this.name); # window.name
    }
    func()
    -----------------
    var name = 'alex';
    function func() {
        var name = 'mjj';

        function inner() {
            console.log(this.name); // window
        }
        inner()
    }
    
    --------------
    var name = 'alex';

    function func() {
        var name = 'mjj';

        (function(){
            console.log(this.name); // window
        })();
    }

    func();
    ----------------
    var name = 'alex';
    var v = {
        name:'mjj',
        func:function () {
            console.log(this.name);
        }
    };
    v.func()
    ----------------
    var name = 'alex';
    var v = {
        name:'mjj',
        func:function () {
            console.log(this.name); // mjj
            
            (function () {
                console.log(this.name); // alex
            })()
        }
    };
    v.func()
    ---------------
    var name = 'alex';
    var v = {
        name:'mjj',
        func:function () {
            console.log(this.name); // mjj
            var that = this;
            (function () {
                console.log(that.name); // mjj
            })()
        }
    };
    v.func()
"""


# 4. vue.js