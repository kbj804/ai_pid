<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        icon
        v-on="on"
        @click="clickEvent()"
      >
        <i
          class="icon-down"
        />
      </v-btn>
    </template>

    <!-- <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title">
          {{ this.$store.state.userid }}
        </h2>
      </div>
      <div class="modal-footer">
        <button
          type="button"
          class="btn btn-primary"
          @click="logout"
        >
          로그아웃
        </button>
      </div>
    </div> -->


    <div
      id="hd-logout"
      class="modal-content"
    >
      <!-- <div class="modal-header">
        <p class="font-weight-bold">
          {{ this.$store.state.userid }}
        </p>
      </div> -->
      <div class="modal-footer">
        <button
          class="btn"
          @click="logout"
        >
          <span class="hide">로그아웃</span>
        </button>
      </div>
    </div>

    <!-- //logout -->
    <!-- <div
      id="hd-logout"
      class="hd-logout"
    >
      <p class="font-weight-bold">
        {{ this.$store.state.userid }}
      </p>
      <a
        href=""
        class="btn"
      ><span class="hide">로그아웃</span></a>
    </div> -->
  </v-menu>
</template>

<script>
export default {
  name: 'Modal',
  methods: {
    onClose () {
      this.$emit('close')
    },
    logout () {
      // 로컬스토리지 token 삭제, store 초기화
      // localStorage.removeItem('token')
      // this.$store.commit('SET_TOKEN', '')
      // this.$store.commit('SET_USERNAME', '')
      // this.$store.commit('SET_USERID', '')
      // this.$store.commit('SET_USERTYPE', '')
      // this.$store.commit('SET_COMPANY', '')
      // this.$store.commit('SET_SOLUTION', '')
      // this.$store.commit('SET_DEPT', '')
      // this.$store.commit('SET_EXP', '')
      // this.$router.push('/login')
    },
    clickEvent () {
      console.log('click event')
    }
  }
}
</script>

<style scoped>
#hd-logout .btn >>> {
  background-color: #ed3137; border: none; color: #fff; padding: .3rem 2.5rem;
}
</style>
