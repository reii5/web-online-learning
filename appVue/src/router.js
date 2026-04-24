import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CoursesView from './views/CoursesView.vue'
import LessonView from './views/LessonView.vue'
import CourseDetailView from './views/CourseDetailView.vue'
import AdminView from './views/AdminView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesView
    },
    {
      path: '/lesson',
      name: 'lesson',
      component: LessonView
    },
    {
      path: '/course-detail',
      name: 'course-detail',
      component: CourseDetailView
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView
    }
  ]
})

export default router
