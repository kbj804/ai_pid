import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue')
  },
  {
    path: '/info',
    name: 'info',
    component: () => import(/* webpackChunkName: "info" */ '../views/Info.vue')

  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue')
  },
  {
    path: '/board',
    name: 'board',
    component: () => import(/* webpackChunkName: "board" */ '../views/Board.vue')
  },
  {
    path: '/doc/git',
    name: 'git',
    component: () => import(/* webpackChunkName: "git" */ '../views/doc/Github.vue')
  },
  {
    path: '/doc/blog',
    name: 'blog',
    component: () => import(/* webpackChunkName: "blog" */ '../views/doc/Blog.vue')
  },
  {
    path: '/doc/test',
    name: 'test',
    component: () => import(/* webpackChunkName: "test" */ '../views/Board.vue')
  },
  {
    path: '/pi',
    name: 'pi',
    component: () => import(/* webpackChunkName: "pi" */ '../views/PersonalInfo/PiView.vue')
  },
  {
    path: '/pi/uploadfiles',
    name: 'uploadfiles',
    component: () => import(/* webpackChunkName: "uploadfiles" */ '../views/PersonalInfo/UploadFilesView.vue')
  },
  {
    path: '/pi/mldetect',
    name: 'mldetect',
    component: () => import(/* webpackChunkName: "mldetect" */ '../views/PersonalInfo/mlDetectView.vue')
  },
  {
    path: '/toy',
    name: 'ToyProject',
    component: () => import(/* webpackChunkName: "mldetect" */ '../views/toyProject/staffView.vue')
  },
  // {
  //   path: '/profile',
  //   name: 'profile',
  //   component: () => import(/* webpackChunkName: "profile" */ '../views/profile/Profile.vue')
  // },
  // {
  //   path: '/profile/edit',
  //   name: 'profileEdit',
  //   component: () => import(/* webpackChunkName: "profileEdit" */ '../views/profile/ProfileEdit.vue')
  // }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })


  export default router
