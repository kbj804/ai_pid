<template>
  <div class="center">
    <md-table-toolbar>
        <h1 class="md-title">Inzent NB Competition Leader Board</h1>
        <md-button class="md-accent md-raised" @click.native="load_leader_board()">REFRESH</md-button>
      </md-table-toolbar>
    
    <md-table v-model="post.data" v-if="post" :md-sort.sync="currentSort" :md-sort-order.sync="currentSortOrder" :md-sort-fn="customSort" md-card>
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Rank" md-numeric>{{ item.id }}</md-table-cell>
        <md-table-cell md-label="팀이름" md-sort-by="name">{{ item.team_name }}</md-table-cell>
        <md-table-cell md-label="Score" md-sort-by="score">{{ item.score }}</md-table-cell>
      </md-table-row>
    </md-table>

  <!-- <md-table v-model="post.data" v-if="post" md-card md-fixed-header @md-selected="onSelect">
  <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" md-selectable="single"> -->
    <!-- <md-table-cell md-label="ID" md-sort-by="id" md-numeric>{{ item.id }}</md-table-cell> -->
    <!-- <md-table-cell md-label="TEAM NAME" md-sort-by="name">{{ item.name }}</md-table-cell>
    <md-table-cell md-label="ext" md-sort-by="ext">{{ item.ext }}</md-table-cell>
    <md-table-cell md-label="is_pid" md-sort-by="is_pid">{{ item.is_pid }}</md-table-cell>
  </md-table-row>
</md-table> -->
  
  <div>
    <md-field>
      <label> TEAM_NAME.csv File 제출</label>
      <md-file v-model="file.name" @md-change="onFileUpload($event)" />
      <md-button class="md-primary md-raised" @click.native="submit(file.name)">Verify File</md-button>
    </md-field>
  </div>

  </div>

  
</template>

<script>
import axios from "axios";

  export default {
    name: 'toyProjecrStaff',

    data () {
      return{
    currentSort: 'score',
      currentSortOrder: 'asc',
      post: null,

      file: {
          name:'Click to here'
          },
      }
    },
    

    methods: {
      startBgBlur(isStart) {
            this.$emit('startBgBlur', isStart);
        },

      onFileUpload (evt) {
          console.log(evt)
          this.file = evt[0]
          console.log("Upload File Info")
          console.log(this.file)
      },
      customSort (value) {
        return value.sort((a, b) => {
          const sortBy = this.currentSort

          if (this.currentSortOrder === 'desc') {
            return a[sortBy].localeCompare(b[sortBy])
          }

          return b[sortBy].localeCompare(a[sortBy])
        })
      },

      submit (name) {
          this.isSpinner = true
          const formData = new FormData();
          // this.filename = files[0].name
          formData.append("files", this.file);
            this.filename = this.file.name
            const url = "http://192.168.21.38:8001/api/toy/uploadFile";
            axios.post(url,
                formData, {
                  headers: {
                      "Content-Type": "multipart/form-data",
                      },
                  params:{
                      team: name
                    },
                
                }).then(response => {
                    this.iscontainer = false
                    this.isSpinner = false
                    this.post = response
                    console.log("RESPONSE");
                    console.log(response);

                }).catch((error) => {
                    this.isSpinner = false,
                    this.errorDialog = true,
                    // this.error = error.toString()
                    
                    this.error = error.response
                    console.log(error);
                })
      },

      load_leader_board() {

        this.post = null;
        this.startBgBlur(true);
        const url = "http://192.168.21.38:8001/api/toy/getLeaderBoard";
            axios.get(url,
            ).then(response => {
                      this.iscontainer = false
                      this.post = response
                      
                      setTimeout(() => {
                        this.startBgBlur(false);
                      }, 1000)

                      console.log("RESPONSE");
                      console.log(response);

                  }).catch((error) => {
                      this.errorDialog = true
                      this.error = error.toString()
                      console.log(error);
                      this.startBgBlur(false);
                  })

      },
    
    }

  }
</script>

<style lang="scss" scoped>
.md-app {
  max-width: 100%;
  max-height: 100%;
  border: 1px solid rgba(#000, .12);
}

.md-table + .md-table {
    margin-top: 16px
  }

.md-progress-spinner {
    margin: 24px;
  }

.center{
  margin: 0 auto;
}


</style>