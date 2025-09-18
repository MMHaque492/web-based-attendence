import axios from 'axios';


const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000';


export const api = axios.create({
baseURL: API_BASE,
timeout: 10000,
});


// EXAMPLE: auth.login
export const login = (email, deviceId) => api.post('/auth/login', {email, device_id: deviceId});


// PLACEHOLDERS: other API calls used across the UI
export const createSession = (payload) => api.post('/session/create', payload);
export const markAttendance = (payload) => api.post('/attendance/mark', payload);
export const verifyFace = (formData) => api.post('/face/verify', formData, {headers: {'Content-Type': 'multipart/form-data'}});
