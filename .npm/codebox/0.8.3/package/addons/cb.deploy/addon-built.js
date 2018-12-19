define("client",[],function(){var e=codebox.require("hr/promise"),t=codebox.require("hr/utils"),n=codebox.require("utils/dialogs"),r=codebox.require("core/box"),i=codebox.require("core/backends/rpc"),s=codebox.require("models/command"),o=codebox.require("core/commands/menu"),u=codebox.require("core/user"),a=codebox.require("vendors/crypto"),f=u.settings("deploymentSolutions"),l=function(){return i.execute("deploy/solutions")},c=function(e){return l().then(function(n){var r=t.find(n,function(t){return t.id==e});if(!r)throw"Invalid solution type";return r})},h=function(e){return a.MD5(e).toString()},p=function(t,n){var r=f.get("solutions",{}),i=h(t);return r[i]?e.reject("Solution already exists"):(r[i]={name:t,type:n,settings:{}},f.set("solutions",r),f.save().then(function(){return r[i]}))},d=function(t){var n=f.get("solutions",{});return n[t]?(delete n[t],f.set("solutions",n),f.save()):e.reject("Invalid solution")},v=function(e,s){return t.isString(e)&&(e=m(e)),i.execute("deploy/run",{solution:e.type,action:s,config:e.settings}).then(function(t){t.shellId?r.openTerminal(t.shellId,{id:"deploy."+h(e.name)+"."+s,title:t.title||"Deployment to "+e.name+" ("+s+")",icons:{"default":"fa-cloud-upload"}}):t.message&&n.alert("Deployment to "+e.name+" ("+s+")",t.message)},function(t){n.alert("Error with "+e.name,t.message||t)})},m=function(e){var t=f.get("solutions",{});return t[e]},g=function(e,t){var n=f.get("solutions",{});n[e].settings=t,f.set("solutions",n)},y=function(e){var r=m(e);return c(r.type).then(function(e){return n.fields("Configuration for "+t.escape(r.name),e.settings,r.settings)}).then(function(t){return g(e,t),f.save()})},b=s.register("deploy.solutions.add",{category:"Deployment",title:"Add Solution",description:"Add a solution",offline:!1,action:function(e){l().then(function(e){return n.fields("Add Deployment Solution",{name:{type:"text",label:"Label"},solution:{type:"select",label:"Type",options:t.object(t.map(e,function(e){return[e.id,e.name]}))}})}).then(function(e){if(!e.name||!e.solution)throw"Need 'name' and 'solution'";return p(e.name,e.solution)}).then(function(e){return y(h(e.name))})}}),w=s.register("deploy.solutions.remove",{category:"Deployment",title:"Remove Solution",description:"Remove a solution",offline:!1,action:function(){n.select("Remove Deployment Solution","Select a solution, this solution and its configuration will be removed from your settings.",t.chain(f.get("solutions",{})).map(function(e,t){return[t,e.name]}).object().value()).then(d)}}),E=o.register("deploy",{title:"Deploy",position:90,offline:!1}),S=function(){return l().then(function(e){var n=f.get("solutions",{});E.clearMenu(),E.menuSection(t.compact([b,t.size(n)>0?w:null]));if(t.size(n)==0)return;E.menuSection(t.chain(n).map(function(n,r){var i=t.find(e,function(e){return e.id==n.type});if(!i)return null;var o=s.register({title:n.name,type:"menu",offline:!1,action:function(){y(r(n.name))}});return o.menuSection(t.map(i.actions,function(e){return{title:e.name,offline:!1,action:function(){return v(n,e.id)}}})),o.menuSection([{title:"Configure",offline:!1,action:function(){y(r)}}]),o}).compact().value())})};S(),f.change(S)});