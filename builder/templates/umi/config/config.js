import { defineConfig } from 'umi';
import routes from './routes';
import defaultSettings from './defaultSettings';
import proxy from './proxy';

export default defineConfig({
  nodeModulesTransform: {
    type: 'none',
  },

  // 生成的文件加上hash后缀，避免浏览器缓存
  hash: true,

  // 设置路由前缀
  // base: '/admin/',

  // 可以用来设置静态资源的cdn地址前缀
  // publicPath: 'https://xxx.com/static/',

  // 修改默认打包后的目录名（默认是dist）
  // outputPath: 'release',

  // 设置html title标签文本
  title: defaultSettings.title,

   // favicon: '/rocket.png',

   mfsu: {},

  // history: {
  //   // hash 会在链接后加上#号
  //   'type': 'hash'
  // },

  // 配置需要兼容的浏览器最低版本
  // targets:{
  //   ie: 11
  // },

  // 修改主题色调
  theme: {
    '@primary-color': defaultSettings.primaryColor,
  },

  // 路由配置
  routes: routes,

  //
  fastRefresh: {},

  // mock关闭
  mock: false,

  //
  proxy: proxy['dev'],

  // 国际化
  locale: {
    default: 'zh-CN',
    antd: true,
    title: true,
    baseNavigator: true,
    baseSeparator: '-',
  },

  // DVA
  dva: {
    immer: true,
    hmr: true,
  },

});
