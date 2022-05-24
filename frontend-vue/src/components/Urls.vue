<template>
<p></p>
<div class="grid grid-cols-3 gap-6">
  <div class="col-span-3 sm:col-span-2">
    <label for="company-website" class="block text-sm font-medium text-gray-700"> New Link </label>
    <div class="mt-1 flex rounded-md shadow-sm">
      <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 text-sm"> http:// </span>
      <input type="text" name="newurl" id="newurl" class="focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-none rounded-r-md sm:text-sm border-gray-300" placeholder="https://www.example.com" v-model="newUrl" />
      <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" @click="submit()">Save</button>
    </div>
  </div>
</div>
<div class="px-4 py-3 bg-gray-50 text-right sm:px-6">
</div>
  <!-- <input type="text" name="newurl" v-model="newUrl" /> 
  <button @click="submit()" type="">Add new</button> -->
  <ul class="list-none">
    <li :key="item.id" v-for="(item, index) in urls">
      <Url @delete-url="$emit('delete-url', item.id)" :url="item" />
    </li>  
  </ul>
</template>

<script>
import axios from 'axios'
  import Url from './Url.vue'

  export default {
    name: 'Urls',
    props: {
      urls: Array,
    },
    components: {
      Url
    },
    emits: ['delete-url',],
    data () {
      return {
        newUrl: '',
        editUrl: '',
        config: {
          headers: {
            'Content-Type': 'application/json',
            'authorization': `Token ` + ''
          }
        }
      }
    },
    methods: {
      async getUrl (id) {
        const response = await axios.get(`http://localhost:8000/api/urls/${id}`, this.config)
        const data = await response.data
      },
      async submit() {
        const submitObj = {u_url: this.newUrl}
        // console.log(submitObj)
        const response = await axios.post('http://localhost:8000/api/urls/', submitObj, this.config)
        const data = await response.data
        this.urls.unshift(response.data)
        this.newUrl = ''
      },
      async submitEdit () {
        console.log('editing')
      }
    }
  }
</script>