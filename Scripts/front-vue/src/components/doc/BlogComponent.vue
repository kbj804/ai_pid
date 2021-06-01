<template>
  <div class="center">
    <md-progress-bar md-mode="buffer" :md-value="amount" :md-buffer="buffer"></md-progress-bar>
    <md-progress-bar class="md-accent" md-mode="buffer" :md-value="amount2" :md-buffer="buffer"></md-progress-bar>
    
    
    <md-button class="md-raised" :md-ripple="false" @click="go(2)">GO!</md-button>
    
    
    <!-- <div>
      Progress <br>
      <input type="range" v-model.number="amount"> {{ amount }}%
    </div>

    <div>
      Buffer <br>
      <input type="range" v-model.number="buffer"> {{ buffer }}%
    </div> -->
  </div>
</template>

<script>
// import axios from "axios";

  export default {
    name: 'EmptyStateBasic',

    data () {
      return{
        amount:0,
        amount2:0,
        buffer: 0,

        winflag: true,
        // restaurants
      }
    },
    computed: {


    },

    methods: {
      randomPick(num) {
        var result = Math.floor(Math.random() * ((num+1) - 1) + 1);
        return result
      },

      go(n){

        let idx = 1, tmpAmount = 0, tmpAmount2 = 0;

        while(100 >= tmpAmount && 100 >= tmpAmount2) {
            const num = this.randomPick(n);

            switch(num){
              case 1:
                tmpAmount += 1;
                break;
              case 2:
                tmpAmount2 += 1;
                break;
            } 
            
            const timeoutId = setTimeout(({tmpAmount, tmpAmount2, num}) => {
              if(1 === num)
                this.amount = tmpAmount;
              else
                this.amount2 = tmpAmount2;

              if(!(100 >= tmpAmount && 100 >= tmpAmount2)) {
                clearTimeout(timeoutId);
                return;
              }
            }, idx++ * 100, {tmpAmount, tmpAmount2, num})
        }


        /* 
          for(let step = 1; step <= 50; step++) {
              setTimeout(() => {
                switch(this.randomPick(n)){
                  case 1:
                    this.amount += 1;
                    break;
                  case 2:
                    this.amount2 += 1;
                    break;
                }
              }, step * 100)            
          }
        */

          /* 
          for (let step = 1; this.winflag == true; step++){
            // while(this.winflag){
              step +=1;
              if (this.amount === 10 || this.amount2 === 10){
                this.winflag = false
              } else {
                setTimeout(() => {
                  switch(this.randomPick(n)){
                    case 1:
                      this.amount += 1;
                      break;
                    case 2:
                      this.amount2 += 1;
                      break;
                  }
                }, step * 100)
            }
          }
          */
      },

    }


  }
</script>

<style lang="scss" scoped>
.md-progress-bar {
    margin: 24px;
  }

</style>