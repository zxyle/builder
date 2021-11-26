export default [
  // 每个路由 也可以配置Title
  // @代表src 相对路径就从src/pages开始找
  // route 可以配置子路由
  { path: '/', component: '@/pages/index', title: '首页' },
  { path: '/demo', component: '@/pages/demo' },
  // 没有匹配到路由的兜底
  { component: '@/pages/404' },
]
