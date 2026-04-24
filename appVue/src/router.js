import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CoursesView from './views/CoursesView.vue'
import LessonView from './views/LessonView.vue'
import CourseDetailView from './views/CourseDetailView.vue'
import AdminView from './views/AdminView.vue'
import LoginView from './views/LoginView.vue'
import RegisterView from './views/RegisterView.vue'
import ProfileView from './views/ProfileView.vue'
import ChatView from './views/ChatView.vue'
import InstructorView from './views/InstructorView.vue'

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
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView
    },
    {
      path: '/instructor',
      name: 'instructor',
      component: InstructorView
    }
  ]
})

export default router
