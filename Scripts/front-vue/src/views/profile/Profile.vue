<template>
  <div id="ct">
    <section class="card">
      <header class="card-header">
        <h2 class="card-title">
          <span class="i-rounded bg-danger"><i class="icon-user" /></span>프로필관리
        </h2>
        <h2 class="card-title text-tertiary text-pad">
          |
        </h2>
        <a href="/point">
          <h2
            class="card-title text-tertiary"
          >
            지식포인트
          </h2>
        </a>
        <div class="btn-container">
          <a
            class="btn btn-m"
            @click="updateProfile"
          ><span class="hide">편집</span></a>
        </div>
      </header>
      <div class="card-body card-img">
        <!-- DB에 프로필 이미지 없을 때 v-if -->
        <div
          v-if="noImage()"
          class="profile_management_sample"
        >
          <i
            class="icon-pic"
          />
          <span class="text-secondary">No image loaded</span>
        </div>
        <!-- DB에 프로필 이미지 있을 때 v-else -->
        <v-img
          v-else
          :src="get_img_src"
        />
      </div>
      <div
        class="table-responsive"
        style="width: 30rem"
      >
        <table class="table">
          <colgroup>
            <col style="width: 30%">
            <col style="width: 70%">
          </colgroup>
          <tbody>
            <tr>
              <td class="alert-text">
                이름
              </td>
              <td>{{ user_name }}</td>
            </tr>
            <tr>
              <td class="alert-text">
                이메일
              </td>
              <td>{{ user_id }}</td>
            </tr>
            <tr>
              <td class="alert-text">
                소속회사
              </td>
              <td>{{ company }}</td>
            </tr>
            <tr>
              <td class="alert-text">
                부서
              </td>
              <td>{{ dept }}</td>
            </tr>
            <tr>
              <td class="alert-text">
                담당솔루션
              </td>
              <td>{{ solution }}</td>
            </tr>
            <tr>
              <td class="alert-text">
                권한
              </td>
              <td>{{ usertype }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
// import { userType, userSolution, expToken } from '@/api/log/Login.js'
// import { formData } from '@/api/log/Signup.js'
// import { selectProfile } from '@/api/prm/Profile.js'

export default {
  data: () => {
    return {
      showNoImage: false,
      usertype: '',
      solution: '',
      imageBytes: '',
      selectedFile: null,
      uploadData: '',
      imgSrc: '',
      image: null,
      rules: [
        value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!' + value.type
      ],
      alert: false
    }
  },
  computed: {
    get_img_src () {
      return 'data:image;base64,' + this.imgSrc
    },
    user_name: function () {
      return this.$store.state.username
    },
    user_id: function () {
      return this.$store.state.userid
    },
    company: function () {
      return this.$store.state.company
    },
    dept: function () {
      return this.$store.state.dept
    }
  },
  mounted () {
  },
  async created () {
    const exp = this.$store.state.exp
    expToken(exp)

    this.$store.commit('SET_DEPTH1', '프로필관리')
    this.$store.commit('SET_DEPTH2', '프로필관리')

    this.userType()
    this.userSolution()

//     const userdata = {
//       user_id: this.$store.state.userid
//     }
//     console.log(userdata)
//     const { data } = await selectProfile(userdata)
//     console.log('data 트루야 펄스야?', data === '')
//     if (data === '') {
//       this.showNoImage = true
//       console.log('data 트루야 펄스야?', data === '')
//     } else {
//       this.imgSrc = data
//     }
  },
  methods: {
    // async onUpload () {
    //   try {
    //     var fd = new FormData()
    //     const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'] // 이미지 파일만 업로드
    //     if (!allowedTypes.includes(this.image.type)) {
    //       this.alert = true // 이미지 파일이 아닐 경우 alert 창 띄움
    //     } else {
    //       this.alert = false
    //       console.log('이미지파일 맞음')
    //       console.log(this.image.type === 'image/*')
    //       fd.append('profile_image', this.image)
    //       fd.append('user_id', this.user_id)
    //       const { data } = await formData(fd)
    //       this.imgSrc = data
    //     }
    //   } catch (error) {
    //   } finally {

    //   }
    },
    userType () {
    //   const type = this.$store.state.usertype
    //   this.usertype = userType(type)
    },
    userSolution () {
    //   const code = this.$store.state.solution
    //   console.log('code뭐가 있지?', code)
    //   this.solution = userSolution(code)
    //   console.log('solution뭐가 있지?', this.solution)
    },

    updateProfile () {
      this.$router.push('/profileUpdate') // 프로필 수정화면으로 이동
    },
    pointPage () {
      this.$router.push('/point') // 포인트 화면으로 이동
    },

    noImage () {
      return this.showNoImage
    }

  }
}
</script>

<style>

</style>
