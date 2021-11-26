import service from './service';

export default{
  namespace: 'demo',

  subscriptions: {
    setup({ dispatch, history }) {
      history.listen(({ pathname }) => {
        if (pathname === '/demo') {
          // dispatch({ type: 'reset' });
          dispatch({ type: 'fetchTags' });
        }
      });
    },

  },

  state: {
    tagsList: []
  },

  // 调用API接口，获取数据，
  effects: {
    // payload 是参数
    // callback
    // put 将数据传递给reducers的方法
    // call
    * fetchTags({payload, callback}, {put, call}) {
      // 获取tags数据
      const response = yield call(service.getTags)

      // 调用reducers
      yield put({
        // reducers名称
        type: 'setTagsList',
        // 被传递的数据
        payload: response.list

      })
    }

  },

  // 更新state
  reducers: {
    setTagsList(state, action) {
      return {...state, tagsList: action.payload}

    }

  },

};
