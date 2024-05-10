import { createRouter, createWebHistory } from 'vue-router'

import CartView from '@/views/CartView.vue'
import ProductListView from '@/views/ProductListView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ProductListView
    },
    {
      path: '/:video_id',
      name: 'search-detail',
      component: SearchDetailView
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    }

  ]
})

export default router
