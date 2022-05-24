<template>
  <p class="text-left bg-blue-100 p-3 mb-1"> <!-- {{url.id}}: --> <a target="_blank" :href="url.u_url">{{url.u_url}}</a> <button class="inline-flex justify-center py-1 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 float-right" @click="$emit('delete-url', url.id)">Delete</button></p>
</template>

<script>
  export default {
    name: "Url",
    props: {
      url: Object,
    },
    emits: ['delete-url',]
  }
</script>