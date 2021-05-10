<template>
  <div id="ct">
    <button @click="checklist">조회하기</button>
    <table>
      <thead>
        <tr>
          <td>글 번호</td>
          <td>제목</td>
          <td>사용자</td>
          <td>조회수</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(d, index) in data" :key="index">
          <td>{{ d.id }}</td>
          <td>{{ d.title }}</td>
          <td>{{ d.user }}</td>
          <td>{{ d.hit }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "ct",
  data() {
    return {
      data: [
        { id: 0, title: "안녕하세요.", user: "새내기", hit: 10 },
        { id: 1, title: "여기는 어디?", user: "누군가", hit: 5 },
        { id: 2, title: "야호 신난다", user: "홍길동", hit: 15 },
        { id: 3, title: "테스트합니다.", user: "관리자", hit: 7 }
      ]
    };
  },
  created () {
    // const exp = this.$store.state.exp
    // expToken(exp)

    this.$store.commit('SET_DEPTH1', 'Document')
    this.$store.commit('SET_DEPTH2', 'Test')
  },
  methods: {
    checklist: function() {
      const self = this;
      axios.get("http://localhost:8000/vuetest")
        .then(function (res) {
        self.data = []
        for(let i of res.data) {
          self.data.push({
            id: i.pk,
            title: i.fields.title,
            user: i.fields.user,
            hit: 0, // not implemented.
          })
        }
      })
      .catch(function(err) {
        alert(err);
      });
    }
  }
};
</script>