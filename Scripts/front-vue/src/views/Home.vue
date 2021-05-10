<template>
<div id='ct'>
  <div class="home">
    <!-- <img alt="Vue logo" src="@/assets/logo.png"> -->
    <HelloWorld msg="Welcome to AIZT App"/>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
    data () {
    return {

    }
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'HOME')
    this.$store.commit('SET_DEPTH2', ' ')
  }
}
</script>



