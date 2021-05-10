<template>
  <header id="hd">
    <div class="hd-brand">
      <h1 class="logo text-hide">
        <a href="javascript:void(0);" 
          @click="goto('/')">
          <img
            src="@/assets/img/ai-logo2.png"
            alt="INZENT"
            height="90"
            width="117"
          >
          </a>
      </h1>
      <button
        type="button"
        class="menu-toggler d-none d-lg-block"
      >
        <i class="icon-hamburger-back" />
      </button>
      <button
        type="button"
        class="menu-toggler d-lg-none"
      >
        <i class="icon-hamburger-back" />
      </button>
    </div>
    <ul class="breadcrumb">
      <li class="breadcrumb-item">
        AI
      </li>
      <template v-if="this.$store.state.depth2 === ' '">
        <li class="breadcrumb-item active">
          {{ depth1 }}
        </li>
      </template>

      <template v-else>
        <li class="breadcrumb-item">
          {{ depth1 }}
        </li>
        <li
          class="breadcrumb-item active"
          aria-current="page"
        >
          {{ depth2 }}
        </li>
      </template>
    </ul>
    <div class="hd-side">
      <a
        href=""
        class="icon-info"
        title="정보"
      />
      <!-- <span class="text-dark small">지식 포인트 {{ this.total_point }} </span>
      
      <a
        href="/profile"
        class="icon-profile"
        title="마이페이지"
      /> -->
      <span
        class="text-dark small"
      > {{ this.$store.state.username }}</span>
      <!-- <Modal /> -->
    </div>
  </header>
</template>

<script>
// import Modal from '@/components/log/KALOGPOP1.vue'
// import { selectTotalPoint } from '@/api/prm/Profile.js'
import { mapState } from 'vuex'

export default {
  components: {
    // Modal
  },
  data: () => {
    return {
      total_point: '',
      // depth1: '',
      // depth2: '',
      fullPath: '',
      depth: []
    }
  },
  methods: {
      goto(url) {
        this.$router.push(url);
      },
  },
  // 회원 total 포인트 조회
//   async created () {
//     const userId = {
//       user_id: this.$store.state.userid,
//       month: '' // ##나중에 수정해주어야함##
//     }
//     console.log(userId)
//     const { data } = await selectTotalPoint(userId)
//     // console.log('data', data)
//     this.total_point = data.total_point
//     // console.log('this.total_point', this.total_point)
//   },
  computed: {
    ...mapState({
      depth1: 'depth1',
      depth2: 'depth2'
    })
  },
  mounted () {
  }
}
</script>

<style>

</style>
