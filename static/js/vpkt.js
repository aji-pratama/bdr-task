var data = { checked : [] }

Vue.component('cbx', {
  template:
  `
  <div id="vpp">
  		<input type="checkbox" value="yes1" v-model="checked">
  		Jack
  		<input type="checkbox" value="yes2" v-model="checked">
  		John
  		<input type="checkbox" value="yes3" v-model="checked">
  		Mike
  		<br>
  		<span>Checked names: {{ checked }}</span>
  </div>
  `,
  data: function() {
    return data
  }
})


// Vue.component('test-com', {
//   template: '<p>{{ message }}</p>',
//   data: function() {
//     return data
//   }
// })
// create a root instance
new Vue({
  el: '#vpkt'
})
