<template>
  <div class="center">
    <md-table v-model="restaurants" md-card md-fixed-header @md-selected="onSelect">
      <md-table-toolbar>
          <h1 class="md-title">점심 뭐먹지?</h1>
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
    <md-button class="md-primary md-raised" @click="active = true">Add</md-button>

    <md-dialog-prompt
      :md-active.sync="active"
      v-model="value"
      md-title="식당 추가"
      md-input-maxlength="15"
      md-input-placeholder="식당 이름"
      md-confirm-text="추가"
      @md-confirm="addRestaurant"
      />

  </div>
</template>

<script>
  import Vue from 'vue';

  export default {
    name: 'ChoiceDisorder',
    data() {
      return{
        selected: [],
        buffer: 0,
        active: false,
        value: null,
        restaurants: [
          {
            name: "오돈",
            amount: 0
          },
          {
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
      getAlternateLabel (count) {
        let plural = ''

        if (count > 1) {
          plural = 's'
        }

        return `${count} resturants${plural} selected`
      },
      onSelect (item) {
        this.selected = item
      },

      addRestaurant() {
        this.restaurants.push({name: this.value, amount:0})
        this.value = null;
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

            const timeoutId = setTimeout(num => {
              ++this.restaurants[num - 1].amount;

              if(!(100 >= this.restaurants[num - 1].amount)) {
                clearTimeout(timeoutId);
                return;
              }
            }, idx++ * 100, num)
        }
      },
      deleter() {
        this.selected.forEach(ele => {
            const idx = this.restaurants.findIndex(element => element.name === ele.name)
            if (idx > -1) this.restaurants.splice(idx, 1)
        })
        // console.log(this.selected.forEach(elements => this.restaurants.filter(element => element.name !== elements.name)))
        // this.restaurants.splice(this.restaurants.indexOf("대문집"))
        // console.log(this.restaurants.filter(element => element.name !== '오돈'))
        // this.restaurants = this.selected.forEach(elements => this.restaurants.forEach(element => element !== elements.name))
        // this.restaurants = this.selected.filter(elements => this.restaurants.filter(element => element !== elements.name))

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