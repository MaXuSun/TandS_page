import Vue from 'vue'
import User from "@/views/User";
import SignIn from "@/components/SignIn";
import SignUp from "@/components/SignUp";
import Display from "@/views/Display";
import Schedule from "@/views/Schedule";
import LogOut from "@/components/LogOut";
import Result from "@/views/Result";
import Search from "@/views/Search";
import Policy from "@/views/Policy";
import VueRouter from 'vue-router'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

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
      redirect: '/index/search',
      children: [
        {
          path: '/index/search',
          component: Search
        },
        {
          path: 'schedule',
          component: Schedule
        },
        {
          path:'result/:title',
          component:Result
        },
        {
          path:'policy',
          component:Policy
        }
      ]
    },

]

const router = new VueRouter({
  mode:'hash',
  routes
})

export default router
