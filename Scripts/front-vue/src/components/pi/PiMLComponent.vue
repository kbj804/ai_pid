<template>
  <div class="center">
    

    <md-chip class="md-accent" md-clickable>전화번호</md-chip>
    <md-chip class="md-accent" md-clickable>휴대폰</md-chip>
    <md-chip class="md-accent" md-clickable>이메일</md-chip>
    <md-chip class="md-accent" md-clickable>주민등록번호</md-chip>
    <md-chip class="md-accent" md-clickable>계좌번호</md-chip>
    <md-chip class="md-accent" md-clickable>IP주소</md-chip>
    <md-chip class="md-accent" md-clickable>MAC주소</md-chip>
    <md-chip class="md-accent" md-clickable>여권번호</md-chip>
    <md-chip class="md-accent" md-clickable>운전면허</md-chip>
    <md-chip class="md-accent" md-clickable>건강보험</md-chip>
    <md-chip class="md-accent" md-clickable>파일형식(이미지,오디오,문서)</md-chip>
    <md-chip md-disabled>은행계좌</md-chip>

    <md-empty-state v-if="iscontainer" style="padding: 10px;"
      class="md-primary"
      md-rounded
      md-icon="done"
      md-label="Load Machine Learning Model"
      md-description="ML Model을 로드하고 테스트 해볼 수 있습니다.">
      <md-input-container>
        <md-field>
          <!-- <label>Load</label> -->
          <!-- <md-file v-model="file.name" @md-change="onFileUpload($event)" /> -->
           <md-button class="md-accent md-raised" @click.native="load_ml_model()">LOAD MODEL</md-button>
        </md-field>
      </md-input-container>
    </md-empty-state>
    <md-field v-else>
          <!-- <label>Only PDF Files</label> -->
          <!-- <md-file v-model="file.name" @md-change="onFileUpload($event)" /> -->
          <md-button class="md-accent md-raised" @click.native="load_ml_model()">LOAD MODEL</md-button>
          <md-button class="md-primary md-raised" v-if="selected" @click="showDialog = true, loadTrain(selected.id)">Show Dialog</md-button>
    </md-field>

<md-table v-model="post.data" v-if="post" md-card md-fixed-header @md-selected="onSelect">
  <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" md-selectable="single">
    <md-table-cell md-label="ID" md-sort-by="id" md-numeric>{{ item.id }}</md-table-cell>
    <md-table-cell md-label="Name" md-sort-by="name">{{ item.name }}</md-table-cell>
    <md-table-cell md-label="ext" md-sort-by="ext">{{ item.ext }}</md-table-cell>
    <md-table-cell md-label="is_pid" md-sort-by="is_pid">{{ item.is_pid }}</md-table-cell>
  </md-table-row>
</md-table>



<div>
    <md-dialog :md-active.sync="showDialog" v-if="trainData">
      <md-dialog-title>{{ selected.name }}.{{selected.ext}}</md-dialog-title>

      <md-tabs md-dynamic-height>
        <md-tab md-label="Information">
          <md-table v-model="trainData.data" md-sort="page" md-sort-order="asc" md-card md-fixed-header >
              <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" md-selectable="single">
              <md-table-cell md-label="Page" md-sort-by="page" md-numeric>{{ item.page }}</md-table-cell>
              <md-table-cell md-label="Reg-Count" md-sort-by="reg_count" md-numeric>{{ item.reg_count }}</md-table-cell>
              
              <md-table-cell md-label="column1" md-sort-by="column1">{{ item.column1 }}</md-table-cell>
              <md-table-cell md-label="column2" md-sort-by="column2">{{ item.column2 }}</md-table-cell>
              <md-table-cell md-label="column3" md-sort-by="column3">{{ item.column3 }}</md-table-cell>
              <md-table-cell md-label="column4" md-sort-by="column4">{{ item.column4 }}</md-table-cell>
              <md-table-cell md-label="column5" md-sort-by="column5">{{ item.column5 }}</md-table-cell>
              <md-table-cell md-label="column6" md-sort-by="column6">{{ item.column6 }}</md-table-cell>
              <md-table-cell md-label="column7" md-sort-by="column7">{{ item.column7 }}</md-table-cell>
              <md-table-cell md-label="column8" md-sort-by="column8">{{ item.column8 }}</md-table-cell>
              <md-table-cell md-label="column9" md-sort-by="column9">{{ item.column9 }}</md-table-cell>
              <md-table-cell md-label="column10" md-sort-by="column10">{{ item.column10 }}</md-table-cell>
            </md-table-row>

          </md-table>
        </md-tab>

        <md-tab md-label="summary" >
          <span class="md-subheading">Sum Reg_count : {{summary.reg_count}}</span>
          <p/>
          <span class="md-subheading">Sum column   : {{summary.col}}</span>
        </md-tab>

        <md-tab md-label="Text">
          <md-steppers md-vertical style="overflow-y: auto; height: 300px;">
            
            <md-step v-for="td in trainData.data" v-bind:key="td.page" md-label="Page">
              <p>{{td.text_data}}</p>
            </md-step>

          </md-steppers>
        </md-tab>
        
      </md-tabs>

      <md-dialog-actions>
        <md-button class="md-primary" @click="predictFile(selected.id)">PREDICT</md-button>
        <md-button class="md-primary" @click="showDialog=false">Close</md-button>
      </md-dialog-actions>
    </md-dialog>

    
  </div>

