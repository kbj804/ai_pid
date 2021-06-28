<template>
<div id='ct'>
  <div class="home">
    <staffComp/>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import staffComp from '@/components/toyProject/staffComponent.vue'

export default {
  name: 'staffView',
  components: {
    staffComp
  },
    data () {
    return {

    }
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'toyProject')
    this.$store.commit('SET_DEPTH2', 'staff DB')
  }
}
</script>



