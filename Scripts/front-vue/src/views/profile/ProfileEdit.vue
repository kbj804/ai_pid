<!-- 프로필 편집 -->
<template>
  <div id="ct">
    <section class="card">
      <header class="card-header">
        <h2 class="card-title">
          <span class="i-rounded bg-danger"><i class="icon-user" /></span>프로필편집
        </h2>
        <h2 class="card-title text-tertiary text-pad">
          |
        </h2>
        <a href="/point">
          <h2 class="card-title text-tertiary">
            지식포인트
          </h2>
        </a>
        <div class="btn-container">
          <a
            class="btn btn-m"
            @click="() => {this.$router.go(-1)}"
          ><span class="hide">취소</span></a>
          <a
            class="btn btn-primary"
            @click="submitForm"
          ><span
            class="hide"
            style="color:white;"
          >확인</span></a>
        </div>
      </header>
      <!-- 이미지 -->
      <div class="card-body card-img">
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
              <td>
                <div class="form-group">
                  <input
                    v-model="dept"
                    type="text"
                    class="form-control"
                    placeholder="부서명을 입력하세요."
                  >
                </div>
              </td>
            </tr>
            <tr>
              <td class="alert-text">
                담당솔루션
              </td>
              <td>
                <select
                  v-model="solution"
                  class="form-control"
                  title="선택하세요"
                  @change="selectSolution"
                >
                  <option
                    v-for="(item,index) in items"
                    :key="index"
                    :value="item.codeId"
                  >
                    {{ item.codeContent }}
                  </option>
                </select>
                <!--
                <v-select
                  v-model="solution"
                  class="form-control compact-form"
                  :items="items"
                  dense
                  solo
                  item-text="codeContent"
                  item-value="codeId"
                  @change="selectSolution"
                /> -->
              </td>
            </tr>
            <tr>
              <td class="alert-text">
                권한
              </td>
              <td>
                <select
                  v-model="user_type"
                  class="form-control"
                  title="선택하세요"
                  @change="selectType"
                >
                  <option
                    v-for="(item,index) in items2"
                    :key="index"
                    :value="item.code"
                  >
                    {{ item.name }}
                  </option>
                </select>
                <!-- <v-select
                  v-model="user_type"
                  class="form-control compact-form"
                  :items="items2"
                  dense
                  solo
                  item-text="name"
                  item-value="code"
                  @change="selectType"
                /> -->
              </td>
            </tr>
            <tr>
              <td class="alert-text">
                프로필 사진
              </td>
              <td>
                <div class="filebox">
                  <label
                    class="btn btn-m"
                    for="ex_file"
                  >업로드</label>
                  <v-file-input
                    id="ex_file"
                    v-model="image"
                    hide-input
                    type="file"
                    accept="image/*"
                    @change="onUpload"
                  />
                </div>
              </td>
            </tr>

            <tr>
              <td class="alert-text">
                비밀번호
              </td>
              <td>
                <a
                  class="btn mr-2 mb-2"
                  data-toggle="modal"
                  @click.prevent="addBoard"
                ><span class="hide">변경</span></a>
              </td>
            </tr>
          </tbody>
        </table>
        <Modal
          :dialog="isAddBoard"
          @close="isAddBoard=false"
        />
        <Alert
          :dialog="completeAlert"
          :send-data="alertContent"
          @close="completeAlert=false"
        />
      </div>
    </section>
  </div>
</template>

<script>
import { userType, userSolution, getSolution, expToken } from '@/api/log/Login.js'
import { updateProfile, selectProfile } from '@/api/prm/Profile.js'
import { formData } from '@/api/log/Signup.js'
import Modal from '@/components/prm/KAPRM0103.vue' // 1. 비밀번호 변경 모달
import Alert from '@/components/common/CompletePOP.vue' // 완료 alert

