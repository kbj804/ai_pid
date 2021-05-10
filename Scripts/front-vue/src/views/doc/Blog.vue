<template>
  <div id="ct">
    <section class="card">
      <!-- <KADSB0101Form /> -->
      <BlogComponent />
    </section>
  </div>
</template>

<script>
// import KADSB0101Form from '@/components/dsb/KADSB0101Form.vue'
import BlogComponent from '@/components/doc/BlogComponent.vue'
// import { expToken } from '@/api/log/Login.js'

export default {
  components: {
    // KADSB0101Form
    BlogComponent
  },
  data () {
    return {

    }
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'Document')
    this.$store.commit('SET_DEPTH2', 'Blog')
  }
}
</script>

<style>

</style>
