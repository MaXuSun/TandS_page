import Vue from 'vue'
import User from "@/views/User";
import SignIn from "@/components/SignIn";
import SignUp from "@/components/SignUp";
import Display from "@/views/Display";
import Schedule from "@/components/Schedule";
import LogOut from "@/components/LogOut";
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
    {
      path:'/',
      redirect: '/user/signin'
    },
    {
      path:'/user',
      redirect: '/user/signin',
      component: User,
      children:[
        {
          path:'/user/signin',
          component:SignIn
        },
        {
          path:'/user/signup',
          component: SignUp
        },
        {
          path:'/user/logout',
          component: LogOut
        }
      ]
    },
    {
      path:'/index',
      component: Display,
      children: [
        {
          path: 'schedule',
          component: Schedule
        }
      ]
    },

]

const router = new VueRouter({
  mode:'history',
  routes
})

export default router
