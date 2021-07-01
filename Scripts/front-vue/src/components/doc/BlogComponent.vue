<template>
  <div class="center">
    <md-table v-model="restaurants" md-card md-fixed-header @md-selected="onSelect">
      <md-table-toolbar>
          <h1 class="md-title">Lunch Selector</h1>
      </md-table-toolbar>

      <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
        <div class="md-toolbar-section-start">{{ getAlternateLabel(count) }}</div>

        <div class="md-toolbar-section-end">
          <md-button class="md-icon-button" @click="deleter">
            <md-icon>delete</md-icon>
          </md-button>
        </div>
      </md-table-toolbar>


      <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" md-selectable="multiple" md-auto-select>
        <md-table-cell style="width:50px;"  md-label="Name" md-sort-by="name">{{item.name}}</md-table-cell>
        <md-table-cell  md-label="Progress Bar" md-sort-by="pb"><md-progress-bar class="md-accent" md-mode="buffer" :md-value="item.amount" :md-buffer="buffer"/></md-table-cell>
      </md-table-row>
    </md-table>
    <md-button class="md-raised" :md-ripple="false" @click="go">GO!</md-button>
    <md-button class="md-raised md-accent" @click="refresh">REFRESH!</md-button>
    <md-button class="md-accent" style="float: right" > WINNER: {{winner}} </md-button>
    
    <md-dialog-alert
      :md-active.sync="flag"
      md-title="★ WINNER ★"
      :md-content="winner" />

    <!-- <md-button class="md-primary md-raised" @click="active = true">Add</md-button>

    <md-dialog-prompt
      :md-active.sync="active"
      v-model="value"
      md-title="Restaurant ADD"
      md-input-maxlength="15"
      md-input-placeholder="Restaurant Name"
      md-confirm-text="ADD"
      @md-confirm="addRestaurant"
    /> -->

    <md-chips class="md-accent" v-model="rname" md-placeholder="Add Here..." :md-auto-insert="true" @md-insert="addRestaurant2">
      <label>Add Name</label>
    </md-chips>
    <md-chip class="md-accent" v-for="chip in rstrChips" :key="chip" md-clickable @click="addChip(chip)">{{ chip }}</md-chip>

  </div>
</template>

<script>
  import Vue from 'vue';

  export default {
    name: 'ChoiceDisorder',
    data() {
      return{
        flag: false,
        stopflag:false,
        rname:[],
        selected: [],
        buffer: 0,
        active: false,
        value: null,
        restaurants: [
          {name: "sample", amount:0}
        ],
        rstrChips:['배꼽집', '대문집', '진주집', '중국집', '쌀국수', '고등어', '분식', '순대국', '오돈'],
        winner: null,
        lastTimeoutID: null,
      }
    },
    created() {
        Vue.nextTick(() => {
            let elementList = document.querySelectorAll('.md-table-head-label');
            
            elementList.forEach((element, idx) => {
                if(0 === idx)
                    element.style.width = "11px";
            });
        })
    },
    methods: {
      getAlternateLabel (count) {
        let plural = ''

        if (count > 1) {
          plural = 's'
        }

        return `${count} contents${plural} selected`
      },
      onSelect (item) {
        this.selected = item
      },

      // addRestaurant() {
      //   this.restaurants.push({name: this.value, amount:0})
      //   this.value = null;
      // },
      addRestaurant2(str){
        this.restaurants.push({name: str, amount:0})
        this.rname=[]
      },

      randomPick(num) {
        return Math.floor(Math.random() * ((num + 1) - 1) + 1);
      },
      go() {
        let idx = 1, 
            n = this.restaurants.length, 
            arr = Array.from({length: n}, () => 0);
          
        while(arr.every(element => element <= 100)) {
            const num = this.randomPick(n);
            ++arr[num - 1];
            let winnerIndex = arr.indexOf(Math.max(...arr));

            const timeoutId = setTimeout(obj => {
              // console.log(timeoutId)
              // if(this.stopflag) {
              //     console.log(1)
              //     this.restaurants[obj.num - 1].amount = 0;
              //     // this.stopflag = false;
              //     clearTimeout(timeoutId);
              //     return;
              // }
              if(!(100 > this.restaurants[obj.num - 1].amount)) {
                console.log(1)
                this.flag = true;
                clearTimeout(timeoutId);
                return;
              }
              ++this.restaurants[obj.num - 1].amount;
              console.log(this.restaurants[obj.num - 1].amount)
              this.winner = this.restaurants[obj.winnerIndex].name
            }, idx++ * 10, {num, winnerIndex})
        }
        
      },
      refresh() {
        let n = this.restaurants.length
        for(let i = 0; i < n ; i ++) this.restaurants[i].amount = 0;
        this.stopflag = true;
      },

      deleter() {
        this.selected.forEach(ele => {
            const idx = this.restaurants.findIndex(element => element.name === ele.name)
            if (idx > -1) this.restaurants.splice(idx, 1)
        })
      },
      addChip(str){
        this.restaurants.push({name: str, amount:0})
      },
      
    }
  }
</script>

<style lang="scss" scoped>
.md-progress-bar {
  margin: 24px;
}
.md-table + .md-table {
  margin-top: 16px
}
</style>