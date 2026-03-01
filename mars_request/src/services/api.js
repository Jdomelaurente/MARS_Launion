import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add a request interceptor to include the JWT token In headers
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export const authService = {
    login(username, password) {
        return apiClient.post('login/', { username, password });
    },
    register(userData) {
        return apiClient.post('register/', userData);
    },
    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    },
};

export const requestService = {
    submitRequest(data) {
        return apiClient.post('requests/', data);
    },
    lookupRequest(code) {
        return apiClient.get(`requests/lookup/${code}/`);
    },
};

export default apiClient;
