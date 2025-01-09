'use strict'

import axios from 'axios'
import qs from 'qs'

axios.interceptors.request.use(config => {
  return config
}, error => {
  return Promise.reject(error)
})

axios.interceptors.response.use(response => {
  return response
}, error => {
  return Promise.resolve(error.response)
})

function checkStatus (response) {
  if (response && (response.status === 200 || response.status === 304 || response.status === 400)) {
    return response
  }
  return {
    status: -404,
    msg: '网络异常'
  }
}

function checkCode (res) {
  if (res.status === -404) {
    alert(res.msg)
  }
  if (res.data && (!res.data.success)) {
    alert(res.data.error_msg)
  }
  return res
}

export default {
  post (url, data) {
    return axios({
      method: 'post',
      baseURL: 'https://172.20.10.8/',
      url,
      data: qs.stringify(data),
      timeout: 10000,
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      }
    }).then(
      (response) => {
        return checkStatus(response)
      }
    ).then(
      (res) => {
        return checkCode(res)
      }
    )},
    get (url, params) {
      return axios({
        method: 'get',
        baseURL: 'https://172.20.10.8/',
        url,
        params, 
        timeout: 10000,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      }).then(
        (response) => {
          return checkStatus(response)
        }
      ).then(
        (res) => {
          return checkCode(res)
        }
      )
  },
};