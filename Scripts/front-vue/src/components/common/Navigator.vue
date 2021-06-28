<template>
  <nav
    id="sidebar"
    class="panel"
  >
    <div
      class="panel-content"
      style="
    width: 237px;"
    >
      <ul id="gnb">
        <li v-for="menu in menuList"  v-bind:key="menu.name">
          <a v-if="isChildren(menu)"
              :href="menu.href"
              class="menu-collapse-link collapsed"
              data-toggle="collapse"
              ><i :class="menu.icon" />{{menu.name}}<i class="icon-down text-dark"/></a>
              <ul v-if="isChildren(menu)"
                :id="menu.id"
                class="menu-collapse collapse"
                data-parent="#gnb">
                  <li v-for="child in menu.children" :key="child.name"
                    class="menu-item">
                    <a
                      href="javascript:void(0);"
                      class="menu-link"
                      @click="goto(child.url)"
                    >{{child.name}}</a>
                  </li>
              </ul>
              
            <a v-else-if="menu.name === 'Visualization'"
              class="menu-collapse-link collapsed"
              style="color: #CFD8DC"
              data-toggle="collapse"
            ><i class="icon-graph text-dark" />{{menu.name}}</a>
            
            <a v-else
              href="javascript:void(0);"
              class="menu-collapse-link collapsed"
              @click="goto(menu.url)"
              ><i :class="menu.icon" />{{menu.name}}</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'Navigator',
  computed: {
  },
  methods: {
      goto(url) {
        this.$router.push(url);
      },
      isChildren(menu) {
        return menu.children
      }
  },
  data () {
    return {
        menuList: [
          { name: 'Info', url: '/info', icon: 'icon-std-code text-dark' },
          { name: 'Document', url: '/doc', icon: 'icon-result text-dark', id:'doc', href:'#doc',
            children: [
              {name: 'Github', url: '/doc/git'},
              {name: 'Blog', url: '/doc/blog'},
              {name: 'Test', url: '/doc/test'}
            ]
          },
          { name: 'Personal Information', icon: 'icon-arrange text-dark', id:'PI', href:'#PI',
            children: [
              {name: 'LoadFiles', url: '/pi'},
              {name: 'UploadFiles', url: '/pi/uploadfiles'},
              {name: 'ML Detection', url: '/pi/mldetect'}
            ]
          },
          { name: 'Beta Model', url: '/betamodel', icon: 'icon-alarm text-dark'},
          { name: 'Visualization', url: '/visual', icon: 'icon-graph text-dark'},
          { name: 'ToyProject', url: '/toy', icon: 'text-dark'},
          { name: 'Profile', url: '/profile', icon: 'icon-user text-dark'},
        ]
    }
  }
}
</script>

<style>

</style>
