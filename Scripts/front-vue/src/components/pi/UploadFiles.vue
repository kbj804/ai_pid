<template>
  <div class="center">
    <md-empty-state v-if="iscontainer"
      md-icon="devices_other"
      md-label="Upload Test Files"
      md-description="Uploading files, you'll be able to show your file's contents and verify to Personal Information.">
      <md-input-container>
        <md-field>
          <label>지원하는 확장자 하단 참조</label>
          <md-file v-model="file.name" @md-change="onFileUpload($event)" />
           <md-button class="md-primary md-raised" @click.native="submit()">Verify File</md-button>
        </md-field>
      </md-input-container>
    </md-empty-state>
    <md-field v-else>
          <label>지원하는 확장자 하단 참조</label>
          <md-file v-model="file.name" @md-change="onFileUpload($event)" />
           <md-button class="md-primary md-raised" @click.native="submit()">Verify File</md-button>
        </md-field>
  
    <div v-if="isSpinner">
      <!-- <md-progress-spinner md-mode="indeterminate"></md-progress-spinner> -->
      <md-progress-spinner class="md-accent" md-mode="indeterminate"></md-progress-spinner>
    </div>

    <md-table v-model="post.data" v-if="post" md-card md-fixed-header @md-selected="onSelect">
      <md-table-toolbar>
        <h1 class="md-title">{{filename}}</h1>
      </md-table-toolbar>

      <!-- <md-table-row slot="md-table-row" slot-scope="{ item }" :class="getClass(item)" md-selectable="single"> -->
        <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" md-selectable="single">
        <md-table-cell md-label="Page" md-sort-by="page" md-numeric>{{ item.page+1 }}</md-table-cell>
        <md-table-cell md-label="TextData" md-sort-by="textdata">{{ item.td }}</md-table-cell>
      </md-table-row>


    </md-table>

    <div style="padding: 20px; left: 48%; position: fixed;">
      <md-chip v-for="reg in regList" :key="reg" class="md-primary" md-clickable>{{reg}}</md-chip>

      <md-chip md-disabled>docx
        <md-tooltip md-direction="bottom">추후 지원</md-tooltip>
      </md-chip>
    </div>



    <md-dialog-alert :md-active.sync="errorDialog" v-if="error"
                    md-title="ERROR!"
                    :md-content="(error.data.msg ? error.data.msg : error.statusText)"
                    >
    </md-dialog-alert>

  </div>
</template>

<script>
import axios from "axios";

  export default {
    name: 'EmptyStateBasic',

    data () {
      return{
        boolean:false,
        isSpinner: false,
        errorDialog: false,
        file: {
          name:'Click to here'
          },
        files:[],
        post: null,
        error:null,
        filename:null,
        iscontainer: true,
        selected: {},

        regList:[
          "pdf", "txt","csv","xlsx", "pptx"
        ]

      }
    },

    methods: {
      onFileUpload (evt) {
          console.log(evt)
          this.file = evt[0]
          console.log("Upload File Info")
          console.log(this.file)
      },

      submit () {
          this.isSpinner = true
          const formData = new FormData();
          // this.filename = files[0].name
          formData.append("files", this.file);
            this.filename = this.file.name
            const url = "http://192.168.21.38:8001/api/pid/uploadfiles";
            axios.post(url, 
                formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
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
      onSelect (item) {
            this.selected = item
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