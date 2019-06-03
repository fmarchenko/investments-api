(function(t){function e(e){for(var n,i,o=e[0],l=e[1],c=e[2],d=0,f=[];d<o.length;d++)i=o[d],s[i]&&f.push(s[i][0]),s[i]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(t[n]=l[n]);u&&u(e);while(f.length)f.shift()();return r.push.apply(r,c||[]),a()}function a(){for(var t,e=0;e<r.length;e++){for(var a=r[e],n=!0,o=1;o<a.length;o++){var l=a[o];0!==s[l]&&(n=!1)}n&&(r.splice(e--,1),t=i(i.s=a[0]))}return t}var n={},s={app:0},r=[];function i(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=t,i.c=n,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(a,n,function(e){return t[e]}.bind(null,n));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],l=o.push.bind(o);o.push=e,o=o.slice();for(var c=0;c<o.length;c++)e(o[c]);var u=l;r.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"56d7":function(t,e,a){"use strict";a.r(e);a("cadf"),a("551c"),a("f751"),a("097d");var n=a("2b0e"),s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("main",{attrs:{id:"app"}},[a("CalcView")],1)},r=[],i=(a("4989"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{staticClass:"calculate-view"},[a("div",{staticClass:"container"},[a("h1",{staticClass:"border-bottom mb-4"},[t._v("Calculate Investments Performance")]),a("div",{staticClass:"row"},[a("div",{staticClass:"col-12"},[a("form",{staticClass:"mb-4",on:{submit:function(e){return e.preventDefault(),t.handleSubmit(e)}}},[a("div",{staticClass:"form-row align-items-center"},[a("div",{staticClass:"col-auto"},[a("label",{staticClass:"sr-only",attrs:{for:"id_start_date"}},[t._v("Investments start date")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.start_date,expression:"start_date"}],staticClass:"form-control mb-2",attrs:{type:"date",id:"id_start_date",placeholder:"Investments start date",required:""},domProps:{value:t.start_date},on:{input:function(e){e.target.composing||(t.start_date=e.target.value)}}})]),a("div",{staticClass:"col-auto"},[a("label",{staticClass:"sr-only",attrs:{for:"id_amount"}},[t._v("Investments amount in USD")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.amount,expression:"amount"}],staticClass:"form-control mb-2",attrs:{type:"number",id:"id_amount",placeholder:"Investments amount"},domProps:{value:t.amount},on:{input:function(e){e.target.composing||(t.amount=e.target.value)}}})]),t._m(0)])])]),t.loading?a("div",{staticClass:"col-12 text-center"},[t._m(1)]):t._e(),t.result.length>0&&!t.loading?a("div",{staticClass:"col-12"},[a("ul",{staticClass:"nav nav-tabs",attrs:{role:"tablist"}},t._l(t.result,function(e,n){return a("li",{key:n,staticClass:"nav-item"},[a("a",{staticClass:"nav-link",class:{active:0==n},attrs:{href:"#"+e.asset,role:"tab","data-toggle":"tab"}},[t._v(t._s(e.asset))])])}),0),a("div",{staticClass:"tab-content"},t._l(t.result,function(e,n){return a("div",{key:n,staticClass:"tab-pane fade",class:{"show active":0==n},attrs:{role:"tabpanel",id:e.asset}},[a("h3",{staticClass:"pt-3 pb-3"},[t._v("Investment: #"+t._s(e.investment)+" start from "+t._s(new Date(e.open_date).toDateString())+"\n                            "),a("br"),a("small",{staticClass:"text-muted"},[t._v("on "+t._s(e.amount)+" USD")])]),a("table",{staticClass:"table table-striped"},[t._m(2,!0),a("tbody",t._l(e.performances,function(e,n){return a("tr",{key:n},[a("td",[t._v(t._s(n))]),a("td",[t._v(t._s(new Date(e.day).toDateString()))]),a("td",[t._v(t._s(e.profit))]),a("td",[t._v(t._s(e.profitability))]),a("td",[t._v(t._s(e.profitability_total))])])}),0)])])}),0)]):t._e()])])])}),o=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-auto"},[a("button",{staticClass:"btn btn-primary mb-2",attrs:{type:"submit",id:"id_send"}},[t._v("Calculate")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("p",{staticClass:"spinner-border",staticStyle:{width:"3rem",height:"3rem"}},[a("span",{staticClass:"sr-only"},[t._v("Loading...")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("thead",[a("tr",[a("th",[t._v("#")]),a("th",[t._v("Month")]),a("th",[t._v("Profit, USD")]),a("th",[t._v("Month Profitability, %")]),a("th",[t._v("Total Profitability, %")])])])}],l=a("bc3a"),c=a.n(l),u={name:"CalcView",data:function(){return{loading:!1,start_date:"2017-09-01",amount:1e3,result:[]}},methods:{handleSubmit:function(){var t=this,e=new Date(this.start_date),a="/api/v1/performance/".concat(e.getFullYear(),"/").concat(e.getMonth()+1,"/").concat(e.getUTCDate(),"/");this.amount>0&&(a+="".concat(this.amount,"/")),this.loading=!0,c.a.get(a).then(function(e){t.result=e.data.result,t.loading=!1})}}},d=u,f=a("2877"),v=Object(f["a"])(d,i,o,!1,null,null,null),m=v.exports,p={name:"app",components:{CalcView:m}},_=p,b=(a("5c0b"),Object(f["a"])(_,s,r,!1,null,null,null)),h=b.exports;n["a"].config.productionTip=!1,new n["a"]({render:function(t){return t(h)}}).$mount("#app")},"5c0b":function(t,e,a){"use strict";var n=a("5e27"),s=a.n(n);s.a},"5e27":function(t,e,a){}});
//# sourceMappingURL=app.js.map