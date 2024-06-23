import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/home-view/HomeView.vue'
import AboutView from '@/views/about-view/AboutView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
