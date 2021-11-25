import { defineConfig } from 'umi';

export default defineConfig({
  hash: true,

  title: 'XX网站',

  // favicon: '/rocket.png',

  mfsu: {},

  dva: {
    hmr: true,
    immer: true,
  },

  locale: {
    default: 'zh-CN',
    antd: true,
    title: true,
    baseNavigator: true,
    baseSeparator: '-',
  },

  proxy: {
    '/api': {
    'target': 'http://127.0.0.1:8080/',
    'changeOrigin': true,
    'pathRewrite': { '^/api' : '' },
    },
  },
  nodeModulesTransform: {
    type: 'none',
  },
  routes: [
    { path: '/', component: '@/pages/index' },
  ],
  fastRefresh: {},
});
