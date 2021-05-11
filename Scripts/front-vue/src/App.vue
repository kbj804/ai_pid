<template>
  <div id="wrap">
    <Header
      v-if="isLoginPage()"
    />
    <Navigator 
      v-if="isLoginPage()" 
    />
  
  <div class="center">
    <router-view/>
  </div>

  </div>
  
</template>

<script>
/* Header, Navigator */
import Header from '@/components/common/Header.vue'
import Navigator from '@/components/common/Navigator.vue'
// import axios from "axios";
 
// let url = "http://localhost:8000/"; // FastAPI 서버 주소
/* css */

import '@/assets/vendor/bootstrap/css/bootstrap.min.css'
// import '@/assets/vendor/summernote/summernote-bs4.min.css'
// import '@/assets/vendor/summernote/summernote.min.css'

// import 'vue-material/dist/vue-material.min.css'
// import 'vue-material/dist/theme/default.css'
// import '@/assets/vendor/bootstrap-select/bootstrap-select.min.css'
import '@/assets/css/common.css'


/* js */
import { common } from '@/assets/js/common.js'
import '@/assets/vendor/bootstrap/js/bootstrap.bundle.min.js'
import '@/assets/vendor/bootstrap-select/bootstrap-select.min.js'
import '@/assets/vendor/jquery/jquery-3.3.1.min.js'
// import '@/assets/vendor/summernote/summernote-bs4.min.js'




/* jquery */
global.jQuery = require('jquery')
var $ = global.jQuery
window.$ = $


export default {
  name: 'App',
  components: {
    Header,
    Navigator
  },
  data () {
    return {

    }
  },
mounted () {
    var $body = $('body')
    var $tooltip = $('[data-toggle="tooltip"]')

    // 메뉴토글
    $('.menu-toggler').click(function () {
      $(this).hasClass('d-lg-none') ? common.panelOpen('sidebar') : $body.toggleClass('sidebar-toggled')
    })

    $(document).on('click', function (e) {
      var tg = '.panel-content'
      if (!$body.is($("[class*='panel-open']")) || $('[data-backdrop="false"]').is(':visible')) {
        return
      }
      if (!$(e.target).closest(tg).length && !$(e.target).is(tg)) {
        common.panelClose($(tg + ':visible').parents('.panel').attr('id'))
      }
    })

    $(document).on('click', '[data-toggle="toggle"]', function () {
      var $t = $(this)
      var txt = $t.data('class')
      var target = $t.data('target') || $t.attr('href')
      $(target).toggleClass(txt)
    })

    // tooltip
    $tooltip.length && $tooltip.tooltip()

    // select
    // var select = $('.selectpicker')
    // select.length && select.selectpicker()
    // select.on({
    //   'show.bs.select': function (e) {
    //     var label = $(e.target).parents('.form-control-label')
    //     label.length && label.addClass('active')
    //   },
    //   'hide.bs.select': function (e) {
    //     var label = $(e.target).parents('.form-control-label')
    //     label.length && label.removeClass('active')
    //   }
    // })
    $('.form-control-label:not(.label-select)').on({
      click: function () {
        $(this).addClass('active')
      },
      focusout: function () {
        $(this).removeClass('active')
      }
    })

    // input
    $('th .custom-control-input').prop('indeterminate', true)
    $('button.custom-switch').click(function () {
      $(this).toggleClass('checked')
    })

    // tab
    $('[data-tab="multi"]').click(function () {
      $('[data-tab-target]').removeClass('active')
      $('[data-tab-target="' + $(this).attr('href') + '"]').addClass('active')
    })
  },

  methods: {
    /* 로그인 페이지에서는 Header, Navigator 숨기기 */
    isLoginPage () {
      console.log('location.pathname !== ', location.pathname !== '/login')
      return location.pathname !== '/login' // 현재주소가 /login 이 아니라면 true
    }
  }


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
textarea:focus {
  outline: none;
}
button:focus {
  outline: none;
}
input:focus {
  outline: none;
}

.center{
  margin: 0 auto;
  width: 100%;
  height: 100%;
}


</style>
