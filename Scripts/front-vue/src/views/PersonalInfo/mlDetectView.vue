<template>
  <div id ="warp">
    <div v-if="isBlurTest" style="position: absolute; width: calc(100% - 237px); left: calc(50% + 54px); top: calc(50% - 54px); z-index:999999">
        <md-progress-spinner class="md-accent" md-mode="indeterminate"></md-progress-spinner>
    </div>
    <div id="ct" :class="{blurTest: isBlurTest}">
        <MLDetectComp @startBgBlur="startBgBlurTest"/>
    </div>
  </div>
</template>

<script>
// import KADSB0101Form from '@/components/dsb/KADSB0101Form.vue'
import MLDetectComp from '@/components/pi/PiMLComponent.vue'
// import { expToken } from '@/api/log/Login.js'

export default {
  name: 'Load_ML_Model_View',
  components: {
    MLDetectComp
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
    this.$store.commit('SET_DEPTH2', 'Machine Learning Detection')
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
