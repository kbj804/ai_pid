<template>
  <div id="ct">
    <section class="card">
      <UploadFilesComp />
    </section>
  </div>
</template>

<script>
// import KADSB0101Form from '@/components/dsb/KADSB0101Form.vue'
import UploadFilesComp from '@/components/pi/UploadFiles.vue'
// import { expToken } from '@/api/log/Login.js'

export default {
  components: {
    UploadFilesComp
  },
  data () {
    return {

    }
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'Personal Information Detection')
    this.$store.commit('SET_DEPTH2', 'Upload Files')
  }
}
</script>

<style>

</style>
