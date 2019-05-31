export default function ({$axios, redirect, app}) {
  $axios.onResponse(({data}) => {
    if (data.code !== 200) {
      app.$toast.error(data.result);
      return Promise.reject('response error');
    }
  });

  $axios.onError(error => {
    if (error !== "response error") {
      app.$toast.error("请求错误");
    }
  })
}
