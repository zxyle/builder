import {request} from "umi";

function getTags() {
  return request('/api/tags')
}

export default {
  getTags,
};
