/* eslint camelcase: 0 */

import axios from "axios";

const tokenConfig = token => ({
  headers: {
    Authorization: token // eslint-disable-line quote-props
  }
});

export function validate_token(token) {
  return axios.post("http://127.0.0.1:5000/api/is_token_valid", {
    token
  });
}

export function create_user(first_name, last_name, email, password) {
  return axios.post("http://127.0.0.1:5000/api/create_user", {
    first_name,
    last_name,
    email,
    password
  });
}

export function get_token(email, password) {
  return axios.post("http://127.0.0.1:5000/api/get_token", {
    email,
    password
  });
}

export function data_about_user(token) {
  return axios.get("http://127.0.0.1:5000/api/user", tokenConfig(token));
}

export function store_task(token, user_id, task, status) {
  return axios.post("http://127.0.0.1:5000/api/submit_task", {
    task,
    user_id,
    status
  },
  tokenConfig(token));
}

export function delete_task(token, task_id) {
  return axios.post("http://127.0.0.1:5000/api/delete_task", {
    task_id
  },
  tokenConfig(token));
}

export function edit_task(token, task_id, task, status) {
  return axios.post("http://127.0.0.1:5000/api/edit_task", {
    task_id,
    task,
    status
  },
  tokenConfig(token));
}