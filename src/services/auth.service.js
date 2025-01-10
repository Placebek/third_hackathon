import axios from 'axios';

const API_URL = 'http://172.20.10.3:8000';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + '/auth/login', {
        email_or_username: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post(API_URL + '/auth/register', {
      username: user.username,
      email: user.email,
      password: user.password
    });
  }
}

export default new AuthService();