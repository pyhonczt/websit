import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/page/layout'
import Main from '@/page/main'
import User from '@/page/user'
import Web from '@/page/web'
import Git from '@/page/git'
import Movie from '@/page/movie'
import Book from '@/page/book'
import Technology from '@/page/technology'
import Blog from '@/page/blog'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      children: [{
        path: '/',
        name: 'Main',
        component: Main
      },
      {
        path: '/user',
        name: 'User',
        component: User
      },
      {
        path: '/web',
        name: 'Web',
        component: Web
      },
      {
        path: '/git',
        name: 'Git',
        component: Git
      },
      {
        path: '/movie',
        name: 'Movie',
        component: Movie
      },
      {
        path: '/book',
        name: 'Book',
        component: Book
      },
      {
        path: '/technology',
        name: 'Technology',
        component: Technology
      },
      {
        path: '/blog',
        name: 'Blog',
        component: Blog
      }]
    }
  ]
})