<md-dialog-alert :md-active.sync="errorDialog" v-if="error"
                md-title="ERROR!"
                :md-content="error"
                >
</md-dialog-alert>

<md-dialog-alert :md-active.sync="predictDialog" v-if="predictValue"
                md-title="Predict Page Result"
                :md-content="predictValue.data"
                >
</md-dialog-alert>


<!-- <div v-if="error" class="error">
      {{ error }}
</div> -->

  </div>
</template>

<script>
import axios from "axios";``

  export default {
    name: 'EmptyStateBasic',

    data () {
      return{
        // mdContent: 'md-content',
        boolean:false,
        // DIALOG
        showDialog: false,
        errorDialog: false,
        predictDialog: false,

        iscontainer: true,
        selected: null,

        trainData: null,

        post: null,
        error:null,
        predictValue: null,

        filename:null,
        
        summary: {
          reg_count:0,
          col1:0, col2:0, col3:0, col4:0, col5:0, col6:0, col7:0, col8:0, col9:0, col10:0,
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
          console.log("zdasdadddsad")
          console.log(this.file)
      },
      load_ml_model() {

        this.post = null;
        this.startBgBlur(true);
        const url = "http://192.168.21.38:8001/api/ml/getLoadML";
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

      onSelect (item) {
            this.selected = item
      },

      loadTrain(idValue) {
            const url = "http://192.168.21.38:8001/api/pid/getTrain";
            axios.get(url,
                  {
                    params:{
                      id: idValue
                    }
                  }
                  ).then(response => {
                      this.trainData = response
                      this.regexSum()
                      console.log("RESPONSE");
                      console.log(response);
                  }).catch((error) => {
                      this.error = error.toString()
                      console.log(error);
                  })
          },
          regexSum(){
          this.summary.reg_count = 0;
          this.summary.col = 0;
          for(let i=0; i < this.trainData.data.length; i++){
            this.summary.reg_count += this.trainData.data[i].reg_count
            this.summary.col += this.trainData.data[i].column1
            this.summary.col += this.trainData.data[i].column2
            this.summary.col += this.trainData.data[i].column3
            this.summary.col += this.trainData.data[i].column4
            this.summary.col += this.trainData.data[i].column5
            this.summary.col += this.trainData.data[i].column6
            this.summary.col += this.trainData.data[i].column7
            this.summary.col += this.trainData.data[i].column8
            this.summary.col += this.trainData.data[i].column9
            this.summary.col += this.trainData.data[i].column10
          }
        },
        predictFile(idValue){
          this.startBgBlur(true);
          const url = "http://192.168.21.38:8001/api/ml/getPredictFile";
          axios.get(url,
                {
                  params:{
                    file_id: idValue
                  }
                }
                ).then(response => {
                    this.predictDialog = true
                    this.predictValue = response
                    setTimeout(() => {
                        this.startBgBlur(false);
                      }, 1000)
                    console.log("RESPONSE");
                    console.log(response);
                }).catch((error) => {
                    this.errorDialog = true
                    this.error = error.toString()
                    this.startBgBlur(false);
                    console.log(error);
                })
        },

    }


  }
</script>

<style lang="scss" scoped>



</style>