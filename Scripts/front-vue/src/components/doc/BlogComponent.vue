<template>
  <div class="center">
    <md-table v-model="restaurants" md-card md-fixed-header>
      <md-table-toolbar>
          <h1 class="md-title">점심 뭐먹지?</h1>
      </md-table-toolbar>
      <md-table-row slot="md-table-row" slot-scope="{ item }" class="md-accent" >
        <md-table-cell style="width:50px;"  md-label="Name" md-sort-by="name">{{item.name}}</md-table-cell>
        <md-table-cell  md-label="Progress Bar" md-sort-by="pb"><md-progress-bar md-mode="buffer" :md-value="item.amount" :md-buffer="buffer"/></md-table-cell>
      </md-table-row>
    </md-table>
    <md-button class="md-raised" :md-ripple="false" @click="go">GO!</md-button>
  </div>
</template>

<script>
  import Vue from 'vue';

  export default {
    name: 'EmptyStateBasic',
    data() {
      return{
        buffer: 0,
        restaurants: [
          {
            id: 1,
            name: "오돈",
            amount: 0
          },
          {
            id: 2,
            name: "대문집",
            amount: 0
          }
        ],
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

            const timeoutId = setTimeout(num => {
              ++this.restaurants[num - 1].amount;

              if(!(100 >= this.restaurants[num - 1].amount)) {
                clearTimeout(timeoutId);
                return;
              }
            }, idx++ * 100, num)
        }
      },
    }
  }
</script>

<style lang="scss" scoped>
.md-progress-bar {
  margin: 24px;
}
</style>