<template>
  <div id="wrap">

    <div v-if="isBlurTest" style="position: absolute; width: calc(100% - 237px); left: calc(50% + 54px); top: calc(50% - 54px); z-index:999999">
        <md-progress-spinner class="md-accent" md-mode="indeterminate"></md-progress-spinner>
    </div>

    <div id="ct" :class="{blurTest: isBlurTest}">
      <!-- <section class="card"> -->
          
        <PIDForm @startBgBlur="startBgBlurTest" />
      <!-- </section> -->
    </div>
  </div>
</template>

<script>
import PIDForm from '@/components/pi/PiFilesComponent.vue'
// import { expToken } from '@/api/log/Login.js'

export default {
    name: 'PID_view',
    components: {
    PIDForm
  },
  data () {
    return {
      name:"leffept",
      isBlurTest: false,
    }
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'Personal Information Detection')
    this.$store.commit('SET_DEPTH2', 'Load Files')
  },
  methods: {
    startBgBlurTest(isBlurTest) {
      this.isBlurTest = isBlurTest;
      // this.isSpinner = isBlurTest
    }
  }
}
</script>

<style>
.blurTest {
  background-color: gray;
  opacity: 0.3;
}
</style>