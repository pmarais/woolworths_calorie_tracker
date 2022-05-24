<template>
  <header class="text-center bg-blue-800 text-white p-4 mb-10">
    <div class="text-3xl font-bold mb-3"> <i class="fa fa-viruses"></i> Trello Bookmarks</div>
  </header>
  <div>
    <Urls @delete-url="deleteUrl" :urls="urls"/>
  </div>
</template>

<script>
import Urls from './components/Urls.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Urls,
  },
  data () {
    return {
      urls: [],
      config: {
        headers: {
          'Content-Type': 'application/json',
          'authorization': `Token ` + ''
        }
      }
    }
  },
  created () {
    axios.get('http://localhost:8000/api/urls/', this.config).then(response => {
      this.urls = response.data
      // console.log(response.data)
      // console.log(this.urls)
    })
  },
  methods: {
    deleteUrl (id) {
      console.log('delete-url', id)
      axios.delete(`http://localhost:8000/api/urls/${id}/`, this.config).then(response => {
        this.urls = this.urls.filter((url) => url.id !== id) // keep verything that isn't the deleted item
      })
    }
  },
  mounted () {
    // console.log(this.urls)
  }
}
</script>


const config = {
          headers: { 'authorization': `Token ` + response.data.token},
        }