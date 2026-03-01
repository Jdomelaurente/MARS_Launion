import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/Staff/login',
    },
    {
      path: '/Staff/login',
      name: 'login',
      component: () => import('../views/auth/login.vue'),
    },
    {
      path: '/Staff/register',
      name: 'register',
      component: () => import('../views/auth/register.vue'),
    },
    {
      path: '/staff/dashboard',
      name: 'staff-dashboard',
      component: () => import('../views/Staff/Staff_dashboard.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/requestor/home',
      name: 'requestor-home',
      component: () => import('../views/requestor/requestor_home.vue'),
    },
    {
      path: '/requestor/request-details/:code',
      name: 'request-details',
      component: () => import('../views/requestor/request_details.vue'),
    },
  ],
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/Staff/login');
  } else if ((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    next('/staff/dashboard');
  } else {
    next();
  }
});

export default router
