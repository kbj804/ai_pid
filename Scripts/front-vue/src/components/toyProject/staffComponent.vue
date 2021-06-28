<template>
  <div>
    <md-table v-model="users" :md-sort.sync="currentSort" :md-sort-order.sync="currentSortOrder" :md-sort-fn="customSort" md-card>
      <md-table-toolbar>
        <h1 class="md-title">스태프 목록</h1>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-numeric>{{ item.id }}</md-table-cell>
        <md-table-cell md-label="이름" md-sort-by="name">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="이메일" md-sort-by="email">{{ item.email }}</md-table-cell>
        <md-table-cell md-label="성별" md-sort-by="gender">{{ item.gender }}</md-table-cell>
        <md-table-cell md-label="Job Title" md-sort-by="title">{{ item.title }}</md-table-cell>
        <md-table-cell md-label="경력" md-sort-by="title">{{ item.due }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>

  export default {
    name: 'toyProjecrStaff',

    data () {
      return{
    currentSort: 'name',
      currentSortOrder: 'asc',
      users: [
        {
          id: 1,
          name: 'Shawna Dubbin',
          email: 'sdubbin0@geocities.com',
          gender: 'Male',
          title: '미디어 플래너',
          due: '3년'
        },
        {
          id: 2,
          name: 'Odette Demageard',
          email: 'odemageard1@spotify.com',
          gender: 'Female',
          title: '코디네이터',
          due: '1년'
        },
        {
          id: 3,
          name: 'Lonnie Izkovitz',
          email: 'lizkovitz3@youtu.be',
          gender: 'Female',
          title: '감독',
          due: '5년'
        },
        {
          id: 4,
          name: 'Thatcher Stave',
          email: 'tstave4@reference.com',
          gender: 'Male',
          title: '데이터 매니저',
          due: '6년'
        },
        {
          id: 5,
          name: 'Clarinda Marieton',
          email: 'cmarietonh@theatlantic.com',
          gender: 'Female',
          title: '카메라',
          due: '1년'
        },
      ]
      }
    },
    

    methods: {
        customSort (value) {
        return value.sort((a, b) => {
          const sortBy = this.currentSort

          if (this.currentSortOrder === 'desc') {
            return a[sortBy].localeCompare(b[sortBy])
          }

          return b[sortBy].localeCompare(a[sortBy])
        })
      }
    
      
  
    }


  }
</script>

<style lang="scss" scoped>



</style>