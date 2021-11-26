import React from 'react';
import {useSelector} from 'dva';

const Demo = () => {
  const {tagsList} = useSelector((state) => state.demo);
  console.log(tagsList)
  // console.log(tagsList.list);

  const list = tagsList || [];
  console.log(list);

  return (
    <div>
      {
        list.map((item, index) => {
          return <p key={index}>{item.name}</p>
        })
      }

    </div>
  );
};

export default Demo;