export default {
  components: {
    Modal,
    Alert
  },
  data: () => {
    return {
      alertContent: '',
      showNoImage: false,
      isAddBoard: false,
      completeAlert: false,
      imgSrc: '',
      image: null,
      code: '',
      typeCode: '',
      alert: false,
      dept: '',
      user_type: '',
      solution: '',
      items: [],
      items2: [
        {
          name: '답변자',
          code: 'A'
        },
        {
          name: '질문자',
          code: 'Q'
        }
      ]
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
    }
  },
  async mounted () {
    console.log('mounted')
    const userdata = {
      user_id: this.$store.state.userid
    }
    const { data } = await selectProfile(userdata)
    if (data === '') {
      this.showNoImage = true
    } else {
      this.imgSrc = data
    }
  },
  async created () {
    const exp = this.$store.state.exp
    expToken(exp)
    this.$store.commit('SET_DEPTH1', '프로필관리')
    this.$store.commit('SET_DEPTH2', '프로필편집')

    const { data } = await getSolution() // 솔루션 목록 가져오기

    console.log('data: ', data)
    this.items = data
    this.userType()
    console.log('유저타입', this.user_type)

    this.code = this.$store.state.solution // 솔루션 코드 저장
    console.log('code는?' + this.code)

    this.solution = userSolution(this.code)
    console.log('솔루션명은?' + this.solution) // 솔루션 명 저장

    this.dept = this.$store.state.dept
    console.log('this.items', this.items)

    this.solution = this.code
    console.log('this.solution', this.solution)
  },
  methods: {
    selectSolution () {
      this.code = this.solution // 변경됐을 때 solution code
    },
    selectType () {
      this.typeCode = this.user_type // 변경됐을 때 user_type code
    },
    userType () {
      this.typeCode = this.$store.state.usertype
      this.user_type = userType(this.typeCode)
      console.log('this.typeCode', this.typeCode)
      console.log('this.user_type', this.user_type)
      this.user_type = this.typeCode
    },
    addBoard () {
      this.isAddBoard = true
      console.log(this.isAddBoard)
    },
    submitForm () { // 회원 정보 수정
      console.log('submitForm 실행')

      const userData = {
        dept: this.dept,
        solution: this.code,
        user_type: this.typeCode,
        user_id: this.user_id
      }

      console.log('여기서 솔루션?', this.solution)
      console.log('userData', userData)
      updateProfile(userData)
        .then((res) => {
          if (res.status === 200) {
            console.log('status200 맞나요?' + res.status)
            console.log('this.code모지??' + this.code)

            // 회원 정보 수정 됐을 때 vue에 있는 data도 변경되어야함..
            this.$store.commit('SET_DEPT', userData.dept)
            this.$store.commit('SET_SOLUTION', this.code)
            this.$store.commit('SET_USERTYPE', this.typeCode)
            console.log('유저타입' + this.typeCode)

            this.alertContent = '정보가 수정되었습니다'
            this.completeAlert = true
          }
        }
        )
    },
    async onUpload () {
      try {
        var fd = new FormData()
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'] // 이미지 파일만 업로드
        if (!allowedTypes.includes(this.image.type)) {
          this.alert = true // 이미지 파일이 아닐 경우 alert 창 띄움
        } else {
          this.alert = false
          console.log('이미지파일 맞음')
          console.log(this.image.type === 'image/*')
          fd.append('profile_image', this.image)
          fd.append('user_id', this.user_id)
          const { data } = await formData(fd)
          console.log('???', data)
          this.imgSrc = data
          this.showNoImage = false
        }
      } catch (error) {
      }
    },
    noImage () {
      return this.showNoImage
    }
  }
}
</script>

<style>
.form-group{position: relative}
.form-group i{position: absolute; right: 9px; top: 9px;}
.form-group img{ width: 1.2rem; position: absolute; right: 7px; top: 7px}

.filebox v-file-input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.theme--light.v-file-input{
  display: none;
}
</style>
